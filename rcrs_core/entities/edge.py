from typing import Optional

from rcrs_core.worldmodel.entityID import EntityID


class Edge:
    def __init__(
        self,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        _neighbour: Optional[EntityID] = None,
    ):
        self.start = (start_x, start_y)
        self.end = (end_x, end_y)
        self.line = ((start_x, start_y), (end_x, end_y))
        self.neighbour = _neighbour

    def get_start_x(self) -> int:
        return self.start[0]

    def get_start_y(self) -> int:
        return self.start[1]

    def get_end_x(self) -> int:
        return self.end[0]

    def get_end_y(self) -> int:
        return self.end[1]

    def is_passable(self) -> bool:
        return self.neighbour is not None

    def get_neighbour(self) -> Optional[EntityID]:
        return self.neighbour

    def to_string(self) -> str:
        return (
            "Edge from "
            + self.start
            + " to "
            + self.end
            + " , neighbour= "
            + self.neighbour
        )
