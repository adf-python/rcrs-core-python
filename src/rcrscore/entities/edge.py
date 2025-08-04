from rcrscore.entities.entity_id import EntityID


class Edge:
  def __init__(
    self,
    start_x: int,
    start_y: int,
    end_x: int,
    end_y: int,
    neighbor: EntityID | None = None,
  ):
    self._start = (start_x, start_y)
    self._end = (end_x, end_y)
    self._line = ((start_x, start_y), (end_x, end_y))
    self._neighbor = neighbor

  def get_start_x(self) -> int:
    return self._start[0]

  def get_start_y(self) -> int:
    return self._start[1]

  def get_end_x(self) -> int:
    return self._end[0]

  def get_end_y(self) -> int:
    return self._end[1]

  def get_neighbour(self) -> EntityID | None:
    return self._neighbor

  def __str__(self) -> str:
    return f"Edge(start=({self._start[0]}, {self._start[1]}), end=({self._end[0]}, {self._end[1]}), neighbor={self._neighbor})"
