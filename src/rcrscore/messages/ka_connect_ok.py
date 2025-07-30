from rcrscore.config.config import Config
from rcrscore.entities.standard_entity_factory import StandardEntityFactory
from rcrscore.messages.message import KAControlMessage
from rcrscore.proto.RCRSProto_pb2 import MessageProto
from rcrscore.urn.component_control_message import ComponentControlMessageURN
from rcrscore.urn.control_message import ControlMessageURN
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class KAConnectOK(KAControlMessage):
  def __init__(self, message_proto: MessageProto) -> None:
    self.config = Config()
    self.world = []
    self.read(message_proto)

  def read(self, message_proto: MessageProto) -> None:
    entities = message_proto.components[
      ComponentControlMessageURN.Entities
    ].entityList.entities
    self.request_id = message_proto.components[
      ComponentControlMessageURN.RequestID
    ].intValue
    self.agent_id = message_proto.components[
      ComponentControlMessageURN.AgentID
    ].entityID
    config = message_proto.components[ComponentControlMessageURN.AgentConfig].config

    for e in entities:
      entity = StandardEntityFactory.make_entity(EntityURN(e.urn), e.entityID)
      properties = {}
      for property in e.properties:
        value = (
          getattr(property, property.WhichOneof("value")) if property.defined else None
        )
        properties[PropertyURN(property.urn)] = value
      entity.set_from_properties(properties)
      self.world.append(entity)

    for key, value in config.data.items():
      self.config.set_value(key, value)

  @staticmethod
  def get_urn() -> ControlMessageURN:
    return ControlMessageURN.KA_CONNECT_OK
