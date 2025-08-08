import rcrscore.proto.RCRSProto_pb2 as _RCRSProto_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogProto(_message.Message):
    __slots__ = ("start", "initialCondition", "command", "perception", "config", "update", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    INITIALCONDITION_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    PERCEPTION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: StartLogProto
    initialCondition: InitialConditionsLogProto
    command: CommandLogProto
    perception: PerceptionLogProto
    config: ConfigLogProto
    update: UpdatesLogProto
    end: EndLogProto
    def __init__(self, start: _Optional[_Union[StartLogProto, _Mapping]] = ..., initialCondition: _Optional[_Union[InitialConditionsLogProto, _Mapping]] = ..., command: _Optional[_Union[CommandLogProto, _Mapping]] = ..., perception: _Optional[_Union[PerceptionLogProto, _Mapping]] = ..., config: _Optional[_Union[ConfigLogProto, _Mapping]] = ..., update: _Optional[_Union[UpdatesLogProto, _Mapping]] = ..., end: _Optional[_Union[EndLogProto, _Mapping]] = ...) -> None: ...

class StartLogProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitialConditionsLogProto(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[_RCRSProto_pb2.EntityProto]
    def __init__(self, entities: _Optional[_Iterable[_Union[_RCRSProto_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class CommandLogProto(_message.Message):
    __slots__ = ("time", "commands")
    TIME_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    time: int
    commands: _containers.RepeatedCompositeFieldContainer[_RCRSProto_pb2.MessageProto]
    def __init__(self, time: _Optional[int] = ..., commands: _Optional[_Iterable[_Union[_RCRSProto_pb2.MessageProto, _Mapping]]] = ...) -> None: ...

class PerceptionLogProto(_message.Message):
    __slots__ = ("time", "entityID", "visible", "communications")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ENTITYID_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_FIELD_NUMBER: _ClassVar[int]
    time: int
    entityID: int
    visible: _RCRSProto_pb2.ChangeSetProto
    communications: _containers.RepeatedCompositeFieldContainer[_RCRSProto_pb2.MessageProto]
    def __init__(self, time: _Optional[int] = ..., entityID: _Optional[int] = ..., visible: _Optional[_Union[_RCRSProto_pb2.ChangeSetProto, _Mapping]] = ..., communications: _Optional[_Iterable[_Union[_RCRSProto_pb2.MessageProto, _Mapping]]] = ...) -> None: ...

class ConfigLogProto(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _RCRSProto_pb2.ConfigProto
    def __init__(self, config: _Optional[_Union[_RCRSProto_pb2.ConfigProto, _Mapping]] = ...) -> None: ...

class UpdatesLogProto(_message.Message):
    __slots__ = ("time", "changes")
    TIME_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    time: int
    changes: _RCRSProto_pb2.ChangeSetProto
    def __init__(self, time: _Optional[int] = ..., changes: _Optional[_Union[_RCRSProto_pb2.ChangeSetProto, _Mapping]] = ...) -> None: ...

class EndLogProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
