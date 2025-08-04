from rcrscore.properties.property import Property
from rcrscore.proto import RCRSProto_pb2
from rcrscore.urn.property import PropertyURN


class IntProperty(Property[int]):
  def __init__(self, urn: PropertyURN, value: int | None = None) -> None:
    super().__init__(urn, value)

  def to_property_proto(self) -> RCRSProto_pb2.PropertyProto:
    proto = RCRSProto_pb2.PropertyProto()
    proto.urn = self.get_urn()
    if value := self.get_value():
      proto.defined = True
      proto.intValue = value
    else:
      proto.defined = False
    return proto
