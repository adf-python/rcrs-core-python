from typing import overload

from rcrscore.entities.edge import Edge
from rcrscore.entities.entity_id import EntityID
from rcrscore.properties.boolean_property import BooleanProperty
from rcrscore.properties.edge_list_property import EdgeListProperty
from rcrscore.properties.entity_id_list_property import EntityIDListProperty
from rcrscore.properties.entity_id_property import EntityIDProperty
from rcrscore.properties.int_list_property import IntListProperty
from rcrscore.properties.int_property import IntProperty
from rcrscore.properties.property import Property
from rcrscore.proto.RCRSProto_pb2 import PropertyProto
from rcrscore.urn.property import PropertyURN


class StandardPropertyFactory:
  def __init__(self) -> None:
    pass

  @overload
  @staticmethod
  def make_property(
    urn: PropertyURN,
    value: int | None = None,
  ) -> IntProperty: ...

  @overload
  @staticmethod
  def make_property(
    urn: PropertyURN,
    value: list[int] | None = None,
  ) -> IntListProperty: ...

  @overload
  @staticmethod
  def make_property(
    urn: PropertyURN,
    value: list[EntityID] | None = None,
  ) -> EntityIDListProperty: ...

  @overload
  @staticmethod
  def make_property(
    urn: PropertyURN,
    value: list[Edge] | None = None,
  ) -> EdgeListProperty: ...

  @overload
  @staticmethod
  def make_property(
    urn: PropertyURN,
    value: bool | None = None,
  ) -> BooleanProperty: ...

  @overload
  @staticmethod
  def make_property(
    urn: PropertyURN,
    value: EntityID | None = None,
  ) -> EntityIDProperty: ...

  @staticmethod
  def make_property(
    urn: PropertyURN,
    value=None,
  ) -> Property:
    match urn:
      case PropertyURN.START_TIME:
        return IntProperty(urn, value)
      case PropertyURN.LONGITUDE:
        return IntProperty(urn, value)
      case PropertyURN.LATITUDE:
        return IntProperty(urn, value)
      case PropertyURN.WIND_FORCE:
        return IntProperty(urn, value)
      case PropertyURN.WIND_DIRECTION:
        return IntProperty(urn, value)
      case PropertyURN.X:
        return IntProperty(urn, value)
      case PropertyURN.Y:
        return IntProperty(urn, value)
      case PropertyURN.FLOORS:
        return IntProperty(urn, value)
      case PropertyURN.BUILDING_ATTRIBUTES:
        return IntProperty(urn, value)
      case PropertyURN.FIERYNESS:
        return IntProperty(urn, value)
      case PropertyURN.BROKENNESS:
        return IntProperty(urn, value)
      case PropertyURN.BUILDING_CODE:
        return IntProperty(urn, value)
      case PropertyURN.BUILDING_AREA_GROUND:
        return IntProperty(urn, value)
      case PropertyURN.BUILDING_AREA_TOTAL:
        return IntProperty(urn, value)
      case PropertyURN.DIRECTION:
        return IntProperty(urn, value)
      case PropertyURN.STAMINA:
        return IntProperty(urn, value)
      case PropertyURN.HP:
        return IntProperty(urn, value)
      case PropertyURN.DAMAGE:
        return IntProperty(urn, value)
      case PropertyURN.BURIEDNESS:
        return IntProperty(urn, value)
      case PropertyURN.WATER_QUANTITY:
        return IntProperty(urn, value)
      case PropertyURN.TEMPERATURE:
        return IntProperty(urn, value)
      case PropertyURN.IMPORTANCE:
        return IntProperty(urn, value)
      case PropertyURN.TRAVEL_DISTANCE:
        return IntProperty(urn, value)
      case PropertyURN.REPAIR_COST:
        return IntProperty(urn, value)
      case PropertyURN.CAPACITY:
        return IntProperty(urn, value)
      case PropertyURN.BEDCAPACITY:
        return IntProperty(urn, value)
      case PropertyURN.OCCUPIEDBEDS:
        return IntProperty(urn, value)
      case PropertyURN.REFILLCAPACITY:
        return IntProperty(urn, value)
      case PropertyURN.WAITINGLISTSIZE:
        return IntProperty(urn, value)
      case PropertyURN.APEXES:
        return IntListProperty(urn, value)
      case PropertyURN.POSITION_HISTORY:
        return IntListProperty(urn, value)
      case PropertyURN.BLOCKADES:
        return EntityIDListProperty(urn, value)
      case PropertyURN.EDGES:
        return EdgeListProperty(urn, value)
      case PropertyURN.IGNITION:
        return BooleanProperty(urn, value)
      case PropertyURN.POSITION:
        return EntityIDProperty(urn, value)
      case _:
        raise ValueError(f"Unknown PropertyURN: {urn}")

  @staticmethod
  def from_property_proto(property_proto: PropertyProto) -> Property:
    urn = PropertyURN(property_proto.urn)
    match urn:
      case PropertyURN.START_TIME:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.LONGITUDE:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.LATITUDE:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.WIND_FORCE:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.WIND_DIRECTION:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.X:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.Y:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.FLOORS:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.BUILDING_ATTRIBUTES:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.FIERYNESS:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.BROKENNESS:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.BUILDING_CODE:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.BUILDING_AREA_GROUND:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.BUILDING_AREA_TOTAL:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.DIRECTION:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.STAMINA:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.HP:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.DAMAGE:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.BURIEDNESS:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.WATER_QUANTITY:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.TEMPERATURE:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.IMPORTANCE:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.TRAVEL_DISTANCE:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.REPAIR_COST:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.CAPACITY:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.BEDCAPACITY:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.OCCUPIEDBEDS:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.REFILLCAPACITY:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.WAITINGLISTSIZE:
        return IntProperty(urn, property_proto.intValue)
      case PropertyURN.APEXES:
        proto_int_list = property_proto.intList
        value = [item for item in proto_int_list.values]
        return IntListProperty(urn, value)
      case PropertyURN.POSITION_HISTORY:
        proto_int_list = property_proto.intList
        value = [item for item in proto_int_list.values]
        return IntListProperty(urn, value)
      case PropertyURN.BLOCKADES:
        proto_int_list = property_proto.intList
        value = [EntityID(item) for item in proto_int_list.values]
        return EntityIDListProperty(urn, value)
      case PropertyURN.EDGES:
        proto_edge_list = property_proto.edgeList
        value = [
          Edge(
            start_x=item.startX,
            start_y=item.startY,
            end_x=item.endX,
            end_y=item.endY,
            neighbor=EntityID(item.neighbour) if item.neighbour != 0 else None,
          )
          for item in proto_edge_list.edges
        ]
        return EdgeListProperty(urn, value)
      case PropertyURN.IGNITION:
        return BooleanProperty(urn, property_proto.boolValue)
      case PropertyURN.POSITION:
        return EntityIDProperty(urn, value=EntityID(property_proto.intValue))
      case _:
        raise ValueError(f"Unknown PropertyURN: {urn}")
