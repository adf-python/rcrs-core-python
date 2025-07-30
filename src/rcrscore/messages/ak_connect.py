from rcrscore.messages.message import AKControlMessage
from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.component_control_message import ComponentControlMessageURN
from rcrscore.urn.control_message import ControlMessageURN


class AKConnect(AKControlMessage):
  @staticmethod
  def write(request_id: int, agent) -> MessageProto:
    msg = MessageProto()
    msg.urn = AKConnect.get_urn()
    msg.components[ComponentControlMessageURN.RequestID].intValue = request_id
    msg.components[ComponentControlMessageURN.Version].intValue = 2
    msg.components[ComponentControlMessageURN.Name].stringValue = agent.name
    for urn in agent.get_requested_entities():
      msg.components[
        ComponentControlMessageURN.RequestedEntityTypes
      ].intList.values.append(urn)

    return msg

  @staticmethod
  def get_urn() -> ControlMessageURN:
    return ControlMessageURN.AK_CONNECT
