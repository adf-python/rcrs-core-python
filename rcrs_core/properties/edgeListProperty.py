from typing import List

from rcrs_core.connection import URN, RCRSProto_pb2
from rcrs_core.entities.edge import Edge
from rcrs_core.properties.property import Property
from rcrs_core.worldmodel.entityID import EntityID


class EdgeListProperty(Property[list[Edge]]):
    def __init__(self, urn: URN.Property) -> None:
        super().__init__(urn)
        self.value: list[Edge] = []

    def get_fields(self) -> None:
        pass

    def set_fields(self, data) -> None:
        _values = []
        edges = data.edges
        for i in range(len(edges)):
            if edges[i].neighbour == -1:
                edge = Edge(
                    edges[i].startX, edges[i].startY, edges[i].endX, edges[i].endY, None
                )
            else:
                edge = Edge(
                    edges[i].startX,
                    edges[i].startY,
                    edges[i].endX,
                    edges[i].endY,
                    EntityID(edges[i].neighbour),
                )

            _values.append(edge)

        self.value = _values

    def set_value(self, _value: List[Edge]) -> None:
        print(type(_value))
        if self.value is not None:
            self.value.clear()
            self.value.extend(_value)
        else:
            self.value = _value

    def set_edges(self, _edges: List[Edge]) -> None:
        self.value.clear()
        self.value.extend(_edges)

    def add_edge(self, _edge: Edge) -> None:
        if isinstance(_edge, Edge):
            self.value.append(_edge)

    def clear_edges(self) -> None:
        self.value.clear()

    def take_value(self, _value: "Property[list[Edge]]") -> None:
        print("edge list property was not implemented....?")
        pass

    def copy(self) -> "EdgeListProperty":
        new_edge_list_prop = EdgeListProperty(self.urn)
        new_edge_list_prop.value = []
        for edge in self.value:
            new_edge_list_prop.value.append(
                Edge(
                    edge.get_start_x(),
                    edge.get_start_y(),
                    edge.get_end_x(),
                    edge.get_end_y(),
                    EntityID(edge.get_neighbour().get_value()),
                )
            )
        return new_edge_list_prop

    def to_property_proto(self):
        prop = RCRSProto_pb2.PropertyProto()
        prop.urn = self.urn
        if isinstance(self.value, list):
            prop.defined = True
            edge_list_proto = RCRSProto_pb2.EdgeListProto()
            edge_proto_list = []
            for edge in self.value:
                edge_proto = RCRSProto_pb2.EdgeProto()
                edge_proto.startX = edge.get_start_x()
                edge_proto.startY = edge.get_start_y()
                edge_proto.endX = edge.get_end_x()
                edge_proto.endY = edge.get_end_y()
                if edge.get_neighbour() is not None:
                    edge_proto.neighbour = edge.get_neighbour().get_value()
                else:
                    edge_proto.neighbour = -1
                edge_proto_list.append(edge_proto)
            edge_list_proto.edges.extend(edge_proto_list)
            prop.edgeList.CopyFrom(edge_list_proto)
        else:
            prop.defined = False
        return prop
