from typing import override

from rcrscore.entities.human import Human
from rcrscore.urn.entity import EntityURN


class AmbulanceTeam(Human):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.AMBULANCE_TEAM

  def __str__(self) -> str:
    return f"AmbulanceTeam({self.get_summary()})"
