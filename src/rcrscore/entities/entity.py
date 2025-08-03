from abc import ABC, abstractmethod

from rcrscore.entities.entity_id import EntityID
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class Entity(ABC):
  def __init__(self, entity_id: int) -> None:
    self._entity_id: EntityID = EntityID(entity_id)
    self._x: IntProperty = IntProperty(PropertyURN.X)
    self._y: IntProperty = IntProperty(PropertyURN.Y)
    self._properties: dict[PropertyURN, Property] = {}

    self.register_properties([self._x, self._y])

  def set_from_properties(self, properties: dict[PropertyURN, Property]) -> None:
    for key, values in properties.items():
      if key == PropertyURN.X:
        self._x.set_value(values.get_value())
      elif key == PropertyURN.Y:
        self._y.set_value(values.get_value())

  def register_properties(self, properties: list[Property]) -> None:
    for property in properties:
      self._properties[property.get_urn()] = property

  @abstractmethod
  def get_urn(self) -> EntityURN:
    raise NotImplementedError("Subclasses must implement get_urn method")

  def get_entity_id(self) -> EntityID:
    return self._entity_id

  def get_properties(self) -> dict[PropertyURN, Property]:
    return self._properties

  def get_property(self, property_urn: PropertyURN) -> Property | None:
    return self._properties.get(property_urn)

  def get_location(self) -> tuple[int | None, int | None]:
    return self._x.get_value(), self._y.get_value()

  def get_x(self) -> int | None:
    return self._x.get_value()

  def get_x_property(self) -> IntProperty:
    return self._x

  def get_y(self) -> int | None:
    return self._y.get_value()

  def get_y_property(self) -> IntProperty:
    return self._y

  def set_x(self, x: int | None) -> None:
    self._x.set_value(x)

  def set_y(self, y: int | None) -> None:
    self._y.set_value(y)

  def get_summary(self) -> str:
    return f"id={self.get_entity_id()}, x={self.get_x()}, y={self.get_y()}"

  def __hash__(self) -> int:
    return self._entity_id.get_value()

  def __str__(self) -> str:
    return f"Entity({self.get_summary()})"
