from typing import List

from rcrscore.entities.edge import Edge
from rcrscore.properties.property import Property
from rcrscore.proto import RCRSProto_pb2
from rcrscore.urn.property import PropertyURN


class EdgeListProperty(Property[list[Edge]]):
  def __init__(self, urn: PropertyURN, value: List[Edge] | None = None) -> None:
    super().__init__(urn, value)

  def to_property_proto(self) -> RCRSProto_pb2.PropertyProto:
    proto = RCRSProto_pb2.PropertyProto()
    proto.urn = self.get_urn()
    if value := self.get_value():
      proto.defined = True
      edge_list_proto = RCRSProto_pb2.EdgeListProto()
      edge_proto_list = []
      for edge in value:
        edge_proto = RCRSProto_pb2.EdgeProto()
        edge_proto.startX = edge.get_start_x()
        edge_proto.startY = edge.get_start_y()
        edge_proto.endX = edge.get_end_x()
        edge_proto.endY = edge.get_end_y()
        if neighbour := edge.get_neighbour():
          edge_proto.neighbour = neighbour.get_value()
        else:
          edge_proto.neighbour = -1
        edge_proto_list.append(edge_proto)
      edge_list_proto.edges.extend(edge_proto_list)
      proto.edgeList.CopyFrom(edge_list_proto)
      return proto
    else:
      proto.defined = False
      return proto
