class EntityID:
  def __init__(self, id: int):
    """Initialize EntityID

    Args:
        id (int): The entity's ID
    """
    if not isinstance(id, int):
      raise TypeError(f"EntityID requires int, got {type(id).__name__}")
    self._id: int = id

  def get_value(self) -> int:
    """Get the value of the ID"""
    return self._id

  def __eq__(self, other: object) -> bool:
    """Check equality"""
    if isinstance(other, EntityID):
      return self._id == other._id
    return False

  def __hash__(self) -> int:
    """Return hash value"""
    return hash(self._id)

  def __str__(self) -> str:
    """Return string representation"""
    return str(self._id)

  def __repr__(self) -> str:
    """Return debug string representation"""
    return f"EntityID({self._id})"
