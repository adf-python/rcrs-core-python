from rcrscore.entities.entity_id import EntityID
from rcrscore.messages.message import KAControlMessage
from rcrscore.properties.standard_property_factory import StandardPropertyFactory
from rcrscore.proto.RCRSProto_pb2 import MessageListProto, MessageProto
from rcrscore.urn.component_control_message import ComponentControlMessageURN
from rcrscore.urn.control_message import ControlMessageURN
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN
from rcrscore.worldmodel.change_set import ChangeSet


class KASense(KAControlMessage):
  def __init__(self, message_proto: MessageProto) -> None:
    self.change_set: ChangeSet = ChangeSet()
    self.read(message_proto)

  def read(self, message_proto: MessageProto) -> None:
    self.agent_id: EntityID = EntityID(
      message_proto.components[ComponentControlMessageURN.AgentID].entityID
    )
    self.time: int = message_proto.components[ComponentControlMessageURN.Time].intValue
    self.hear: MessageListProto = message_proto.components[
      ComponentControlMessageURN.Hearing
    ].commandList
    changes = message_proto.components[ComponentControlMessageURN.Updates].changeSet
    for change in changes.changes:
      entity_id = EntityID(change.entityID)
      entity_urn = EntityURN(change.urn)
      for p in change.properties:
        property_urn = PropertyURN(p.urn)
        property = StandardPropertyFactory.make_property(property_urn)
        value = getattr(p, p.WhichOneof("value")) if p.defined else None
        if property is not None and value is not None:
          property.set_value(value)
          self.change_set.add_changed(entity_id, entity_urn, property)

    for entity_id in changes.deletes:
      self.change_set.add_deleted(EntityID(entity_id))

  def get_urn(self) -> ControlMessageURN:
    return ControlMessageURN.KA_SENSE
