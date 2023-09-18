import sys
from typing import List, Tuple

import config
import grpc
from google.protobuf.json_format import MessageToDict
from grpc import Channel

sys.path.append(r"./grpc_file")

from grpc_file.default_msg import default_pb2
from grpc_file.bs_db_connector_msg import db_connector_pb2, db_connector_pb2_grpc


def _prepare_client() -> Tuple[db_connector_pb2_grpc.DbConnectorServiceStub, Channel]:
    """
    Prepare client gRPC.

    Return:
        Tuple[foo_pb2_grpc.FooServiceStub, Channel]: Client gRPC and channel to connect.
    """
    channel = grpc.insecure_channel(
        f"{config.BS_DB_CONNECTOR_MS_IP}:{config.BS_DB_CONNECTOR_MS_PORT}",
        options=[
            ("grpc.max_send_message_length", config.MAX_MSG_LENGTH),
            ("grpc.max_receive_message_length", config.MAX_MSG_LENGTH),
        ],
    )
    client = db_connector_pb2_grpc.DbConnectorServiceStub(channel)
    return client, channel


def get_balance(user_id: str) -> dict:
    """
    Method gRPC to obtain user balance.

    Args:
        user_id (str): User id.

    Returns:
        dict: User balance info.
    """
    client, channel = _prepare_client()
    request = db_connector_pb2.UserId(user_id=user_id)
    data: db_connector_pb2.BalanceInfo = client.GetBalance(request)
    channel.close()
    data_dict = MessageToDict(data, preserving_proto_field_name=True)
    return data_dict


def get_user_info(user_id: str) -> dict:
    """
    Method gRPC to obtain user info.

    Args:
        user_id (str): User id.

    Returns:
        dict: User info.
    """
    client, channel = _prepare_client()
    request = db_connector_pb2.UserId(user_id=user_id)
    data: db_connector_pb2.UserInfo = client.GetUserInfo(request)
    channel.close()
    data_dict = MessageToDict(data, preserving_proto_field_name=True)
    return data_dict
