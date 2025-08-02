from typing import override

from rcrscore.entities.entity import Entity
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class World(Entity):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)
    self.start_time: IntProperty = IntProperty(PropertyURN.START_TIME)
    self.longitude: IntProperty = IntProperty(PropertyURN.LONGITUDE)
    self.latitude: IntProperty = IntProperty(PropertyURN.LATITUDE)
    self.wind_force: IntProperty = IntProperty(PropertyURN.WIND_FORCE)
    self.wind_direction: IntProperty = IntProperty(PropertyURN.WIND_DIRECTION)

    self.register_properties(
      [
        self.start_time,
        self.longitude,
        self.latitude,
        self.wind_force,
        self.wind_direction,
      ]
    )

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.WORLD

  @override
  def set_from_properties(self, properties: dict[PropertyURN, Property]) -> None:
    super().set_from_properties(properties)
    for key, values in properties.items():
      if key == PropertyURN.START_TIME:
        self.start_time.set_value(values.get_value())
      elif key == PropertyURN.LONGITUDE:
        self.longitude.set_value(values.get_value())
      elif key == PropertyURN.LATITUDE:
        self.latitude.set_value(values.get_value())
      elif key == PropertyURN.WIND_FORCE:
        self.wind_force.set_value(values.get_value())
      elif key == PropertyURN.WIND_DIRECTION:
        self.wind_direction.set_value(values.get_value())
