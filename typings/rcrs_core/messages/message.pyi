"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod

class Message(ABC):
    def __init__(self, _urn) -> None:
        ...
    
    @abstractmethod
    def read(self): # -> None:
        ...
    
    @abstractmethod
    def write(self): # -> None:
        ...
    
    def get_urn(self): # -> Any:
        ...
    

