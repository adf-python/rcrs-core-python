from abc import ABC, abstractmethod

from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.control_message import ControlMessageURN


class ControlMessage(ABC):
  @abstractmethod
  @staticmethod
  def get_urn() -> ControlMessageURN:
    raise NotImplementedError("Subclasses must implement get_urn method")


class AKControlMessage(ControlMessage, ABC):
  @abstractmethod
  @staticmethod
  def get_urn() -> ControlMessageURN:
    raise NotImplementedError("Subclasses must implement get_urn method")

  @abstractmethod
  @staticmethod
  def write():
    raise NotImplementedError("Subclasses must implement write method")


class KAControlMessage(ControlMessage, ABC):
  @abstractmethod
  @staticmethod
  def get_urn() -> ControlMessageURN:
    raise NotImplementedError("Subclasses must implement get_urn method")

  @abstractmethod
  def read(self, message_proto: MessageProto) -> None:
    raise NotImplementedError("Subclasses must implement read method")
