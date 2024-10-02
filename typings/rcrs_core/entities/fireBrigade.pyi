"""
This type stub file was generated by pyright.
"""

from rcrs_core.entities.human import Human

class FireBrigadeEntity(Human):
    urn = ...
    def __init__(self, entity_id) -> None:
        ...
    
    def set_entity(self, properties): # -> None:
        ...
    
    def copy_impl(self): # -> FireBrigadeEntity:
        ...
    
    def get_entity_name(self): # -> Literal['Fire brigade']:
        ...
    
    def get_property(self, urn): # -> IntProperty | EntityIDProperty | IntArrayProperty | None:
        ...
    
    def get_water_property(self): # -> IntProperty:
        ...
    
    def get_water(self): # -> None:
        ...
    
    def set_water(self, value): # -> None:
        ...
    


