from rcrs_core.connection import URN, RCRSProto_pb2
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

    def to_property_proto(self):
        prop = RCRSProto_pb2.PropertyProto()
        prop.urn = self.urn
        if isinstance(self.value, bool):
            prop.defined = True
            prop.boolValue = self.value
        else:
            prop.defined = False
        return prop
