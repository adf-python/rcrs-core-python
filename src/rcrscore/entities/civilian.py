from typing import override

from rcrscore.entities.human import Human
from rcrscore.urn.entity import EntityURN


class Civilian(Human):
  def __init__(self, entity_id: int):
    super().__init__(entity_id)

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.CIVILIAN
