from rcrscore.messages.ka_connect_error import KAConnectError
from rcrscore.messages.ka_connect_ok import KAConnectOK
from rcrscore.messages.ka_sense import KASense
from rcrscore.messages.message import ControlMessage
from rcrscore.messages.shutdown import Shutdown
from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.control_message import ControlMessageURN


class ControlMessageFactory:
  @staticmethod
  def make_message(msg: MessageProto) -> ControlMessage:
    match msg.urn:
      case ControlMessageURN.KA_SENSE:
        return KASense(msg)
      case ControlMessageURN.KA_CONNECT_OK:
        return KAConnectOK(msg)
      case ControlMessageURN.KA_CONNECT_ERROR:
        return KAConnectError(msg)
      case ControlMessageURN.SHUTDOWN:
        return Shutdown()
      case _:
        raise ValueError(f"Unknown control message URN: {msg.urn}")
