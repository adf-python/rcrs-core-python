import sys
from abc import ABC, abstractmethod
from logging import Logger
from typing import Callable

from rcrscore.commands.ak_clear import AKClear
from rcrscore.commands.ak_clear_area import AKClearArea
from rcrscore.commands.ak_extinguish import AKExtinguish
from rcrscore.commands.ak_load import AKLoad
from rcrscore.commands.ak_move import AKMove
from rcrscore.commands.ak_rescue import AKRescue
from rcrscore.commands.ak_rest import AKRest
from rcrscore.commands.ak_say import AKSay
from rcrscore.commands.ak_speak import AKSpeak
from rcrscore.commands.ak_subscribe import AKSubscribe
from rcrscore.commands.ak_tell import AKTell
from rcrscore.commands.ak_unload import AKUnload
from rcrscore.config.config import Config
from rcrscore.entities.entity import Entity
from rcrscore.entities.entity_id import EntityID
from rcrscore.entities.human import Human
from rcrscore.logger.logger import get_logger
from rcrscore.messages.ak_acknowledge import AKAcknowledge
from rcrscore.messages.ak_connect import AKConnect
from rcrscore.messages.control_message_factory import ControlMessageFactory
from rcrscore.messages.ka_connect_error import KAConnectError
from rcrscore.messages.ka_connect_ok import KAConnectOK
from rcrscore.messages.ka_sense import KASense
from rcrscore.proto.RCRSProto_pb2 import MessageListProto, MessageProto
from rcrscore.urn.entity import EntityURN
from rcrscore.worldmodel.change_set import ChangeSet
from rcrscore.worldmodel.world_model import WorldModel


class Agent(ABC):
  def __init__(self, precompute_flag: bool = False):
    self.precompute_flag: bool = precompute_flag
    self.connect_request_id = None
    self.world_model: WorldModel = WorldModel()
    self.config: Config = Config()
    self.agent_id: EntityID = EntityID(-1)

  @abstractmethod
  def precompute(self) -> None:
    pass

  @abstractmethod
  def think(self, time: int, change_set: ChangeSet, hear: MessageListProto) -> None:
    pass

  @abstractmethod
  def post_connect(self) -> None:
    pass

  @abstractmethod
  def get_name(self) -> str:
    raise NotImplementedError("get_name method must be implemented by subclass")

  @abstractmethod
  def get_urn(self) -> EntityURN:
    raise NotImplementedError("get_urn method must be implemented by subclass")

  def get_logger(self) -> Logger:
    if self.logger is None:
      self.logger: Logger = get_logger(
        self.get_name(), self.get_entity_id().get_value()
      )
    return self.logger

  def get_entity_id(self) -> EntityID:
    return self.agent_id

  def me(self) -> Human | None:
    human = self.world_model.get_entity(self.agent_id)
    if not isinstance(human, Human):
      return None

    return human

  def location(self) -> Entity | None:
    me = self.me()
    if not me:
      return None

    location_entity_id = me.get_position().get_value()
    if location_entity_id is None:
      return None

    return self.world_model.get_entity(location_entity_id)

  def message_handlers(self, msg: MessageProto) -> None:
    c_msg = ControlMessageFactory.make_message(msg)
    match c_msg:
      case KASense():
        self.handle_sense(c_msg)
      case KAConnectOK():
        self.handle_connect_ok(c_msg)
      case KAConnectError():
        self.handle_connect_error(c_msg)
      case _:
        self.get_logger().warning(
          f"Unknown control message: {c_msg.__class__.__name__}"
        )

  def handle_sense(self, msg: KASense) -> None:
    entity_id: EntityID = msg.agent_id
    time: int = msg.time
    change_set: ChangeSet = msg.change_set
    hear: MessageListProto = msg.hear

    if entity_id != self.get_entity_id():
      self.get_logger().warning("agent received a message which not belongs to him")
      return

    self.world_model.merge(change_set)
    self.think(time, change_set, hear)

  def handle_connect_ok(self, msg: KAConnectOK) -> None:
    self.agent_id = EntityID(msg.agent_id)
    self.config = msg.config
    self.world_model.add_entities(msg.world)
    self.send_acknowledge(msg.request_id)
    self.post_connect()
    if self.precompute_flag:
      self.get_logger().info("self.precompute_flag: {0}".format(self.precompute_flag))
      self.precompute()

  def handle_connect_error(self, msg: KAConnectError) -> None:
    self.get_logger().warning("failed {0} : {1}".format(msg.request_id, msg.reason))
    sys.exit(1)

  def set_send_msg(self, connection_send_func: Callable[[MessageProto], None]) -> None:
    self.send_msg = connection_send_func

  def send_connect(self, request_id: int) -> None:
    cmd = AKConnect()
    self.send_msg(cmd.write(request_id, self.get_name(), [self.get_urn()]))

  def send_acknowledge(self, request_id: int) -> None:
    ak_ack = AKAcknowledge()
    self.send_msg(ak_ack.write(request_id, self.agent_id))

  def send_move(
    self, time: int, path: list[EntityID], x: int = -1, y: int = -1
  ) -> None:
    cmd = AKMove(self.get_entity_id(), time, path, x, y)
    self.send_msg(cmd.to_message_proto())

  def send_clear(self, time: int, target: EntityID) -> None:
    cmd = AKClear(self.get_entity_id(), time, target)
    self.send_msg(cmd.to_message_proto())

  def send_clear_area(self, time: int, x: int = -1, y: int = -1) -> None:
    cmd = AKClearArea(self.get_entity_id(), time, x, y)
    self.send_msg(cmd.to_message_proto())

  def send_extinguish(self, time: int, target: EntityID) -> None:
    cmd = AKExtinguish(self.get_entity_id(), time, target)
    self.send_msg(cmd.to_message_proto())

  def send_load(self, time: int, target: EntityID) -> None:
    cmd = AKLoad(self.get_entity_id(), time, target)
    self.send_msg(cmd.to_message_proto())

  def send_unload(self, time: int) -> None:
    cmd = AKUnload(self.get_entity_id(), time)
    self.send_msg(cmd.to_message_proto())

  def send_rescue(self, time: int, target: EntityID) -> None:
    cmd = AKRescue(self.get_entity_id(), time, target)
    self.send_msg(cmd.to_message_proto())

  def send_rest(self, time: int) -> None:
    cmd = AKRest(self.get_entity_id(), time)
    self.send_msg(cmd.to_message_proto())

  def send_say(self, time_step: int, message: bytes) -> None:
    cmd = AKSay(self.get_entity_id(), time_step, message)
    self.send_msg(cmd.to_message_proto())

  def send_speak(self, time_step: int, message: bytes, channel: int) -> None:
    cmd = AKSpeak(self.get_entity_id(), time_step, message, channel)
    self.send_msg(cmd.to_message_proto())

  def send_subscribe(self, time: int, channels: list[int]) -> None:
    cmd = AKSubscribe(self.get_entity_id(), time, channels)
    self.send_msg(cmd.to_message_proto())

  def send_tell(self, time: int, message: bytes) -> None:
    cmd = AKTell(self.get_entity_id(), time, message)
    self.send_msg(cmd.to_message_proto())
