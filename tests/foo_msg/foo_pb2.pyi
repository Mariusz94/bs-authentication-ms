from default_msg import default_pb2 as _default_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FooFile(_message.Message):
    __slots__ = ["foo_file", "foo_file_name"]
    FOO_FILE_FIELD_NUMBER: _ClassVar[int]
    FOO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    foo_file: bytes
    foo_file_name: str
    def __init__(self, foo_file_name: _Optional[str] = ..., foo_file: _Optional[bytes] = ...) -> None: ...

class FooFileInfo(_message.Message):
    __slots__ = ["foo_file_name"]
    FOO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    foo_file_name: str
    def __init__(self, foo_file_name: _Optional[str] = ...) -> None: ...

class FooRequest(_message.Message):
    __slots__ = ["foo_bool_field", "foo_float_field", "foo_int32_field", "foo_int64_field", "foo_repeated_bool_field", "foo_repeated_float_field", "foo_repeated_int32_field", "foo_repeated_int64_field", "foo_repeated_string_field", "foo_string_field"]
    FOO_BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    FOO_FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    FOO_INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    FOO_INT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    FOO_REPEATED_BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    FOO_REPEATED_FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    FOO_REPEATED_INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    FOO_REPEATED_INT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    FOO_REPEATED_STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    FOO_STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    foo_bool_field: bool
    foo_float_field: float
    foo_int32_field: int
    foo_int64_field: int
    foo_repeated_bool_field: _containers.RepeatedScalarFieldContainer[bool]
    foo_repeated_float_field: _containers.RepeatedScalarFieldContainer[float]
    foo_repeated_int32_field: _containers.RepeatedScalarFieldContainer[int]
    foo_repeated_int64_field: _containers.RepeatedScalarFieldContainer[int]
    foo_repeated_string_field: _containers.RepeatedScalarFieldContainer[str]
    foo_string_field: str
    def __init__(self, foo_string_field: _Optional[str] = ..., foo_repeated_string_field: _Optional[_Iterable[str]] = ..., foo_int32_field: _Optional[int] = ..., foo_repeated_int32_field: _Optional[_Iterable[int]] = ..., foo_int64_field: _Optional[int] = ..., foo_repeated_int64_field: _Optional[_Iterable[int]] = ..., foo_float_field: _Optional[float] = ..., foo_repeated_float_field: _Optional[_Iterable[float]] = ..., foo_bool_field: bool = ..., foo_repeated_bool_field: _Optional[_Iterable[bool]] = ...) -> None: ...

class FooResponse(_message.Message):
    __slots__ = ["foo_response"]
    FOO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    foo_response: str
    def __init__(self, foo_response: _Optional[str] = ...) -> None: ...

class FooStatus(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
