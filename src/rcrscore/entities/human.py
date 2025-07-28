from __future__ import annotations

from abc import ABC, abstractmethod
from typing import override

from rcrs_core.connection import URN
from rcrscore.entities.entity import Entity
from rcrscore.entities.entity_id import EntityID
from rcrscore.properties.entity_id_property import EntityIDProperty
from rcrscore.properties.int_list_property import IntListProperty
from rcrscore.properties.int_property import IntProperty
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class Human(Entity, ABC):
  def __init__(self, entity_id: int):
    super().__init__(entity_id)
    self.travel_distance: IntProperty = IntProperty(PropertyURN.TRAVEL_DISTANCE)
    self.position: EntityIDProperty = EntityIDProperty(PropertyURN.POSITION)
    self.position_history: IntListProperty = IntListProperty(
      PropertyURN.POSITION_HISTORY
    )
    self.direction: IntProperty = IntProperty(PropertyURN.DIRECTION)
    self.stamina: IntProperty = IntProperty(PropertyURN.STAMINA)
    self.hp: IntProperty = IntProperty(PropertyURN.HP)
    self.damage: IntProperty = IntProperty(PropertyURN.DAMAGE)
    self.buriedness: IntProperty = IntProperty(PropertyURN.BURIEDNESS)

    self.register_properties(
      [
        self.travel_distance,
        self.position,
        self.position_history,
        self.direction,
        self.stamina,
        self.hp,
        self.damage,
        self.buriedness,
      ]
    )

  @override
  def set_from_properties(self, properties) -> None:
    super().set_from_properties(properties)
    for key, values in properties.items():
      if key == URN.Property.POSITION:
        self.position.set_value(EntityID(values))
      elif key == URN.Property.POSITION_HISTORY:
        self.position_history.set_value(values)
      elif key == URN.Property.DIRECTION:
        self.direction.set_value(values)
      elif key == URN.Property.STAMINA:
        self.stamina.set_value(values)
      elif key == URN.Property.HP:
        self.hp.set_value(values)
      elif key == URN.Property.DAMAGE:
        self.damage.set_value(values)
      elif key == URN.Property.BURIEDNESS:
        self.buriedness.set_value(values)
      elif key == URN.Property.TRAVEL_DISTANCE:
        self.travel_distance.set_value(values)

  @abstractmethod
  def get_urn(self) -> EntityURN:
    raise NotImplementedError("Subclasses must implement get_urn method")

  def get_travel_distance(self) -> IntProperty:
    return self.travel_distance

  def get_position(self) -> EntityIDProperty:
    return self.position

  def get_position_history(self) -> IntListProperty:
    return self.position_history

  def get_direction(self) -> IntProperty:
    return self.direction

  def get_stamina(self) -> IntProperty:
    return self.stamina

  def get_hp(self) -> IntProperty:
    return self.hp

  def get_damage(self) -> IntProperty:
    return self.damage

  def get_buriedness(self) -> IntProperty:
    return self.buriedness
