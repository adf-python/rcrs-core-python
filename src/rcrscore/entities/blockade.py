from typing import override

from rcrscore.entities.entity import Entity
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

  def get_position(self) -> EntityIDProperty:
    return self._position

  def get_apexes(self) -> IntListProperty:
    return self._apexes

  def get_repair_cost(self) -> IntProperty:
    return self._repair_cost
