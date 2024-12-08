from rcrs_core.connection import URN, RCRSProto_pb2
from rcrs_core.properties.property import Property
from rcrs_core.worldmodel.entityID import EntityID


class EntityIDListProperty(Property[list[EntityID]]):
    def __init__(self, urn: URN.Property) -> None:
        super().__init__(urn)
        self.value: list[EntityID] = []

    def set_fields(self, data) -> None:
        _values = []
        for d in data.values:
            _values.append(EntityID(d))
        self.value = _values

    def set_value(self, _value: list[EntityID]) -> None:
        if self.value is not None:
            self.value.clear()
            self.value.extend(_value)
        else:
            self.value = _value

    def copy(self) -> "EntityIDListProperty":
        new_entity_id_list_prop = EntityIDListProperty(self.urn)
        new_entity_id_list_prop.value = []
        for entity_id in self.value:
            new_entity_id_list_prop.value.append(EntityID(entity_id.get_value()))
        return new_entity_id_list_prop

    def take_value(self, _property: "Property[list[EntityID]]") -> None:
        if isinstance(_property, EntityIDListProperty):
            self.set_value(_property.get_value())
        else:
            raise Exception("cannot take value from ", _property)

    def to_property_proto(self):
        prop = RCRSProto_pb2.PropertyProto()
        prop.urn = self.urn
        if isinstance(self.value, list):
            prop.defined = True
            int_list_proto = RCRSProto_pb2.IntListProto()
            int_list_proto.values.extend([entity_id.get_value() for entity_id in self.value])
            prop.intList.CopyFrom(int_list_proto)
        else:
            prop.defined = False
        return prop
