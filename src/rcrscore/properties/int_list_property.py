from rcrscore.properties.property import Property
from rcrscore.proto import RCRSProto_pb2
from rcrscore.urn.property import PropertyURN


class IntListProperty(Property[list[int]]):
  def __init__(self, urn: PropertyURN, value: list[int] | None = None) -> None:
    super().__init__(urn, value)

  def to_property_proto(self) -> RCRSProto_pb2.PropertyProto:
    proto = RCRSProto_pb2.PropertyProto()
    proto.urn = self.get_urn()
    if value := self.get_value():
      proto.defined = True
      int_list_proto = RCRSProto_pb2.IntListProto()
      int_list_proto.values.extend(value)
      proto.intList.CopyFrom(int_list_proto)
    else:
      proto.defined = False
    return proto
