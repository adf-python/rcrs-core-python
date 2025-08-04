import argparse
import ipaddress
import logging
import time
from dataclasses import dataclass
from enum import Enum
from multiprocessing import Process
from typing import Dict, Optional, Type

from rcrscore.agents.agent import Agent
from rcrscore.agents.ambulance_center_agent import AmbulanceCenterAgent
from rcrscore.agents.ambulance_team_agent import AmbulanceTeamAgent
from rcrscore.agents.fire_brigade_agent import FireBrigadeAgent
from rcrscore.agents.fire_station_agent import FireStationAgent
from rcrscore.agents.police_force_agent import PoliceForceAgent
from rcrscore.agents.police_office_agent import PoliceOfficeAgent
from rcrscore.connection.component_launcher import ComponentLauncher
from rcrscore.constants.constants import (
  DEFAULT_KERNEL_HOST_NAME,
  DEFAULT_KERNEL_PORT_NUMBER,
)


class AgentType(Enum):
  """Available agent types."""

  FIRE_BRIGADE = "fb"
  FIRE_STATION = "fs"
  POLICE_FORCE = "pf"
  POLICE_OFFICE = "po"
  AMBULANCE_TEAM = "at"
  AMBULANCE_CENTER = "ac"


@dataclass
class LaunchConfig:
  """Configuration for launching agents."""

  host: str
  port: int
  precompute: bool
  agent_counts: Dict[AgentType, int]
  start_delay: float = 0.01  # Delay between starting agents (seconds)


class AgentRegistry:
  """Registry for mapping agent types to their classes."""

  _AGENT_CLASSES: Dict[AgentType, Type[Agent]] = {
    AgentType.FIRE_BRIGADE: FireBrigadeAgent,
    AgentType.FIRE_STATION: FireStationAgent,
    AgentType.POLICE_FORCE: PoliceForceAgent,
    AgentType.POLICE_OFFICE: PoliceOfficeAgent,
    AgentType.AMBULANCE_TEAM: AmbulanceTeamAgent,
    AgentType.AMBULANCE_CENTER: AmbulanceCenterAgent,
  }

  @classmethod
  def get_agent_class(cls, agent_type: AgentType) -> Type[Agent]:
    """Get the agent class for the given type."""
    if agent_type not in cls._AGENT_CLASSES:
      raise ValueError(f"Unknown agent type: {agent_type}")
    return cls._AGENT_CLASSES[agent_type]

  @classmethod
  def get_available_types(cls) -> list[AgentType]:
    """Get all available agent types."""
    return list(cls._AGENT_CLASSES.keys())


class ArgumentParser:
  """Handles command line argument parsing."""

  DEFAULT_AGENT_COUNT = 0
  MAX_AGENT_COUNT_FOR_ALL = 100

  def __init__(self) -> None:
    self.parser = self._create_parser()

  def _create_parser(self) -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
      description="Launch RCRS agents",
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog="""
Examples:
  %(prog)s -fb 5 -at 3 -precompute true
  %(prog)s -h 192.168.1.100 -p 27931 -fb -1
  %(prog)s --all-agents 10
            """,
    )

    # Connection settings
    connection_group = parser.add_argument_group("Connection Settings")
    connection_group.add_argument(
      "--host",
      default=DEFAULT_KERNEL_HOST_NAME,
      help=f"RCRS server host IP (default: {DEFAULT_KERNEL_HOST_NAME})",
    )
    connection_group.add_argument(
      "-p",
      "--port",
      type=int,
      default=int(DEFAULT_KERNEL_PORT_NUMBER),
      help=f"RCRS server port number (default: {DEFAULT_KERNEL_PORT_NUMBER})",
    )

    # Agent settings
    agent_group = parser.add_argument_group("Agent Settings")
    agent_group.add_argument(
      "-pre",
      "--precompute",
      type=self._str_to_bool,
      default=False,
      help="Enable precompute flag (default: false)",
    )

    # Individual agent counts
    for agent_type in AgentRegistry.get_available_types():
      agent_group.add_argument(
        f"-{agent_type.value}",
        type=int,
        default=self.DEFAULT_AGENT_COUNT,
        metavar="COUNT",
        help=f"Number of {agent_type.name.replace('_', ' ').title()} agents "
        f"(-1 to run {self.MAX_AGENT_COUNT_FOR_ALL}, default: {self.DEFAULT_AGENT_COUNT})",
      )

    # Convenience option
    agent_group.add_argument(
      "--all-agents",
      type=int,
      metavar="COUNT",
      help="Set the same count for all agent types",
    )

    # Advanced settings
    advanced_group = parser.add_argument_group("Advanced Settings")
    advanced_group.add_argument(
      "--start-delay",
      type=float,
      default=0.01,
      help="Delay between starting agents in seconds (default: 0.01)",
    )
    advanced_group.add_argument(
      "--log-level",
      choices=["DEBUG", "INFO", "WARNING", "ERROR"],
      default="INFO",
      help="Set logging level (default: INFO)",
    )

    return parser

  @staticmethod
  def _str_to_bool(value: str) -> bool:
    """Convert string to boolean."""
    if value.lower() in ("true", "yes", "1", "on"):
      return True
    elif value.lower() in ("false", "no", "0", "off"):
      return False
    else:
      raise argparse.ArgumentTypeError(f"Boolean value expected, got: {value}")

  def parse_args(self, args: Optional[list[str]] = None) -> LaunchConfig:
    """Parse command line arguments and return configuration."""
    parsed_args = self.parser.parse_args(args)

    # Set up logging
    logging.basicConfig(
      level=getattr(logging, parsed_args.log_level),
      format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Validate host
    host = self._validate_host(parsed_args.host)

    # Validate port
    port = self._validate_port(parsed_args.port)

    # Process agent counts
    agent_counts = self._process_agent_counts(parsed_args)

    return LaunchConfig(
      host=host,
      port=port,
      precompute=parsed_args.precompute,
      agent_counts=agent_counts,
      start_delay=parsed_args.start_delay,
    )

  def _validate_host(self, host: str) -> str:
    """Validate host address."""
    if host == "localhost":
      return host

    try:
      ipaddress.ip_address(host)
      return host
    except ValueError as e:
      raise argparse.ArgumentTypeError(f"Invalid host address '{host}': {e}")

  def _validate_port(self, port: int) -> int:
    """Validate port number."""
    if not (1 <= port <= 65535):
      raise argparse.ArgumentTypeError(f"Port must be between 1 and 65535, got: {port}")
    return port

  def _process_agent_counts(self, args: argparse.Namespace) -> Dict[AgentType, int]:
    """Process agent count arguments."""
    agent_counts = {}

    # If --all-agents is specified, use that for all types
    if args.all_agents is not None:
      for agent_type in AgentRegistry.get_available_types():
        agent_counts[agent_type] = args.all_agents
    else:
      # Process individual agent counts
      for agent_type in AgentRegistry.get_available_types():
        count = getattr(args, agent_type.value)
        if count == -1:
          count = self.MAX_AGENT_COUNT_FOR_ALL
        elif count < 0:
          raise argparse.ArgumentTypeError(
            f"Agent count must be >= 0 or -1 for all, got: {count}"
          )
        agent_counts[agent_type] = count

    # Validate total agent count
    total_agents = sum(agent_counts.values())
    if total_agents == 0:
      logging.warning("No agents will be launched")
    elif total_agents > 1000:
      logging.warning(f"Large number of agents ({total_agents}) may impact performance")

    return agent_counts


class Launcher:
  """Main launcher class for RCRS agents."""

  def __init__(self) -> None:
    self.logger = logging.getLogger(__name__)
    self.agent_registry = AgentRegistry()

  def run(self, config: LaunchConfig) -> None:
    """
    Launch agents based on the provided configuration.

    Args:
        config: Launch configuration
    """
    self.logger.info(f"Starting launcher with config: {config}")

    # Create component launcher
    component_launcher = ComponentLauncher(config.host, config.port)

    # Launch agents
    processes = self._launch_agents(component_launcher, config)

    if not processes:
      self.logger.warning("No agents were launched")
      return

    self.logger.info(f"Launched {len(processes)} agent processes")

    # Wait for all processes to complete
    try:
      for process in processes:
        process.join()
    except KeyboardInterrupt:
      self.logger.info("Received interrupt signal, terminating agents...")
      self._terminate_processes(processes)

  def _launch_agents(
    self, component_launcher: ComponentLauncher, config: LaunchConfig
  ) -> list[Process]:
    """Launch all agent processes."""
    processes = []
    total_agents = sum(config.agent_counts.values())
    launched_count = 0

    for agent_type, count in config.agent_counts.items():
      if count <= 0:
        continue

      agent_class = self.agent_registry.get_agent_class(agent_type)

      for i in range(count):
        try:
          process = self._launch_single_agent(
            component_launcher,
            agent_class,
            config.precompute,
            f"{agent_type.name}_{i + 1}",
          )
          processes.append(process)
          launched_count += 1

          self.logger.debug(
            f"Launched {agent_type.name} {i + 1}/{count} "
            f"(Total: {launched_count}/{total_agents})"
          )

          # Add delay between launches to avoid overwhelming the server
          if config.start_delay > 0:
            time.sleep(config.start_delay)

        except Exception as e:
          self.logger.error(f"Failed to launch {agent_type.name} agent: {e}")

    return processes

  def _launch_single_agent(
    self,
    component_launcher: ComponentLauncher,
    agent_class: Type[Agent],
    precompute: bool,
    agent_name: str,
  ) -> Process:
    """Launch a single agent process."""
    request_id = component_launcher.generate_request_id()
    agent_instance = agent_class(precompute)

    process = Process(
      target=component_launcher.connect,
      args=(agent_instance, request_id),
      name=agent_name,
    )
    process.start()

    return process

  def _terminate_processes(self, processes: list[Process]) -> None:
    """Terminate all agent processes."""
    for process in processes:
      if process.is_alive():
        process.terminate()
        process.join(timeout=5)
        if process.is_alive():
          self.logger.warning(f"Force killing process {process.name}")
          process.kill()
