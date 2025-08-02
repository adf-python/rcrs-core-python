from typing import override

from rcrscore.entities.area import Area
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class Building(Area):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)
    self._floors: IntProperty = IntProperty(PropertyURN.FLOORS)
    self._ignition: IntProperty = IntProperty(PropertyURN.IGNITION)
    self._fieryness: IntProperty = IntProperty(PropertyURN.FIERYNESS)
    self._brokenness: IntProperty = IntProperty(PropertyURN.BROKENNESS)
    self._building_code: IntProperty = IntProperty(PropertyURN.BUILDING_CODE)
    self._attributes: IntProperty = IntProperty(PropertyURN.BUILDING_ATTRIBUTES)
    self._ground_area: IntProperty = IntProperty(PropertyURN.BUILDING_AREA_GROUND)
    self._total_area: IntProperty = IntProperty(PropertyURN.BUILDING_AREA_TOTAL)
    self._temperature: IntProperty = IntProperty(PropertyURN.TEMPERATURE)
    self._importance: IntProperty = IntProperty(PropertyURN.IMPORTANCE)
    self._capacity: IntProperty = IntProperty(PropertyURN.CAPACITY)

    self.register_properties(
      [
        self._floors,
        self._ignition,
        self._fieryness,
        self._brokenness,
        self._attributes,
        self._ground_area,
        self._total_area,
        self._capacity,
        self._temperature,
        self._importance,
        self._building_code,
      ]
    )

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.BUILDING

  @override
  def set_from_properties(self, properties: dict[PropertyURN, Property]) -> None:
    super().set_from_properties(properties)
    for key, values in properties.items():
      if key == PropertyURN.FLOORS:
        self._floors.set_value(values.get_value())
      elif key == PropertyURN.IGNITION:
        self._ignition.set_value(values.get_value())
      elif key == PropertyURN.FIERYNESS:
        self._fieryness.set_value(values.get_value())
      elif key == PropertyURN.BROKENNESS:
        self._brokenness.set_value(values.get_value())
      elif key == PropertyURN.BUILDING_CODE:
        self._building_code.set_value(values.get_value())
      elif key == PropertyURN.BUILDING_ATTRIBUTES:
        self._attributes.set_value(values.get_value())
      elif key == PropertyURN.BUILDING_AREA_GROUND:
        self._ground_area.set_value(values.get_value())
      elif key == PropertyURN.BUILDING_AREA_TOTAL:
        self._total_area.set_value(values.get_value())
      elif key == PropertyURN.TEMPERATURE:
        self._temperature.set_value(values.get_value())
      elif key == PropertyURN.IMPORTANCE:
        self._importance.set_value(values.get_value())

  def is_fiery(self) -> bool:
    fieryness_value = self._fieryness.get_value()
    # HEATING:1 BURNING:2 INFERNO:3
    if fieryness_value == 1 or fieryness_value == 2 or fieryness_value == 3:
      return True
    return False

  def get_floors(self) -> int | None:
    return self._floors.get_value()

  def get_floors_property(self) -> IntProperty:
    return self._floors

  def get_ignition(self) -> int | None:
    return self._ignition.get_value()

  def get_ignition_property(self) -> IntProperty:
    return self._ignition

  def get_fieryness(self) -> int | None:
    return self._fieryness.get_value()

  def get_fieryness_property(self) -> IntProperty:
    return self._fieryness

  def get_brokenness(self) -> int | None:
    return self._brokenness.get_value()

  def get_brokenness_property(self) -> IntProperty:
    return self._brokenness

  def get_building_code(self) -> int | None:
    return self._building_code.get_value()

  def get_building_code_property(self) -> IntProperty:
    return self._building_code

  def get_attributes(self) -> int | None:
    return self._attributes.get_value()

  def get_attributes_property(self) -> IntProperty:
    return self._attributes

  def get_ground_area(self) -> int | None:
    return self._ground_area.get_value()

  def get_ground_area_property(self) -> IntProperty:
    return self._ground_area

  def get_total_area(self) -> int | None:
    return self._total_area.get_value()

  def get_total_area_property(self) -> IntProperty:
    return self._total_area

  def get_temperature(self) -> int | None:
    return self._temperature.get_value()

  def get_temperature_property(self) -> IntProperty:
    return self._temperature

  def get_importance(self) -> int | None:
    return self._importance.get_value()

  def get_importance_property(self) -> IntProperty:
    return self._importance

  def get_capacity(self) -> int | None:
    return self._capacity.get_value()

  def get_capacity_property(self) -> IntProperty:
    return self._capacity

  def __str__(self) -> str:
    return (
      f"Building(id={self.get_entity_id()}, x={self.get_x()}, "
      f"y={self.get_y()}, floors={self._floors.get_value()}, "
      f"ignition={self._ignition.get_value()}, fieryness={self._fieryness.get_value()}, "
      f"brokenness={self._brokenness.get_value()}, building_code={self._building_code.get_value()}, "
      f"attributes={self._attributes.get_value()}, ground_area={self._ground_area.get_value()}, "
      f"total_area={self._total_area.get_value()}, temperature={self._temperature.get_value()}, "
      f"importance={self._importance.get_value()})"
    )

  def __repr__(self) -> str:
    return (
      f"Building(entity_id={self.get_entity_id()}, x={self.get_x()}, y={self.get_y()}, "
      f"floors={self._floors}, ignition={self._ignition}, fieryness={self._fieryness}, "
      f"brokenness={self._brokenness}, building_code={self._building_code}, "
      f"attributes={self._attributes}, ground_area={self._ground_area}, "
      f"total_area={self._total_area}, temperature={self._temperature}, "
      f"importance={self._importance})"
    )
