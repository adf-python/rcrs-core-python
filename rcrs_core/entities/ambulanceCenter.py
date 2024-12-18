from rcrs_core.connection import URN
from rcrs_core.entities.building import Building


class AmbulanceCentre(Building):
    urn = URN.Entity.AMBULANCE_CENTRE

    def __init__(self, entity_id: int):
        super().__init__(entity_id)
        pass

    def set_entity(self, properties):
        super().set_entity(properties)

    def get_entity_name(self):
        return "Ambulance Centre"

    def copy_impl(self):
        return AmbulanceCentre(self.get_id())
