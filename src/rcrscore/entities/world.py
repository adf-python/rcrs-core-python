from typing import override

from rcrscore.entities.entity import Entity
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class World(Entity):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)
    self._start_time: IntProperty = IntProperty(PropertyURN.START_TIME)
    self._longitude: IntProperty = IntProperty(PropertyURN.LONGITUDE)
    self._latitude: IntProperty = IntProperty(PropertyURN.LATITUDE)
    self._wind_force: IntProperty = IntProperty(PropertyURN.WIND_FORCE)
    self._wind_direction: IntProperty = IntProperty(PropertyURN.WIND_DIRECTION)

    self.register_properties(
      [
        self._start_time,
        self._longitude,
        self._latitude,
        self._wind_force,
        self._wind_direction,
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
        self._start_time.set_value(values.get_value())
      elif key == PropertyURN.LONGITUDE:
        self._longitude.set_value(values.get_value())
      elif key == PropertyURN.LATITUDE:
        self._latitude.set_value(values.get_value())
      elif key == PropertyURN.WIND_FORCE:
        self._wind_force.set_value(values.get_value())
      elif key == PropertyURN.WIND_DIRECTION:
        self._wind_direction.set_value(values.get_value())

  def get_start_time(self) -> int | None:
    return self._start_time.get_value()

  def get_start_time_property(self) -> IntProperty:
    return self._start_time

  def get_longitude(self) -> int | None:
    return self._longitude.get_value()

  def get_longitude_property(self) -> IntProperty:
    return self._longitude

  def get_latitude(self) -> int | None:
    return self._latitude.get_value()

  def get_latitude_property(self) -> IntProperty:
    return self._latitude

  def get_wind_force(self) -> int | None:
    return self._wind_force.get_value()

  def get_wind_force_property(self) -> IntProperty:
    return self._wind_force

  def get_wind_direction(self) -> int | None:
    return self._wind_direction.get_value()

  def get_wind_direction_property(self) -> IntProperty:
    return self._wind_direction
