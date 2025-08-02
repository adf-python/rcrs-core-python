from typing import override

from rcrscore.commands.command import Command
from rcrscore.entities.entity_id import EntityID
from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.command import CommandURN
from rcrscore.urn.component_command import ComponentCommandURN
from rcrscore.urn.component_control_message import ComponentControlMessageURN


class AKClear(Command):
  def __init__(self, agent_id: EntityID, time: int, target_id: EntityID) -> None:
    self.agent_id = agent_id
    self.time = time
    self.target_id = target_id

  @staticmethod
  @override
  def get_urn() -> CommandURN:
    return CommandURN.AK_CLEAR

  @override
  def to_message_proto(self) -> MessageProto:
    msg: MessageProto = MessageProto()
    msg.urn = self.get_urn()
    msg.components[
      ComponentControlMessageURN.AgentID
    ].entityID = self.agent_id.get_value()
    msg.components[ComponentControlMessageURN.Time].intValue = self.time
    msg.components[ComponentCommandURN.Target].entityID = self.target_id.get_value()
    return msg
