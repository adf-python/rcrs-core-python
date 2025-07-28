from typing import override

from rcrscore.entities.road import Road
from rcrscore.urn.entity import EntityURN


class Hydrant(Road):
  def __init__(self, entity_id: int):
    super().__init__(entity_id)

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.HYDRANT
