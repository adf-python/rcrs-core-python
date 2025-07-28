from rcrscore.entities.entity_id import EntityID
from rcrscore.properties.property import Property
from rcrscore.proto import RCRSProto_pb2
from rcrscore.urn.property import PropertyURN


class EntityIDListProperty(Property[list[EntityID]]):
  def __init__(self, urn: PropertyURN, value: list[EntityID] | None = None) -> None:
    super().__init__(urn, value)

  def to_property_proto(self) -> RCRSProto_pb2.PropertyProto:
    proto = RCRSProto_pb2.PropertyProto()
    proto.urn = self.get_urn()
    if value := self.get_value():
      proto.defined = True
      int_list_proto = RCRSProto_pb2.IntListProto()
      int_list_proto.values.extend([entity_id.get_value() for entity_id in value])
      proto.intList.CopyFrom(int_list_proto)
    else:
      proto.defined = False
    return proto
