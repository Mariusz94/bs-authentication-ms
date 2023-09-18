import sys
from typing import List, Tuple

import config
import grpc
from google.protobuf.json_format import MessageToDict
from grpc import Channel

sys.path.append(r"./grpc_file")

from grpc_file.bs_authentication_msg import authentication_pb2, authentication_pb2_grpc
from grpc_file.default_msg import default_pb2


def _prepare_client() -> (
    Tuple[authentication_pb2_grpc.AuthenticationServiceStub, Channel]
):
    """
    Prepare client gRPC.

    Return:
        Tuple[authentication_pb2_grpc.AuthenticationServiceStub, Channel]: Client gRPC and channel to connect.
    """
    channel = grpc.insecure_channel(
        f"{config.BS_AUTHENTICATION_MS_IP}:{config.BS_AUTHENTICATION_MS_PORT}",
        options=[
            ("grpc.max_send_message_length", config.MAX_MSG_LENGTH),
            ("grpc.max_receive_message_length", config.MAX_MSG_LENGTH),
        ],
    )
    client = authentication_pb2_grpc.AuthenticationServiceStub(channel)
    return client, channel


def login(login: str, password: str) -> dict:
    """
    Method to login user.

    Args:
        login (str): User login.
        password (str): User password.

    Returns:
        dict: User info.
    """
    client, channel = _prepare_client()
    request = authentication_pb2.LoginData(login=login, password=password)
    data: authentication_pb2.UserInfo = client.Login(request)
    channel.close()
    data_dict = MessageToDict(data, preserving_proto_field_name=True)
    return data_dict
