from rcrscore.agents.agent import Agent
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

  def get_urn(self) -> EntityURN:
    return EntityURN.POLICE_OFFICE
