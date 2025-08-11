from random import Random

from rcrscore.agents.agent import Agent
from rcrscore.entities.area import Area
from rcrscore.entities.entity_id import EntityID
from rcrscore.proto.RCRSProto_pb2 import MessageListProto
from rcrscore.urn.entity import EntityURN
from rcrscore.worldmodel.change_set import ChangeSet


class FireBrigadeAgent(Agent):
  def __init__(self, precompute_flag: bool = False):
    super().__init__(precompute_flag)
    self.random = Random(0)

  def precompute(self) -> None:
    return

  def think(self, time: int, change_set: ChangeSet, hear: MessageListProto) -> None:
    next_location = self.random_walk()
    if next_location:
      self.logger.info(f"Time step: {time}, Moving to: {next_location}")
      self.send_move(time, [next_location])
    else:
      self.logger.info(f"Time step: {time}, No move, resting.")
      self.send_rest(time)

  def random_walk(self) -> EntityID | None:
    if not (location := self.location()):
      return None

    if not isinstance(location, Area):
      return None

    neighbors: set[EntityID] = location.get_neighbors()
    if not neighbors:
      return None

    return self.random.choice(list(neighbors))

  def post_connect(self) -> None:
    return

  def get_name(self) -> str:
    return "FireBrigadeAgent"

  def get_urn(self) -> EntityURN:
    return EntityURN.FIRE_BRIGADE
