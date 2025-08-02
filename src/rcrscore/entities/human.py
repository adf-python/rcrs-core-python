from __future__ import annotations

from abc import ABC, abstractmethod
from typing import override

from rcrscore.entities.entity import Entity
from rcrscore.entities.entity_id import EntityID
from rcrscore.properties.entity_id_property import EntityIDProperty
from rcrscore.properties.int_list_property import IntListProperty
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class Human(Entity, ABC):
  def __init__(self, entity_id: int):
    super().__init__(entity_id)
    self._travel_distance: IntProperty = IntProperty(PropertyURN.TRAVEL_DISTANCE)
    self._position: EntityIDProperty = EntityIDProperty(PropertyURN.POSITION)
    self._position_history: IntListProperty = IntListProperty(
      PropertyURN.POSITION_HISTORY
    )
    self._direction: IntProperty = IntProperty(PropertyURN.DIRECTION)
    self._stamina: IntProperty = IntProperty(PropertyURN.STAMINA)
    self._hp: IntProperty = IntProperty(PropertyURN.HP)
    self._damage: IntProperty = IntProperty(PropertyURN.DAMAGE)
    self._buriedness: IntProperty = IntProperty(PropertyURN.BURIEDNESS)

    self.register_properties(
      [
        self._travel_distance,
        self._position,
        self._position_history,
        self._direction,
        self._stamina,
        self._hp,
        self._damage,
        self._buriedness,
      ]
    )

  @override
  def set_from_properties(self, properties: dict[PropertyURN, Property]) -> None:
    super().set_from_properties(properties)
    for key, values in properties.items():
      if key == PropertyURN.POSITION:
        self._position.set_value(values.get_value())
      elif key == PropertyURN.POSITION_HISTORY:
        self._position_history.set_value(values.get_value())
      elif key == PropertyURN.DIRECTION:
        self._direction.set_value(values.get_value())
      elif key == PropertyURN.STAMINA:
        self._stamina.set_value(values.get_value())
      elif key == PropertyURN.HP:
        self._hp.set_value(values.get_value())
      elif key == PropertyURN.DAMAGE:
        self._damage.set_value(values.get_value())
      elif key == PropertyURN.BURIEDNESS:
        self._buriedness.set_value(values.get_value())
      elif key == PropertyURN.TRAVEL_DISTANCE:
        self._travel_distance.set_value(values.get_value())

  @abstractmethod
  def get_urn(self) -> EntityURN:
    raise NotImplementedError("Subclasses must implement get_urn method")

  def get_travel_distance(self) -> int | None:
    return self._travel_distance.get_value()

  def get_travel_distance_property(self) -> IntProperty:
    return self._travel_distance

  def get_position(self) -> EntityID | None:
    return self._position.get_value()

  def get_position_property(self) -> EntityIDProperty:
    return self._position

  def get_position_history(self) -> list[int] | None:
    return self._position_history.get_value()

  def get_position_history_property(self) -> IntListProperty:
    return self._position_history

  def get_direction(self) -> int | None:
    return self._direction.get_value()

  def get_direction_property(self) -> IntProperty:
    return self._direction

  def get_stamina(self) -> int | None:
    return self._stamina.get_value()

  def get_stamina_property(self) -> IntProperty:
    return self._stamina

  def get_hp(self) -> int | None:
    return self._hp.get_value()

  def get_hp_property(self) -> IntProperty:
    return self._hp

  def get_damage(self) -> int | None:
    return self._damage.get_value()

  def get_damage_property(self) -> IntProperty:
    return self._damage

  def get_buriedness(self) -> int | None:
    return self._buriedness.get_value()

  def get_buriedness_property(self) -> IntProperty:
    return self._buriedness
