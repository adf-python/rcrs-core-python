"""
This type stub file was generated by pyright.
"""

from rcrs_core.worldmodel.entityID import EntityID
from abc import ABC

class Entity(ABC):
    def __init__(self, _entity_id) -> None:
        ...
    
    def set_entity(self, properties): # -> None:
        ...
    
    def get_id(self) -> EntityID:
        ...
    
    def get_properties(self): # -> dict[Any, Any]:
        ...
    
    def register_properties(self, _properties): # -> None:
        ...
    
    def copy_impl(self): # -> Entity:
        ...
    
    def copy(self): # -> Entity:
        ...
    
    def get_urn(self):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def get_property(self, property_urn): # -> None:
        ...
    
    def get_location(self): # -> tuple[Any | None, Any | None] | tuple[None, None]:
        ...
    
    def get_x_property(self): # -> IntProperty:
        ...
    
    def get_x(self): # -> None:
        ...
    
    def set_x(self, value): # -> None:
        ...
    
    def get_y_property(self): # -> IntProperty:
        ...
    
    def get_y(self): # -> None:
        ...
    
    def set_y(self, value): # -> None:
        ...
    

