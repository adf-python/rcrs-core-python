from logging import Logger

from rcrscore.agents.agent import Agent
from rcrscore.logger.logger import get_logger
from rcrscore.proto.RCRSProto_pb2 import MessageListProto
from rcrscore.urn.entity import EntityURN
from rcrscore.worldmodel.change_set import ChangeSet


class PoliceOfficeAgent(Agent):
  def __init__(self, precompute_flag: bool = False):
    super().__init__(precompute_flag)

  def precompute(self) -> None:
    return

  def think(self, time: int, change_set: ChangeSet, hear: MessageListProto) -> None:
    return

  def post_connect(self) -> None:
    return

  def get_name(self) -> str:
    return "PoliceOfficeAgent"

  def get_logger(self) -> Logger:
    if not self.logger:
      self.logger = get_logger(self.get_name(), self.get_entity_id().get_value())
    return self.logger

  def get_urn(self) -> EntityURN:
    return EntityURN.POLICE_OFFICE
