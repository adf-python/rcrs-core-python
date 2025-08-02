from typing import override

from rcrscore.entities.human import Human
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class FireBrigade(Human):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)
    self.water = IntProperty(PropertyURN.WATER_QUANTITY)

    self.register_properties([self.water])

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.FIRE_BRIGADE

  @override
  def set_from_properties(self, properties: dict[PropertyURN, Property]) -> None:
    super().set_from_properties(properties)
    for key, values in properties.items():
      if key == PropertyURN.WATER_QUANTITY:
        self.water.set_value(values.get_value())

  def get_water(self) -> IntProperty:
    return self.water
