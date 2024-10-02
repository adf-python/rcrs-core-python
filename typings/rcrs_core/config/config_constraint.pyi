"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod
from typing import Set, TYPE_CHECKING
from rcrs_core.config.config import Config

if TYPE_CHECKING:
    ...
class ConfigConstraint(ABC):
    @abstractmethod
    def is_violated(self, config: Config) -> bool:
        ...
    
    @abstractmethod
    def get_description(self) -> str:
        ...
    
    @abstractmethod
    def get_keys(self) -> Set[str]:
        ...
    


