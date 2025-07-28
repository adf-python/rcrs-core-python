from typing import override

from rcrscore.entities.building import Building
from rcrscore.properties.int_property import IntProperty
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class Refuge(Building):
  def __init__(self, entity_id: int):
    super().__init__(entity_id)
    self.bed_capacity = IntProperty(PropertyURN.BEDCAPACITY)
    self.occupied_beds = IntProperty(PropertyURN.OCCUPIEDBEDS)
    self.refill_capacity = IntProperty(PropertyURN.REFILLCAPACITY)
    self.waiting_list_size = IntProperty(PropertyURN.WAITINGLISTSIZE)
    self.register_properties(
      [
        self.bed_capacity,
        self.occupied_beds,
        self.refill_capacity,
        self.waiting_list_size,
      ]
    )

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.REFUGE

  @override
  def set_from_properties(self, properties) -> None:
    super().set_from_properties(properties)
    for key, values in properties.items():
      if key == PropertyURN.BEDCAPACITY:
        self.bed_capacity.set_value(values)
      elif key == PropertyURN.OCCUPIEDBEDS:
        self.occupied_beds.set_value(values)
      elif key == PropertyURN.REFILLCAPACITY:
        self.refill_capacity.set_value(values)
      elif key == PropertyURN.WAITINGLISTSIZE:
        self.waiting_list_size.set_value(values)

  def get_bed_capacity(self) -> IntProperty:
    return self.bed_capacity

  def get_occupied_beds(self) -> IntProperty:
    return self.occupied_beds

  def get_refill_capacity(self) -> IntProperty:
    return self.refill_capacity

  def get_waiting_list_size(self) -> IntProperty:
    return self.waiting_list_size

  def __str__(self) -> str:
    return (
      f"Refuge(id={self.get_entity_id()}, "
      f"bed_capacity={self.bed_capacity.get_value()}, "
      f"occupied_beds={self.occupied_beds.get_value()}, "
      f"refill_capacity={self.refill_capacity.get_value()}, "
      f"waiting_list_size={self.waiting_list_size.get_value()})"
    )

  def __repr__(self) -> str:
    return (
      f"Refuge(entity_id={self.get_entity_id()}, "
      f"bed_capacity={self.bed_capacity}, "
      f"occupied_beds={self.occupied_beds}, "
      f"refill_capacity={self.refill_capacity}, "
      f"waiting_list_size={self.waiting_list_size}, "
      f"properties={self.get_properties()})"
    )
