from typing import override

from rcrscore.entities.building import Building
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class Refuge(Building):
  def __init__(self, entity_id: int):
    super().__init__(entity_id)
    self._bed_capacity = IntProperty(PropertyURN.BEDCAPACITY)
    self._occupied_beds = IntProperty(PropertyURN.OCCUPIEDBEDS)
    self._refill_capacity = IntProperty(PropertyURN.REFILLCAPACITY)
    self._waiting_list_size = IntProperty(PropertyURN.WAITINGLISTSIZE)
    self.register_properties(
      [
        self._bed_capacity,
        self._occupied_beds,
        self._refill_capacity,
        self._waiting_list_size,
      ]
    )

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.REFUGE

  @override
  def set_from_properties(self, properties: dict[PropertyURN, Property]) -> None:
    super().set_from_properties(properties)
    for key, values in properties.items():
      if key == PropertyURN.BEDCAPACITY:
        self._bed_capacity.set_value(values.get_value())
      elif key == PropertyURN.OCCUPIEDBEDS:
        self._occupied_beds.set_value(values.get_value())
      elif key == PropertyURN.REFILLCAPACITY:
        self._refill_capacity.set_value(values.get_value())
      elif key == PropertyURN.WAITINGLISTSIZE:
        self._waiting_list_size.set_value(values.get_value())

  def get_bed_capacity(self) -> int | None:
    return self._bed_capacity.get_value()

  def get_bed_capacity_property(self) -> IntProperty:
    return self._bed_capacity

  def get_occupied_beds(self) -> int | None:
    return self._occupied_beds.get_value()

  def get_occupied_beds_property(self) -> IntProperty:
    return self._occupied_beds

  def get_refill_capacity(self) -> int | None:
    return self._refill_capacity.get_value()

  def get_refill_capacity_property(self) -> IntProperty:
    return self._refill_capacity

  def get_waiting_list_size(self) -> int | None:
    return self._waiting_list_size.get_value()

  def get_waiting_list_size_property(self) -> IntProperty:
    return self._waiting_list_size

  def __str__(self) -> str:
    return (
      f"Refuge(id={self.get_entity_id()}, "
      f"bed_capacity={self._bed_capacity.get_value()}, "
      f"occupied_beds={self._occupied_beds.get_value()}, "
      f"refill_capacity={self._refill_capacity.get_value()}, "
      f"waiting_list_size={self._waiting_list_size.get_value()})"
    )

  def __repr__(self) -> str:
    return (
      f"Refuge(entity_id={self.get_entity_id()}, "
      f"bed_capacity={self._bed_capacity}, "
      f"occupied_beds={self._occupied_beds}, "
      f"refill_capacity={self._refill_capacity}, "
      f"waiting_list_size={self._waiting_list_size}, "
      f"properties={self.get_properties()})"
    )
