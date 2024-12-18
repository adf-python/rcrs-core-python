from rcrs_core.connection import URN
from rcrs_core.messages.message import Message


class KAConnectError(Message):
    def __init__(self, data):
        super().__init__(URN.ControlMSG.GK_CONNECT_ERROR)
        self.data = data
        self.read()

    def read(self):
        self.request_id = self.data.components[
            URN.ComponentControlMSG.RequestID
        ].intValue
        self.reason = self.data.components[URN.ComponentControlMSG.Reason].stringValue

    def write(self):
        pass
