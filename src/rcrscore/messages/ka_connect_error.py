from rcrscore.messages.message import KAControlMessage
from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.component_control_message import ComponentControlMessageURN
from rcrscore.urn.control_message import ControlMessageURN


class KAConnectError(KAControlMessage):
  def __init__(self, message_proto: MessageProto) -> None:
    self.read(message_proto)

  def read(self, message_proto: MessageProto) -> None:
    self.request_id: int = message_proto.components[
      ComponentControlMessageURN.RequestID
    ].intValue
    self.reason: str = message_proto.components[
      ComponentControlMessageURN.Reason
    ].stringValue

  @staticmethod
  def get_urn() -> ControlMessageURN:
    return ControlMessageURN.KA_CONNECT_ERROR
