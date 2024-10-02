"""
This type stub file was generated by pyright.
"""

from rcrs_core.agents.agent import Agent
from rcrs_core.connection.connection import Connection

class ComponentLauncher:
    def __init__(self, port, host) -> None:
        ...
    
    def make_connection(self) -> Connection:
        ...
    
    def connect(self, agent: Agent, _request_id): # -> None:
        ...
    
    def generate_request_ID(self): # -> int:
        ...
    

