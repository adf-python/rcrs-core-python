from rcrs_core.connection import URN
from rcrs_core.properties.property import Property
from rcrs_core.worldmodel.entityID import EntityID


class EntityIDProperty(Property[EntityID]):
    def __init__(self, urn: URN.Property) -> None:
        super().__init__(urn)
        self.value: EntityID = EntityID(0)

    def set_fields(self, value: int) -> None:
        self.value = EntityID(value)

    def copy(self) -> "EntityIDProperty":
        new_entity_id_prop = EntityIDProperty(self.urn)
        new_entity_id_prop.set_value(EntityID(self.value.get_value()))
        return new_entity_id_prop

    def take_value(self, _property: "Property[EntityID]") -> None:
        if isinstance(_property, EntityIDProperty):
            self.set_value(_property.get_value())
        else:
            raise Exception("cannot take value from ", _property)
