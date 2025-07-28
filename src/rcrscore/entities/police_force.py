from typing import override

from rcrscore.entities.human import Human
from rcrscore.urn.entity import EntityURN


class PoliceForce(Human):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)

  @override
  def get_urn(self) -> EntityURN:
    return EntityURN.POLICE_FORCE
