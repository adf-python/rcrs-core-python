from rcrs_core.connection import URN
from rcrs_core.entities.building import Building


class PoliceOffice(Building):
    urn = URN.Entity.POLICE_OFFICE

    def __init__(self, entity_id: int):
        Building.__init__(self, entity_id)

    def copy_impl(self):
        return PoliceOffice(self.get_id())

    def get_entity_name(self):
        return "Police office"

    def set_entity(self, properties):
        super().set_entity(properties)
