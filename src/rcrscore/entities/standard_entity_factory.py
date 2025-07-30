from rcrscore.entities.ambulance_center import AmbulanceCenter
from rcrscore.entities.ambulance_team import AmbulanceTeam
from rcrscore.entities.blockade import Blockade
from rcrscore.entities.building import Building
from rcrscore.entities.civilian import Civilian
from rcrscore.entities.entity import Entity
from rcrscore.entities.fire_brigade import FireBrigade
from rcrscore.entities.fire_station import FireStation
from rcrscore.entities.gas_station import GasStation
from rcrscore.entities.hydrant import Hydrant
from rcrscore.entities.police_force import PoliceForce
from rcrscore.entities.police_office import PoliceOffice
from rcrscore.entities.refuge import Refuge
from rcrscore.entities.road import Road
from rcrscore.urn.entity import EntityURN


class StandardEntityFactory:
  @staticmethod
  def make_entity(urn: EntityURN, raw_entity_id: int) -> Entity:
    if urn == EntityURN.BUILDING:
      return Building(raw_entity_id)
    elif urn == EntityURN.REFUGE:
      return Refuge(raw_entity_id)
    elif urn == EntityURN.ROAD:
      return Road(raw_entity_id)
    elif urn == EntityURN.BLOCKADE:
      return Blockade(raw_entity_id)
    elif urn == EntityURN.POLICE_FORCE:
      return PoliceForce(raw_entity_id)
    elif urn == EntityURN.POLICE_OFFICE:
      return PoliceOffice(raw_entity_id)
    elif urn == EntityURN.AMBULANCE_TEAM:
      return AmbulanceTeam(raw_entity_id)
    elif urn == EntityURN.AMBULANCE_CENTER:
      return AmbulanceCenter(raw_entity_id)
    elif urn == EntityURN.FIRE_BRIGADE:
      return FireBrigade(raw_entity_id)
    elif urn == EntityURN.FIRE_STATION:
      return FireStation(raw_entity_id)
    elif urn == EntityURN.CIVILIAN:
      return Civilian(raw_entity_id)
    elif urn == EntityURN.HYDRANT:
      return Hydrant(raw_entity_id)
    elif urn == EntityURN.GAS_STATION:
      return GasStation(raw_entity_id)
    raise ValueError(f"Unknown entity type: {urn}")
