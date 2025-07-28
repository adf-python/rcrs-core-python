# from rcrs_core.connection import URN
# from rcrs_core.entities.ambulanceCenter import AmbulanceCentre
# from rcrs_core.entities.ambulanceTeam import AmbulanceTeam
# from rcrs_core.entities.blockade import Blockade
# from rcrs_core.entities.building import Building
# from rcrs_core.entities.civilian import Civilian
# from rcrs_core.entities.fireBrigade import FireBrigade
# from rcrs_core.entities.fireStation import FireStation
# from rcrs_core.entities.gasStation import GasStation
# from rcrs_core.entities.hydrant import Hydrant
# from rcrs_core.entities.policeForce import PoliceForce
# from rcrs_core.entities.policeOffice import PoliceOffice
# from rcrs_core.entities.refuge import Refuge
# from rcrs_core.entities.road import Road

from rcrs_core.connection import URN
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


class StandardEntityFactory:
  @staticmethod
  def make_entity(urn, id) -> Entity:
    if urn == URN.Entity.BUILDING:
      return Building(id)
    elif urn == URN.Entity.REFUGE:
      return Refuge(id)
    elif urn == URN.Entity.ROAD:
      return Road(id)
    elif urn == URN.Entity.BLOCKADE:
      return Blockade(id)
    elif urn == URN.Entity.POLICE_FORCE:
      return PoliceForce(id)
    elif urn == URN.Entity.POLICE_OFFICE:
      return PoliceOffice(id)
    elif urn == URN.Entity.AMBULANCE_TEAM:
      return AmbulanceTeam(id)
    elif urn == URN.Entity.AMBULANCE_CENTRE:
      return AmbulanceCenter(id)
    elif urn == URN.Entity.FIRE_BRIGADE:
      return FireBrigade(id)
    elif urn == URN.Entity.FIRE_STATION:
      return FireStation(id)
    elif urn == URN.Entity.CIVILIAN:
      return Civilian(id)
    elif urn == URN.Entity.HYDRANT:
      return Hydrant(id)
    elif urn == URN.Entity.GAS_STATION:
      return GasStation(id)
    raise ValueError(f"Unknown entity type: {urn}")
