from enum import IntEnum


class ComponentControlMessageURN(IntEnum):
  RequestID = 0x0201
  AgentID = 0x0202
  Version = 0x0203
  Name = 0x0204
  RequestedEntityTypes = 0x0205
  SimulatorID = 0x0206
  RequestNumber = 0x0207
  NumberOfIDs = 0x0208
  NewEntityIDs = 0x0209
  Reason = 0x020A
  Entities = 0x020B
  ViewerID = 0x020C
  AgentConfig = 0x020D
  Time = 0x020E
  Updates = 0x020F
  Hearing = 0x0210
  INTENSITIES = 0x0211
  TIMES = 0x0212
  ID = 0x0213
  Commands = 0x0214
  SimulatorConfig = 0x0215
  Changes = 0x0216
