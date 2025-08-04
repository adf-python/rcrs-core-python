from rtree import index

from rcrscore.entities.area import Area
from rcrscore.entities.blockade import Blockade
from rcrscore.entities.entity import Entity
from rcrscore.entities.entity_id import EntityID
from rcrscore.entities.human import Human
from rcrscore.entities.standard_entity_factory import StandardEntityFactory
from rcrscore.worldmodel.change_set import ChangeSet


class WorldModel:
  def __init__(self) -> None:
    self.index = index.Index()
    self.unindexed_entities: dict[EntityID, Entity] = {}
    self.human_rectangles: dict[Human, tuple[float, float, float, float]] = {}
    self.indexed = False
    self.min_x: float | None = None
    self.min_y: float | None = None
    self.max_x: float | None = None
    self.max_y: float | None = None
    self.num = 0

  def add_entity(self, entity: Entity) -> None:
    self.unindexed_entities[entity.get_entity_id()] = entity

  def add_entities(self, entities: list[Entity]) -> None:
    for entity in entities:
      self.unindexed_entities[entity.get_entity_id()] = entity

  def get_entity(self, entity_id: EntityID) -> Entity | None:
    return self.unindexed_entities.get(entity_id)

  def get_entities(self) -> list[Entity]:
    return list(self.unindexed_entities.values())

  def delete_entity(self, entity_id: EntityID) -> None:
    del self.unindexed_entities[entity_id]

  def delete_entities(self, entity_ids: list[EntityID]) -> None:
    for entity_id in entity_ids:
      self.delete_entity(entity_id)

  def merge(self, change_set: ChangeSet) -> None:
    for entity_id in change_set.get_changed_entities():
      entity = self.get_entity(entity_id)
      if entity is None:
        entity_urn = change_set.get_entity_urn(entity_id)
        if entity_urn is None:
          raise ValueError(f"Entity URN not found for entity ID: {entity_id}")
        entity = StandardEntityFactory.make_entity(entity_urn, entity_id.get_value())
        self.add_entity(entity)

      if change_properties := change_set.get_entity_changes(entity_id):
        entity.set_from_properties(change_properties)

    for entity_id in change_set.get_deleted_entities():
      self.delete_entity(entity_id)

    # update human rectangles
    new_human_rectangles_to_push = {}
    for human in self.human_rectangles:
      rectangle = self.human_rectangles[human]
      self.index.delete(human.get_entity_id().get_value(), rectangle)
      new_rectangle = self.make_rectangle(human)
      if new_rectangle is not None:
        left, bottom, right, top = new_rectangle
        self.index.insert(human.get_entity_id().get_value(), (left, bottom, right, top))
        new_human_rectangles_to_push[human] = (left, bottom, right, top)

    for human in new_human_rectangles_to_push:
      rectangle = new_human_rectangles_to_push[human]
      self.human_rectangles[human] = rectangle

  def index_entities(self) -> None:
    if not self.indexed:
      self.min_x = float("inf")
      self.min_y = float("inf")
      self.max_x = float("inf")
      self.max_y = float("inf")

      self.index = index.Index()
      self.human_rectangles.clear()

      for entity in self.unindexed_entities.values():
        rectangle = self.make_rectangle(entity)

        if rectangle is not None:
          left, bottom, right, top = rectangle
          self.index.insert(
            entity.get_entity_id().get_value(), (left, bottom, right, top)
          )
          self.min_x = min(self.min_x, left, right)
          self.max_x = max(self.max_x, left, right)
          self.min_y = min(self.min_y, bottom, top)
          self.max_y = max(self.max_y, bottom, top)
          if isinstance(entity, Human):
            self.human_rectangles[entity] = (left, bottom, right, top)
      self.indexed = True

  def make_rectangle(self, entity: Entity) -> tuple[float, float, float, float] | None:
    x1 = x2 = y1 = y2 = float("inf")
    apexes = []

    if isinstance(entity, Area):
      apexes = entity.get_apexes()
    elif isinstance(entity, Blockade):
      apexes = entity.get_apexes().get_value()
      if apexes is None:
        return None
    elif isinstance(entity, Human):
      apexes = []
      human_x, human_y = entity.get_location()
      apexes.append(human_x)
      apexes.append(human_y)
    else:
      return None

    if len(apexes) == 0:
      print("this " + str(type(entity)) + "entity does not have apexes!!")
      return None

    for i in range(0, len(apexes), 2):
      x1 = min(x1, apexes[i])
      x2 = max(x2, apexes[i])
      y1 = min(y1, apexes[i + 1])
      y2 = max(y2, apexes[i + 1])
    return x1, y1, x2, y2

  def get_rect_bounds(self) -> tuple[float, float, float, float]:
    if not self.indexed:
      self.index_entities()

    if (
      self.min_x is None
      or self.min_y is None
      or self.max_x is None
      or self.max_y is None
    ):
      raise ValueError("Bounds are not properly initialized.")

    return self.min_x, self.min_y, self.max_x - self.min_x, self.max_y - self.min_y

  def get_world_bounds(self) -> tuple[float, float, float, float]:
    if not self.indexed:
      self.index_entities()

    if (
      self.min_x is None
      or self.min_y is None
      or self.max_x is None
      or self.max_y is None
    ):
      raise ValueError("Bounds are not properly initialized.")

    return self.min_x, self.min_y, self.max_x, self.max_y

  def get_objects_in_rectangle(
    self, x1: float, y1: float, x2: float, y2: float
  ) -> list[Entity]:
    if not self.indexed:
      self.index_entities()

    entities_ids = self.index.intersection((x1, y1, x2, y2))

    result = []
    for entity_id in entities_ids:
      result.append(self.get_entity(EntityID(entity_id)))

    return result

  def get_objects_in_range(self, entity: Entity, range: float) -> list[Entity]:
    location = entity.get_location()

    if location is None:
      return []

    x = location[0].get_value()
    y = location[1].get_value()

    if x is None or y is None:
      return []

    return self.get_objects_in_rectangle(x - range, y - range, x + range, y + range)
