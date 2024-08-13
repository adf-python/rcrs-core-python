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
        if key in self.data:
            return self.data[key]
        return None

    def get_value_or_default(self, key: str, default: str) -> str:
        if key in self.data:
            return self.data[key]
        return default

    def get_int_value(self, key: str) -> int | None:
        if key in self.int_data:
            return self.int_data[key]
        return None

    def get_int_value_or_default(self, key: str, default: int) -> int:
        if key in self.int_data:
            return self.int_data[key]
        return default

    def get_float_value(self, key) -> float | None:
        if key in self.float_data:
            return self.float_data[key]
        return None

    def get_float_value_or_default(self, key: str, default: float) -> float:
        if key in self.float_data:
            return self.float_data[key]
        return default

    def get_boolean_value(self, key) -> bool | None:
        if key in self.boolean_data:
            return self.boolean_data[key]
        return None

    def get_boolean_value_or_default(self, key: str, default: bool) -> bool:
        if key in self.boolean_data:
            return self.boolean_data[key]
        return default

    def get_array_value(self, key) -> list | None:
        if key in self.array_data:
            return self.array_data[key]
        return None

    def get_array_value_or_default(self, key: str, default: list) -> list:
        if key in self.array_data:
            return self.array_data[key]
        return default

    def set_value(self, key: str, value: str) -> None:
        self.data[key] = value

    def set_int_value(self, key: str, value: int) -> None:
        self.int_data[key] = value

    def set_float_value(self, key: str, value: float) -> None:
        self.float_data[key] = value

    def set_boolean_value(self, key: str, value: bool) -> None:
        self.boolean_data[key] = value

    def set_array_value(self, key: str, value: list) -> None:
        self.array_data[key] = value
