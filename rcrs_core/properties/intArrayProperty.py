from rcrs_core.connection import URN
from rcrs_core.properties.property import Property


class IntArrayProperty(Property[list[int]]):
    def __init__(self, urn: URN.Property) -> None:
        super().__init__(urn)
        self.value: list[int] = []

    def set_fields(self, data) -> None:
        self.value = data.values[:]

    def set_value(self, data) -> None:
        if self.value is not None:
            self.value.clear()
            self.value.extend(data.values[:])
        else:
            self.value = data[:]

    def copy(self) -> "IntArrayProperty":
        new_int_array_prop = IntArrayProperty(self.urn)
        new_int_array_prop.value = []
        for int_val in self.value:
            new_int_array_prop.value.append(int_val)
        return new_int_array_prop

    def take_value(self, _property: "Property[list[int]]") -> None:
        if isinstance(_property, IntArrayProperty):
            if self.value is not None:
                self.value.clear()
                self.value.extend(_property.get_value())
            else:
                self.value = _property.get_value[:]
        else:
            raise Exception("cannot take value from ", _property)
