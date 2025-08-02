from typing import override

from rcrscore.commands.command import Command
from rcrscore.entities.entity_id import EntityID
from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.command import CommandURN
from rcrscore.urn.component_command import ComponentCommandURN
from rcrscore.urn.component_control_message import ComponentControlMessageURN


class AKMove(Command):
  def __init__(
    self,
    agent_id: EntityID,
    time: int,
    path: list[EntityID],
    destination_x: int = -1,
    destination_y: int = -1,
  ) -> None:
    """
    Command to move an agent along a specified path to a destination.

    Attributes:
      agent_id: The ID of the agent to move.
      time: Simulation time
      path: The path to move the agent along.
      destination_x: The X coordinate to move the agent to (Default: -1).
      destination_y: The Y coordinate to move the agent to (Default: -1).

    """
    self.agent_id: EntityID = agent_id
    self.path: list[EntityID] = path
    self.time: int = time
    self.x: int = destination_x
    self.y: int = destination_y

  @override
  @staticmethod
  def get_urn() -> CommandURN:
    return CommandURN.AK_MOVE

  @override
  def to_message_proto(self) -> MessageProto:
    msg: MessageProto = MessageProto()
    msg.urn = self.get_urn()
    msg.components[
      ComponentControlMessageURN.AgentID
    ].entityID = self.agent_id.get_value()
    msg.components[ComponentControlMessageURN.Time].intValue = self.time
    msg.components[ComponentCommandURN.DestinationX].intValue = self.x
    msg.components[ComponentCommandURN.DestinationY].intValue = self.y
    msg.components[ComponentCommandURN.Path].entityIDList.values.extend(
      [id.get_value() for id in self.path]
    )
    return msg
