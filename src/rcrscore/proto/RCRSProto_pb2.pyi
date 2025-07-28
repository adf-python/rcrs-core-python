from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageProto(_message.Message):
    __slots__ = ("urn", "components")
    class ComponentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MessageComponentProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MessageComponentProto, _Mapping]] = ...) -> None: ...
    URN_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    urn: int
    components: _containers.MessageMap[int, MessageComponentProto]
    def __init__(self, urn: _Optional[int] = ..., components: _Optional[_Mapping[int, MessageComponentProto]] = ...) -> None: ...

class MessageListProto(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[MessageProto]
    def __init__(self, commands: _Optional[_Iterable[_Union[MessageProto, _Mapping]]] = ...) -> None: ...

class MessageComponentProto(_message.Message):
    __slots__ = ("changeSet", "commandList", "config", "entity", "entityID", "entityIDList", "entityList", "floatList", "intValue", "intList", "rawData", "stringValue", "stringList")
    CHANGESET_FIELD_NUMBER: _ClassVar[int]
    COMMANDLIST_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITYID_FIELD_NUMBER: _ClassVar[int]
    ENTITYIDLIST_FIELD_NUMBER: _ClassVar[int]
    ENTITYLIST_FIELD_NUMBER: _ClassVar[int]
    FLOATLIST_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    INTLIST_FIELD_NUMBER: _ClassVar[int]
    RAWDATA_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGLIST_FIELD_NUMBER: _ClassVar[int]
    changeSet: ChangeSetProto
    commandList: MessageListProto
    config: ConfigProto
    entity: EntityProto
    entityID: int
    entityIDList: IntListProto
    entityList: EntityListProto
    floatList: FloatListProto
    intValue: int
    intList: IntListProto
    rawData: bytes
    stringValue: str
    stringList: StrListProto
    def __init__(self, changeSet: _Optional[_Union[ChangeSetProto, _Mapping]] = ..., commandList: _Optional[_Union[MessageListProto, _Mapping]] = ..., config: _Optional[_Union[ConfigProto, _Mapping]] = ..., entity: _Optional[_Union[EntityProto, _Mapping]] = ..., entityID: _Optional[int] = ..., entityIDList: _Optional[_Union[IntListProto, _Mapping]] = ..., entityList: _Optional[_Union[EntityListProto, _Mapping]] = ..., floatList: _Optional[_Union[FloatListProto, _Mapping]] = ..., intValue: _Optional[int] = ..., intList: _Optional[_Union[IntListProto, _Mapping]] = ..., rawData: _Optional[bytes] = ..., stringValue: _Optional[str] = ..., stringList: _Optional[_Union[StrListProto, _Mapping]] = ...) -> None: ...

class StrListProto(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class IntListProto(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class FloatListProto(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class IntMatrixProto(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[IntListProto]
    def __init__(self, values: _Optional[_Iterable[_Union[IntListProto, _Mapping]]] = ...) -> None: ...

class ValueProto(_message.Message):
    __slots__ = ("defined", "intValue", "boolValue", "doubleValue", "byteList", "intList", "intMatrix", "edgeList", "point2D")
    DEFINED_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLEVALUE_FIELD_NUMBER: _ClassVar[int]
    BYTELIST_FIELD_NUMBER: _ClassVar[int]
    INTLIST_FIELD_NUMBER: _ClassVar[int]
    INTMATRIX_FIELD_NUMBER: _ClassVar[int]
    EDGELIST_FIELD_NUMBER: _ClassVar[int]
    POINT2D_FIELD_NUMBER: _ClassVar[int]
    defined: bool
    intValue: int
    boolValue: bool
    doubleValue: float
    byteList: bytes
    intList: IntListProto
    intMatrix: IntMatrixProto
    edgeList: EdgeListProto
    point2D: Point2DProto
    def __init__(self, defined: bool = ..., intValue: _Optional[int] = ..., boolValue: bool = ..., doubleValue: _Optional[float] = ..., byteList: _Optional[bytes] = ..., intList: _Optional[_Union[IntListProto, _Mapping]] = ..., intMatrix: _Optional[_Union[IntMatrixProto, _Mapping]] = ..., edgeList: _Optional[_Union[EdgeListProto, _Mapping]] = ..., point2D: _Optional[_Union[Point2DProto, _Mapping]] = ...) -> None: ...

class PropertyProto(_message.Message):
    __slots__ = ("urn", "defined", "intValue", "boolValue", "doubleValue", "byteList", "intList", "intMatrix", "edgeList", "point2D")
    URN_FIELD_NUMBER: _ClassVar[int]
    DEFINED_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLEVALUE_FIELD_NUMBER: _ClassVar[int]
    BYTELIST_FIELD_NUMBER: _ClassVar[int]
    INTLIST_FIELD_NUMBER: _ClassVar[int]
    INTMATRIX_FIELD_NUMBER: _ClassVar[int]
    EDGELIST_FIELD_NUMBER: _ClassVar[int]
    POINT2D_FIELD_NUMBER: _ClassVar[int]
    urn: int
    defined: bool
    intValue: int
    boolValue: bool
    doubleValue: float
    byteList: bytes
    intList: IntListProto
    intMatrix: IntMatrixProto
    edgeList: EdgeListProto
    point2D: Point2DProto
    def __init__(self, urn: _Optional[int] = ..., defined: bool = ..., intValue: _Optional[int] = ..., boolValue: bool = ..., doubleValue: _Optional[float] = ..., byteList: _Optional[bytes] = ..., intList: _Optional[_Union[IntListProto, _Mapping]] = ..., intMatrix: _Optional[_Union[IntMatrixProto, _Mapping]] = ..., edgeList: _Optional[_Union[EdgeListProto, _Mapping]] = ..., point2D: _Optional[_Union[Point2DProto, _Mapping]] = ...) -> None: ...

class Point2DProto(_message.Message):
    __slots__ = ("X", "Y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    X: float
    Y: float
    def __init__(self, X: _Optional[float] = ..., Y: _Optional[float] = ...) -> None: ...

class EntityProto(_message.Message):
    __slots__ = ("urn", "entityID", "properties")
    URN_FIELD_NUMBER: _ClassVar[int]
    ENTITYID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    urn: int
    entityID: int
    properties: _containers.RepeatedCompositeFieldContainer[PropertyProto]
    def __init__(self, urn: _Optional[int] = ..., entityID: _Optional[int] = ..., properties: _Optional[_Iterable[_Union[PropertyProto, _Mapping]]] = ...) -> None: ...

class EntityListProto(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[EntityProto]
    def __init__(self, entities: _Optional[_Iterable[_Union[EntityProto, _Mapping]]] = ...) -> None: ...

class ConfigProto(_message.Message):
    __slots__ = ("data",)
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.ScalarMap[str, str]
    def __init__(self, data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EdgeListProto(_message.Message):
    __slots__ = ("edges",)
    EDGES_FIELD_NUMBER: _ClassVar[int]
    edges: _containers.RepeatedCompositeFieldContainer[EdgeProto]
    def __init__(self, edges: _Optional[_Iterable[_Union[EdgeProto, _Mapping]]] = ...) -> None: ...

class EdgeProto(_message.Message):
    __slots__ = ("startX", "startY", "endX", "endY", "neighbour")
    STARTX_FIELD_NUMBER: _ClassVar[int]
    STARTY_FIELD_NUMBER: _ClassVar[int]
    ENDX_FIELD_NUMBER: _ClassVar[int]
    ENDY_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOUR_FIELD_NUMBER: _ClassVar[int]
    startX: int
    startY: int
    endX: int
    endY: int
    neighbour: int
    def __init__(self, startX: _Optional[int] = ..., startY: _Optional[int] = ..., endX: _Optional[int] = ..., endY: _Optional[int] = ..., neighbour: _Optional[int] = ...) -> None: ...

class ChangeSetProto(_message.Message):
    __slots__ = ("changes", "deletes")
    class EntityChangeProto(_message.Message):
        __slots__ = ("entityID", "urn", "properties")
        ENTITYID_FIELD_NUMBER: _ClassVar[int]
        URN_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        entityID: int
        urn: int
        properties: _containers.RepeatedCompositeFieldContainer[PropertyProto]
        def __init__(self, entityID: _Optional[int] = ..., urn: _Optional[int] = ..., properties: _Optional[_Iterable[_Union[PropertyProto, _Mapping]]] = ...) -> None: ...
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    DELETES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ChangeSetProto.EntityChangeProto]
    deletes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, changes: _Optional[_Iterable[_Union[ChangeSetProto.EntityChangeProto, _Mapping]]] = ..., deletes: _Optional[_Iterable[int]] = ...) -> None: ...
