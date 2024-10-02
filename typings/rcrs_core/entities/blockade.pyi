"""
This type stub file was generated by pyright.
"""

from rcrs_core.entities.entity import Entity

class Blockade(Entity):
    urn = ...
    def __init__(self, entity_id) -> None:
        ...
    
    def get_entity_name(self): # -> Literal['Blockade']:
        ...
    
    def set_entity(self, properties): # -> None:
        ...
    
    def copy_impl(self): # -> Blockade:
        ...
    
    def get_property(self, urn): # -> IntProperty | EntityIDProperty | IntArrayProperty | None:
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
    
    def get_apexes_property(self): # -> IntArrayProperty:
        ...
    
    def get_apexes(self): # -> None:
        ...
    
    def set_apexes(self, value): # -> None:
        ...
    
    def get_position_property(self): # -> EntityIDProperty:
        ...
    
    def get_position(self): # -> None:
        ...
    
    def set_position(self, value): # -> None:
        ...
    
    def get_repaire_cost_property(self): # -> IntProperty:
        ...
    
    def get_repaire_cost(self): # -> None:
        ...
    
    def set_repaire_cost(self, value): # -> None:
        ...
    
    def get_shape(self): # -> None:
        ...
    

