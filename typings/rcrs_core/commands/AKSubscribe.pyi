"""
This type stub file was generated by pyright.
"""

from rcrs_core.commands.Command import Command
from rcrs_core.worldmodel.entityID import EntityID
from typing import List

class AKSubscribe(Command):
    def __init__(self, agent_id: EntityID, time: int, channels: List[int]) -> None:
        ...
    
    def prepare_cmd(self): # -> MessageProto:
        ...
    

