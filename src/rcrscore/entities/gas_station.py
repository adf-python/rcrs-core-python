from typing import override

from rcrscore.entities.building import Building
from rcrscore.urn.entity import EntityURN


class GasStation(Building):
  def __init__(self, entity_id: int):
    super().__init__(entity_id)

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.GAS_STATION

  def __str__(self) -> str:
    return f"GasStation({self.get_summary()})"
