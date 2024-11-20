from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Set

if TYPE_CHECKING:
    from rcrs_core.config.config import Config


class ConfigConstraint(ABC):
    @abstractmethod
    def is_violated(self, config: "Config") -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_keys(self) -> Set[str]:
        raise NotImplementedError
