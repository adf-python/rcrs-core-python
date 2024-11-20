from rcrs_core.connection import URN
from rcrs_core.messages.message import Message


class Shutdown(Message):
    def __init__(self, data) -> None:
        super().__init__(URN.ControlMSG.SHUTDOWN)

    def read(self):
        pass

    def write(self):
        pass
