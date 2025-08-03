from typing import override

from rcrscore.entities.road import Road
from rcrscore.urn.entity import EntityURN


class Hydrant(Road):
  def __init__(self, entity_id: int):
    super().__init__(entity_id)

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.HYDRANT

  def __str__(self) -> str:
    return f"Hydrant(id={self.get_entity_id()}, x={self.get_x()}, y={self.get_y()})"
