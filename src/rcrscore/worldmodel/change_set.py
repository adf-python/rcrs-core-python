from __future__ import annotations

from rcrscore.entities.entity_id import EntityID
from rcrscore.properties.property import Property
from rcrscore.proto import RCRSProto_pb2
from rcrscore.urn.entity import EntityURN
from rcrscore.urn.property import PropertyURN


class ChangeSet:
  def __init__(self, change_set: ChangeSet | None = None) -> None:
    self.changed: dict[EntityID, dict[PropertyURN, Property]] = {}
    self.deleted: set[EntityID] = set()
    self.entity_urns: dict[EntityID, EntityURN] = {}

    if change_set is not None:
      self.merge(change_set)

  def add_changed(
    self, entity_id: EntityID, entity_urn: EntityURN, property: Property
  ) -> None:
    if entity_id in self.deleted:
      return

    if not (property_dict := self.changed.get(entity_id)):
      property_dict = {}

    property_urn = property.get_urn()

    property_dict[property_urn] = property
    self.changed[entity_id] = property_dict
    self.entity_urns[entity_id] = entity_urn

  def add_deleted(self, entity_id: EntityID) -> None:
    self.deleted.add(entity_id)
    if entity_id in self.changed:
      del self.changed[entity_id]

  def get_changed_properties(self, entity_id: EntityID) -> list[Property]:
    if entity_id in self.changed:
      return list(self.changed[entity_id].values())
    return []

  def get_changed_property(
    self, entity_id: EntityID, prop_urn: PropertyURN
  ) -> Property | None:
    if entity_id in self.changed:
      property_dict = self.changed.get(entity_id)
      if property_dict is not None and len(property_dict) > 0:
        if prop_urn in property_dict:
          return property_dict[prop_urn]
    return None

  def get_changed_entities(self) -> set[EntityID]:
    return set(self.changed.keys())

  def get_deleted_entities(self) -> set[EntityID]:
    return self.deleted

  def get_entity_changes(
    self, entity_id: EntityID
  ) -> dict[PropertyURN, Property] | None:
    if entity_id in self.changed:
      return self.changed[entity_id]
    return None

  def get_entity_urn(self, entity_id: EntityID) -> EntityURN | None:
    return self.entity_urns.get(entity_id)

  def merge(self, change_set: ChangeSet) -> None:
    for entity_id in change_set.changed:
      entity_urn = change_set.get_entity_urn(entity_id)
      property_dict = change_set.get_entity_changes(entity_id)
      if entity_urn is None or property_dict is None:
        continue
      for property_urn in property_dict:
        self.add_changed(entity_id, entity_urn, property_dict[property_urn])

    for entity_id in change_set.deleted:
      self.add_deleted(entity_id)

  def to_change_set_proto(self) -> RCRSProto_pb2.ChangeSetProto:
    entity_change_proto_list = []
    change_set_proto = RCRSProto_pb2.ChangeSetProto()
    for changed_entity_id, changed_properties in self.changed.items():
      entity_change_proto = change_set_proto.EntityChangeProto()
      entity_change_proto.entityID = changed_entity_id.get_value()
      entity_change_proto.urn = self.entity_urns[changed_entity_id]
      property_proto_list = []
      for _, property_value in changed_properties.items():
        property_proto = property_value.to_property_proto()
        property_proto_list.append(property_proto)
      entity_change_proto.properties.extend(property_proto_list)
      entity_change_proto_list.append(entity_change_proto)
    change_set_proto.changes.extend(entity_change_proto_list)
    change_set_proto.deletes.extend(
      [entity_id.get_value() for entity_id in list(self.deleted)]
    )

    return change_set_proto
