"""
This type stub file was generated by pyright.
"""

from typing import List
from rcrs_core.entities.entity import Entity
from rcrs_core.worldmodel.changeSet import ChangeSet
from rcrs_core.worldmodel.entityID import EntityID

class WorldModel:
    def __init__(self) -> None:
        ...
    
    def add_entities(self, entities: List[Entity]): # -> None:
        ...
    
    def get_entity(self, entity_id: EntityID) -> Entity:
        ...
    
    def add_entity(self, entity): # -> None:
        ...
    
    def remove_entity(self, entity_id): # -> None:
        ...
    
    def get_entities(self): # -> dict_values[Any, Any]:
        ...
    
    def merge(self, change_set: ChangeSet): # -> None:
        ...
    
    def index_entities(self): # -> None:
        ...
    
    def make_rectangle(self, entity): # -> tuple[None, None, None, None] | tuple[float, float, float, float]:
        ...
    
    def get_rect_bounds(self): # -> tuple[Any, Any, Any, Any]:
        ...
    
    def get_world_bounds(self): # -> tuple[Any, Any, Any, Any]:
        ...
    
    def get_objects_in_rectangle(self, x1, y1, x2, y2): # -> list[Any]:
        ...
    
    def get_objects_in_range(self, entity, range): # -> list[Any]:
        ...
    

