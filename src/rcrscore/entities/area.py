from typing import override

from rcrscore.entities.edge import Edge
from rcrscore.entities.entity import Entity
from rcrscore.entities.entity_id import EntityID
from rcrscore.properties.edge_list_property import EdgeListProperty
from rcrscore.properties.entity_id_list_property import EntityIDListProperty
from rcrscore.properties.property import Property
from rcrscore.urn.property import PropertyURN


class Area(Entity):
  def __init__(self, entity_id: int) -> None:
    super().__init__(entity_id)
    self._edges: EdgeListProperty = EdgeListProperty(PropertyURN.EDGES)
    self._blockades: EntityIDListProperty = EntityIDListProperty(PropertyURN.BLOCKADES)
    self._neighbors: set[EntityID] = set()
    self._apexes: list[int] = []
    self.register_properties([self._edges, self._blockades])

  @override
  def set_from_properties(self, properties: dict[PropertyURN, Property]) -> None:
    super().set_from_properties(properties)
    for key, values in properties.items():
      if key == PropertyURN.EDGES:
        self._edges.set_value(values.get_value())
      elif key == PropertyURN.BLOCKADES:
        self._blockades.set_value(values.get_value())

  def get_neighbors(self) -> set[EntityID]:
    if len(self._neighbors) > 0:
      return self._neighbors

    if edges := self._edges.get_value():
      for edge in edges:
        if neighbor := edge.get_neighbour():
          self._neighbors.add(neighbor)

    return self._neighbors

  def get_edge_to(self, neighbor: EntityID) -> Edge | None:
    if edges := self.get_edges().get_value():
      for edge in edges:
        if neighbor == edge.get_neighbour():
          return edge
    return None

  def get_edges(self) -> EdgeListProperty:
    return self._edges

  def get_apexes(self) -> list[int]:
    if self._apexes != []:
      return self._apexes

    if edges := self._edges.get_value():
      for edge in edges:
        self._apexes.append(edge.get_start_x())
        self._apexes.append(edge.get_start_y())
    return self._apexes

  def get_blockades(self) -> EntityIDListProperty:
    return self._blockades

  def __str__(self) -> str:
    return f"Area(id={self.get_entity_id()}, edges={self._edges}, blockades={self._blockades})"

  def __repr__(self) -> str:
    return f"Area(entity_id={self.get_entity_id()}, edges={self._edges}, blockades={self._blockades})"
