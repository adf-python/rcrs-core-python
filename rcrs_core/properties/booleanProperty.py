from rcrs_core.connection import URN
from rcrs_core.properties.property import Property


class BooleanProperty(Property[bool]):
    def __init__(self, urn: URN.Property) -> None:
        super().__init__(urn)
        self.value: bool = False

    def set_fields(self, value) -> None:
        self.value = bool(value)

    def copy(self) -> "BooleanProperty":
        new_boolean_prop = BooleanProperty(self.urn)
        new_boolean_prop.set_value(self.value)
        return new_boolean_prop

    def take_value(self, _property: "Property[bool]") -> None:
        if isinstance(_property, BooleanProperty):
            self.set_value(_property.get_value())
        else:
            raise Exception("cannot take value from ", _property)
