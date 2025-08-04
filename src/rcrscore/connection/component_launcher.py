import traceback

from rcrscore.agents.agent import Agent
from rcrscore.connection.connection import Connection
from rcrscore.logger.logger import ClientLoggerSingleton


class ComponentLauncher:
  def __init__(self, host: str, port: int) -> None:
    self.request_id: int = 0
    self.host: str = host
    self.port: int = port

  def connect(self, agent: Agent, request_id: int) -> None:
    with Connection(self.host, self.port) as connection:
      connection.set_agent_message_handler(agent.message_handlers)
      agent.set_send_msg(connection.send_message)
      agent.send_connect(request_id)
      try:
        connection.parse_message_from_kernel()
      except Exception as e:
        ClientLoggerSingleton.get_instance().warning(
          f"Connection to kernel {self.host}:{self.port} failed, Error: {e}\n{traceback.format_exc()}"
        )

  def generate_request_id(self) -> int:
    self.request_id += 1
    return self.request_id
