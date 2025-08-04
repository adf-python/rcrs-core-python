from rcrscore.messages.message import ControlMessage
from rcrscore.urn.control_message import ControlMessageURN


class Shutdown(ControlMessage):
  @staticmethod
  def get_urn() -> ControlMessageURN:
    return ControlMessageURN.SHUTDOWN
