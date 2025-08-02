from typing import override

from rcrscore.entities.area import Area
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class Building(Area):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)
    self.floors: IntProperty = IntProperty(PropertyURN.FLOORS)
    self.ignition: IntProperty = IntProperty(PropertyURN.IGNITION)
    self.fieryness: IntProperty = IntProperty(PropertyURN.FIERYNESS)
    self.brokenness: IntProperty = IntProperty(PropertyURN.BROKENNESS)
    self.building_code: IntProperty = IntProperty(PropertyURN.BUILDING_CODE)
    self.attributes: IntProperty = IntProperty(PropertyURN.BUILDING_ATTRIBUTES)
    self.ground_area: IntProperty = IntProperty(PropertyURN.BUILDING_AREA_GROUND)
    self.total_area: IntProperty = IntProperty(PropertyURN.BUILDING_AREA_TOTAL)
    self.temperature: IntProperty = IntProperty(PropertyURN.TEMPERATURE)
    self.importance: IntProperty = IntProperty(PropertyURN.IMPORTANCE)
    self.capacity: IntProperty = IntProperty(PropertyURN.CAPACITY)

    self.register_properties(
      [
        self.floors,
        self.ignition,
        self.fieryness,
        self.brokenness,
        self.attributes,
        self.ground_area,
        self.total_area,
        self.capacity,
        self.temperature,
        self.importance,
        self.building_code,
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
        self.floors.set_value(values.get_value())
      elif key == PropertyURN.IGNITION:
        self.ignition.set_value(values.get_value())
      elif key == PropertyURN.FIERYNESS:
        self.fieryness.set_value(values.get_value())
      elif key == PropertyURN.BROKENNESS:
        self.brokenness.set_value(values.get_value())
      elif key == PropertyURN.BUILDING_CODE:
        self.building_code.set_value(values.get_value())
      elif key == PropertyURN.BUILDING_ATTRIBUTES:
        self.attributes.set_value(values.get_value())
      elif key == PropertyURN.BUILDING_AREA_GROUND:
        self.ground_area.set_value(values.get_value())
      elif key == PropertyURN.BUILDING_AREA_TOTAL:
        self.total_area.set_value(values.get_value())
      elif key == PropertyURN.TEMPERATURE:
        self.temperature.set_value(values.get_value())
      elif key == PropertyURN.IMPORTANCE:
        self.importance.set_value(values.get_value())

  def is_fiery(self) -> bool:
    fieryness_value = self.fieryness.get_value()
    # HEATING:1 BURNING:2 INFERNO:3
    if fieryness_value == 1 or fieryness_value == 2 or fieryness_value == 3:
      return True
    return False

  def get_floors(self) -> IntProperty:
    return self.floors

  def get_ignition(self) -> IntProperty:
    return self.ignition

  def get_fieryness(self) -> IntProperty:
    return self.fieryness

  def get_brokenness(self) -> IntProperty:
    return self.brokenness

  def get_building_code(self) -> IntProperty:
    return self.building_code

  def get_attributes(self) -> IntProperty:
    return self.attributes

  def get_ground_area(self) -> IntProperty:
    return self.ground_area

  def get_total_area(self) -> IntProperty:
    return self.total_area

  def get_temperature(self) -> IntProperty:
    return self.temperature

  def get_importance(self) -> IntProperty:
    return self.importance

  def get_capacity(self) -> IntProperty:
    return self.capacity

  def __str__(self) -> str:
    return (
      f"Building(id={self.get_entity_id()}, x={self.get_x().get_value()}, "
      f"y={self.get_y().get_value()}, floors={self.floors.get_value()}, "
      f"ignition={self.ignition.get_value()}, fieryness={self.fieryness.get_value()}, "
      f"brokenness={self.brokenness.get_value()}, building_code={self.building_code.get_value()}, "
      f"attributes={self.attributes.get_value()}, ground_area={self.ground_area.get_value()}, "
      f"total_area={self.total_area.get_value()}, temperature={self.temperature.get_value()}, "
      f"importance={self.importance.get_value()})"
    )

  def __repr__(self) -> str:
    return (
      f"Building(entity_id={self.get_entity_id()}, x={self.get_x()}, y={self.get_y()}, "
      f"floors={self.floors}, ignition={self.ignition}, fieryness={self.fieryness}, "
      f"brokenness={self.brokenness}, building_code={self.building_code}, "
      f"attributes={self.attributes}, ground_area={self.ground_area}, "
      f"total_area={self.total_area}, temperature={self.temperature}, "
      f"importance={self.importance})"
    )
