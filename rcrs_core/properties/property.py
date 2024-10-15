from abc import abstractmethod
from typing import Generic, TypeVar

from rcrs_core.connection import URN

T = TypeVar("T")


class Property(Generic[T]):
    def __init__(self, _urn: URN.Property) -> None:
        self.urn: URN.Property = _urn
        self.defined: bool = False
        self.value: T

    @abstractmethod
    def copy(self) -> "Property[T]":
        pass

    @abstractmethod
    def take_value(self, _property: "Property[T]") -> None:
        pass

    def get_urn(self) -> URN.Property:
        return self.urn

    def get_value(self) -> T:
        return self.value

    def set_value(self, _value: T) -> None:
        self.value = _value

    def to_string(self) -> None:
        print("property = ", self.urn, self.value)
