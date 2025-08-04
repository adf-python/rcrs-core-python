from abc import ABC, abstractmethod
from typing import Any

from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.control_message import ControlMessageURN


class ControlMessage(ABC):
  @staticmethod
  @abstractmethod
  def get_urn() -> ControlMessageURN:
    raise NotImplementedError("Subclasses must implement get_urn method")


class AKControlMessage(ControlMessage, ABC):
  @staticmethod
  @abstractmethod
  def get_urn() -> ControlMessageURN:
    raise NotImplementedError("Subclasses must implement get_urn method")

  @staticmethod
  @abstractmethod
  def write(*args: Any, **kwargs: Any) -> MessageProto:
    raise NotImplementedError("Subclasses must implement write method")


class KAControlMessage(ControlMessage, ABC):
  @staticmethod
  @abstractmethod
  def get_urn() -> ControlMessageURN:
    raise NotImplementedError("Subclasses must implement get_urn method")

  @abstractmethod
  def read(self, message_proto: MessageProto) -> None:
    raise NotImplementedError("Subclasses must implement read method")
