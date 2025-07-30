from rcrscore.entities.entity_id import EntityID
from rcrscore.messages.message import AKControlMessage
from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.component_control_message import ComponentControlMessageURN
from rcrscore.urn.control_message import ControlMessageURN


class AKAcknowledge(AKControlMessage):
  @staticmethod
  def write(request_id: int, agent_id: EntityID) -> MessageProto:
    msg = MessageProto()
    msg.urn = AKAcknowledge.get_urn()
    msg.components[ComponentControlMessageURN.RequestID].intValue = request_id
    msg.components[ComponentControlMessageURN.AgentID].entityID = agent_id.get_value()
    return msg

  @staticmethod
  def get_urn() -> ControlMessageURN:
    return ControlMessageURN.AK_ACKNOWLEDGE
