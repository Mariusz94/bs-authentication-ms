import sys
from typing import List, Tuple

import config
import grpc
from google.protobuf.json_format import MessageToDict
from grpc import Channel

sys.path.append(r"./grpc_file")

from grpc_file.default_msg import default_pb2
from grpc_file.foo_msg import foo_pb2, foo_pb2_grpc


def _prepare_client() -> Tuple[foo_pb2_grpc.FooServiceStub, Channel]:
    """
    Prepare client gRPC.

    Return:
        Tuple[foo_pb2_grpc.FooServiceStub, Channel]: Client gRPC and channel to connect.
    """
    channel = grpc.insecure_channel(
        f"{config.FOO_MS_IP}:{config.FOO_MS_PORT}",
        options=[
            ("grpc.max_send_message_length", config.MAX_MSG_LENGTH),
            ("grpc.max_receive_message_length", config.MAX_MSG_LENGTH),
        ],
    )
    client = foo_pb2_grpc.FooServiceStub(channel)
    return client, channel


def foo_method_1(
    foo_string_field: str = "field",
    foo_repeated_string_field: List[str] = ["field1", "filed2"],
    foo_int32_field: int = 1,
    foo_repeated_int32_field: List[int] = [1, 2, 3, 4],
    foo_int64_field: int = 1,
    foo_repeated_int64_field: List[int] = [1, 2, 3, 4],
    foo_float_field: float = 1.1,
    foo_repeated_float_field: List[int] = [1.1, 2.2, 3.3, 4.4],
    foo_bool_field: bool = True,
    foo_repeated_bool_field: List[bool] = [False, True],
) -> dict:
    """
    Sample 'foo_method_1'.

    Args:
        foo_string_field (str): Sample field.
        foo_repeated_string_field (List[str]): Sample field.
        foo_int32_field (int): Sample field.
        foo_repeated_int32_field (List[int]): Sample field.
        foo_int64_field (int): Sample field.
        foo_repeated_int64_field (List[int]): Sample field.
        foo_float_field (float): Sample field.
        foo_repeated_float_field (List[float]): Sample field.
        foo_bool_field (bool): Sample field.
        foo_repeated_bool_field (List[bool]): Sample field.

    Returns:
        dict: Sample dict.
    """
    client, channel = _prepare_client()
    request = foo_pb2.FooRequest(
        foo_string_field=foo_string_field,
        foo_repeated_string_field=foo_repeated_string_field,
        foo_int32_field=foo_int32_field,
        foo_repeated_int32_field=foo_repeated_int32_field,
        foo_int64_field=foo_int64_field,
        foo_repeated_int64_field=foo_repeated_int64_field,
        foo_float_field=foo_float_field,
        foo_repeated_float_field=foo_repeated_float_field,
        foo_bool_field=foo_bool_field,
        foo_repeated_bool_field=foo_repeated_bool_field,
    )
    data: foo_pb2.FooResponse = client.FooMethod1(request)
    channel.close()
    data_dict = MessageToDict(data, preserving_proto_field_name=True)
    return data_dict


def foo_method_2(
    foo_string_field: str = "field",
    foo_repeated_string_field: List[str] = ["field1", "filed2"],
    foo_int32_field: int = 1,
    foo_repeated_int32_field: List[int] = [1, 2, 3, 4],
    foo_int64_field: int = 1,
    foo_repeated_int64_field: List[int] = [1, 2, 3, 4],
    foo_float_field: float = 1.1,
    foo_repeated_float_field: List[int] = [1.1, 2.2, 3.3, 4.4],
    foo_bool_field: bool = True,
    foo_repeated_bool_field: List[bool] = [False, True],
) -> dict:
    """
    Sample 'foo_method_2'.

    Args:
        foo_string_field (str): Sample field.
        foo_repeated_string_field (List[str]): Sample field.
        foo_int32_field (int): Sample field.
        foo_repeated_int32_field (List[int]): Sample field.
        foo_int64_field (int): Sample field.
        foo_repeated_int64_field (List[int]): Sample field.
        foo_float_field (float): Sample field.
        foo_repeated_float_field (List[float]): Sample field.
        foo_bool_field (bool): Sample field.
        foo_repeated_bool_field (List[bool]): Sample field.

    Returns:
        dict: Sample dict.
    """
    client, channel = _prepare_client()
    request = foo_pb2.FooRequest(
        foo_string_field=foo_string_field,
        foo_repeated_string_field=foo_repeated_string_field,
        foo_int32_field=foo_int32_field,
        foo_repeated_int32_field=foo_repeated_int32_field,
        foo_int64_field=foo_int64_field,
        foo_repeated_int64_field=foo_repeated_int64_field,
        foo_float_field=foo_float_field,
        foo_repeated_float_field=foo_repeated_float_field,
        foo_bool_field=foo_bool_field,
        foo_repeated_bool_field=foo_repeated_bool_field,
    )
    data: default_pb2.Empty = client.FooMethod2(request)
    channel.close()
    data_dict = MessageToDict(data, preserving_proto_field_name=True)
    return data_dict


def foo_method_download_file(foo_file_name: str = "sample_name.jpg") -> tuple:
    """
    Sample 'foo_method_download_file'.

    Args:
        foo_file_name (str): Sample path.

    Returns:
        dict: Sample dict.
    """
    client, channel = _prepare_client()
    request = foo_pb2.FooFileInfo(foo_file_name=foo_file_name)
    data: foo_pb2.FooFile = client.FooMethodDownloadFile(request)
    response = None
    for i in data:
        response = i
    channel.close()
    data_dict = MessageToDict(response, preserving_proto_field_name=True)
    return response.foo_file, data_dict


def foo_method_upload_file(
    foo_file: bytes,
    foo_file_name: str = "sample_name.jpg",
) -> dict:
    """
    Sample 'foo_method_upload_file'.

    Args:
        foo_file (bytes): Sample file.
        foo_file_name (str): Sample name

    Returns:
        dict: Sample dict.
    """
    client, channel = _prepare_client()
    request = foo_pb2.FooFile(
        foo_file_name=foo_file_name,
        foo_file=foo_file,
    )
    data = client.FooMethodUploadFile(iter([request]))
    channel.close()
    data_dict = MessageToDict(data, preserving_proto_field_name=True)
    return data_dict
