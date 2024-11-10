from rcrs_core.connection import URN
from rcrs_core.entities.human import Human


class AmbulanceTeamEntity(Human):
    urn = URN.Entity.AMBULANCE_TEAM

    def __init__(self, entity_id: int):
        super().__init__(entity_id)

    def set_entity(self, properties):
        super().set_entity(properties)

    def get_entity_name(self):
        return "Ambulance Team"

    def copy_impl(self):
        return AmbulanceTeamEntity(self.get_id())
