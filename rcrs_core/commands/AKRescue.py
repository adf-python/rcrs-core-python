from rcrs_core.commands.Command import Command
from rcrs_core.connection import URN, RCRSProto_pb2
from rcrs_core.worldmodel.entityID import EntityID


class AKRescue(Command):
    def __init__(self, agent_id: EntityID, time: int, target: EntityID) -> None:
        super().__init__()
        self.urn = URN.Command.AK_RESCUE
        self.agent_id = agent_id
        self.target = target
        self.time = time

    def prepare_cmd(self):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.urn
        msg.components[
            URN.ComponentControlMSG.AgentID
        ].entityID = self.agent_id.get_value()
        msg.components[URN.ComponentControlMSG.Time].intValue = self.time
        msg.components[URN.ComponentCommand.Target].entityID = self.target.get_value()
        return msg
