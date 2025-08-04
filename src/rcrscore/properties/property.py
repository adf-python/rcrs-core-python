from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from rcrscore.proto import RCRSProto_pb2
from rcrscore.urn.property import PropertyURN

T = TypeVar("T")


class Property(Generic[T], ABC):
  def __init__(self, urn: PropertyURN, value: T | None = None) -> None:
    self._urn: PropertyURN = urn
    self._value: T | None = value

  @abstractmethod
  def to_property_proto(self) -> RCRSProto_pb2.PropertyProto:
    pass

  def set_value(self, value: T | None) -> None:
    self._value = value

  def get_urn(self) -> PropertyURN:
    return self._urn

  def get_value(self) -> T | None:
    return self._value

  def __str__(self) -> str:
    return f"property = {self._urn} {self._value}"

  def __repr__(self) -> str:
    return f"Property(urn={self._urn}, value={self._value})"
