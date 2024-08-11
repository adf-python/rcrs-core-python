from __future__ import annotations
from typing import Dict, Set

from rcrs_core.config.config_constraint import ConfigConstraint

class Config:
    
    def __init__(self) -> None:
        self.data: Dict[str, str] = {}
        self.no_cache: Set[str] = set()
        self.int_data: Dict[str, int] = {}
        self.float_data: Dict[str, float] = {}
        self.boolean_data: Dict[str, bool] = {}
        self.array_data: Dict[str, list] = {}
        self.constraints: Set[ConfigConstraint] = set()
        self.violated_constraints: Set[ConfigConstraint] = set()
    
    def get_value(self, key: str) -> str | None:
        if key in self._data:
            return self._data[key]
        return None
    
    def get_float_value(self, key):
        pass
    
    def get_boolean_value(self, key):
        pass
    
    def get_array_value(self, key):
        pass

    def set_value(self, key: str, value: str) -> None:
        self.data[key] = value
