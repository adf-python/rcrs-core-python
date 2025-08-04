from typing import override

from rcrscore.entities.entity import Entity
from rcrscore.entities.entity_id import EntityID
from rcrscore.properties.entity_id_property import EntityIDProperty
from rcrscore.properties.int_list_property import IntListProperty
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class Blockade(Entity):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)
    self._position: EntityIDProperty = EntityIDProperty(PropertyURN.POSITION)
    self._apexes: IntListProperty = IntListProperty(PropertyURN.APEXES)
    self._repair_cost: IntProperty = IntProperty(PropertyURN.REPAIR_COST)

    self.register_properties([self._position, self._apexes, self._repair_cost])

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.BLOCKADE

  @override
  def set_from_properties(self, properties: dict[PropertyURN, Property]) -> None:
    super().set_from_properties(properties)
    for key, values in properties.items():
      if key == PropertyURN.POSITION:
        self._position.set_value(values.get_value())
      elif key == PropertyURN.APEXES:
        self._apexes.set_value(values.get_value())
      elif key == PropertyURN.REPAIR_COST:
        self._repair_cost.set_value(values.get_value())

  def get_position(self) -> EntityID | None:
    return self._position.get_value()

  def get_position_property(self) -> EntityIDProperty:
    return self._position

  def get_apexes(self) -> list[int] | None:
    return self._apexes.get_value()

  def get_apexes_property(self) -> IntListProperty:
    return self._apexes

  def get_repair_cost(self) -> int | None:
    return self._repair_cost.get_value()

  def get_repair_cost_property(self) -> IntProperty:
    return self._repair_cost

  def set_position(self, position: EntityID | None) -> None:
    self._position.set_value(position)

  def set_apexes(self, apexes: list[int] | None) -> None:
    self._apexes.set_value(apexes)

  def set_repair_cost(self, repair_cost: int | None) -> None:
    self._repair_cost.set_value(repair_cost)

  def __str__(self) -> str:
    return (
      f"Blockade(id={self.get_entity_id()}, x={self.get_x()}, y={self.get_y()}, "
      f"position={self._position.get_value()}, "
      f"repair_cost={self._repair_cost.get_value()})"
    )
