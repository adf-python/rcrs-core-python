from typing import override

from rcrscore.entities.area import Area
from rcrscore.urn.entity import EntityURN


class Road(Area):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.ROAD
