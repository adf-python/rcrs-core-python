"""
This type stub file was generated by pyright.
"""

from rcrs_core.entities.human import Human

class PoliceForceEntity(Human):
    urn = ...
    def __init__(self, entity_id) -> None:
        ...
    
    def copy_impl(self): # -> PoliceForceEntity:
        ...
    
    def get_entity_name(self): # -> Literal['Police force']:
        ...
    
    def set_entity(self, properties): # -> None:
        ...
    


