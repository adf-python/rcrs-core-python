from rcrs_core.connection import URN
from rcrs_core.properties.property import Property


class IntProperty(Property[int]):
    def __init__(self, urn: URN.Property) -> None:
        super().__init__(urn)
        self.value: int = 0

    def set_fields(self, value: int) -> None:
        self.value = value

    def copy(self) -> "IntProperty":
        new_int_prop = IntProperty(self.urn)
        new_int_prop.set_value(self.value)
        return new_int_prop

    def take_value(self, _property: "Property[int]") -> None:
        if isinstance(_property, IntProperty):
            self.set_value(_property.get_value())
        else:
            raise Exception("cannot take value from ", _property)
