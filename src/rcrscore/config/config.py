from typing import Any


class Config:
  def __init__(self) -> None:
    self.data: dict[str, Any] = {}

  def set_value(self, key: str, value: Any) -> None:
    self.data[key] = value

  def get_value(self, key: str) -> Any | None:
    return self.data.get(key, None)
