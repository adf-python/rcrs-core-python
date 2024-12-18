from typing import List

from rcrs_core.commands.Command import Command
from rcrs_core.connection import URN, RCRSProto_pb2
from rcrs_core.worldmodel.entityID import EntityID


class AKMove(Command):
    def __init__(
        self,
        agent_id: EntityID,
        time: int,
        path: List[int],
        destinationX=-1,
        destinationY=-1,
    ) -> None:
        super().__init__()
        self.urn = URN.Command.AK_MOVE

        self.agent_id = agent_id
        self.path = path[:]
        self.time = time
        self.x = destinationX
        self.y = destinationY

    def prepare_cmd(self):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.urn
        msg.components[
            URN.ComponentControlMSG.AgentID
        ].entityID = self.agent_id.get_value()
        msg.components[URN.ComponentControlMSG.Time].intValue = self.time
        msg.components[URN.ComponentCommand.DestinationX].intValue = self.x
        msg.components[URN.ComponentCommand.DestinationY].intValue = self.y
        msg.components[URN.ComponentCommand.Path].entityIDList.values.extend(self.path)
        return msg
