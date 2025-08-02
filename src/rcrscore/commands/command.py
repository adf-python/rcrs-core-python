from abc import ABC, abstractmethod

from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.command import CommandURN


class Command(ABC):
  @staticmethod
  @abstractmethod
  def get_urn() -> CommandURN:
    raise NotImplementedError("get_urn method must be implemented by subclass")

  @abstractmethod
  def to_message_proto(self) -> MessageProto:
    raise NotImplementedError("to_message_proto method must be implemented by subclass")
