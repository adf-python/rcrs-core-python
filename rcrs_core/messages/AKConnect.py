from rcrs_core.connection import URN, RCRSProto_pb2
from rcrs_core.messages.message import Message


class AKConnect(Message):
    def __init__(self):
        super().__init__(URN.ControlMSG.AK_CONNECT)

    def write(self, request_id, agent):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.get_urn()
        msg.components[URN.ComponentControlMSG.RequestID].intValue = request_id
        msg.components[URN.ComponentControlMSG.Version].intValue = 2
        msg.components[URN.ComponentControlMSG.Name].stringValue = agent.name
        for urn in agent.get_requested_entities():
            msg.components[
                URN.ComponentControlMSG.RequestedEntityTypes
            ].intList.values.append(urn)

        return msg

    def read(self):
        pass
