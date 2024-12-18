from rcrs_core.connection import URN
from rcrs_core.entities.entity import Entity
from rcrs_core.properties.entityIDProperty import EntityIDProperty
from rcrs_core.properties.intArrayProperty import IntArrayProperty
from rcrs_core.properties.intProperty import IntProperty


class Blockade(Entity):
    urn = URN.Entity.BLOCKADE

    def __init__(self, entity_id: int):
        super().__init__(entity_id)
        self.position = EntityIDProperty(URN.Property.POSITION)
        self.apexes = IntArrayProperty(URN.Property.APEXES)
        self.repair_cost = IntProperty(URN.Property.REPAIR_COST)
        self.shape = None

        self.register_properties([self.position, self.apexes, self.repair_cost])

    def get_entity_name(self):
        return "Blockade"

    def set_entity(self, properties):
        super().set_entity(properties)

        for key, values in properties.items():
            if key == URN.Property.POSITION:
                self.position.set_value(values)

            elif key == URN.Property.REPAIR_COST:
                self.repair_cost.set_value(values)

            elif key == URN.Property.APEXES:
                self.apexes.set_value(values)

    def copy_impl(self):
        return Blockade(self.get_id())

    def get_property(self, urn):
        if urn == URN.Property.X:
            return self.x
        elif urn == URN.Property.Y:
            return self.y
        elif urn == URN.Property.POSITION:
            return self.position
        elif urn == URN.Property.APEXES:
            return self.apexes
        elif urn == URN.Property.REPAIR_COST:
            return self.repair_cost
        else:
            return super().get_property(urn)

    def get_x_property(self):
        return self.x

    def get_x(self):
        return self.x.get_value()

    def set_x(self, value):
        self.x.set_value(value)

    def get_y_property(self):
        return self.y

    def get_y(self):
        return self.y.get_value()

    def set_y(self, value):
        self.y.set_value(value)

    def get_apexes_property(self):
        return self.apexes

    def get_apexes(self):
        return self.apexes.get_value()

    def set_apexes(self, value):
        self.apexes.set_value(value)

    def get_position_property(self):
        return self.position

    def get_position(self):
        return self.position.get_value()

    def set_position(self, value):
        self.position.set_value(value)

    def get_repaire_cost_property(self):
        return self.repair_cost

    def get_repaire_cost(self):
        return self.repair_cost.get_value()

    def set_repaire_cost(self, value):
        self.repair_cost.set_value(value)

    def get_shape(self):
        return None
