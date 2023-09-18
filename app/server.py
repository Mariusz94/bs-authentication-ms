import logging
import sys, os
from concurrent import futures

import config
import service.grpc_exceptions.grpc_exceptions as gRPC_exceptions
from google.protobuf.json_format import MessageToDict
from service.logs_service.app_logs import config_logs, init_logging

import grpc


sys.path.append(r"./grpc_file")

from grpc_file.default_msg import default_pb2
from grpc_file.foo_msg import foo_pb2, foo_pb2_grpc


class AuthenticationService:
    def Login(
        self, request: foo_pb2.FooRequest, context: grpc.ServicerContext
    ) -> foo_pb2.FooResponse:
        """
        Sample function.

        Args:
            request (foo_pb2.FooRequest): A gRPC message containing information.
            context (grpc.ServicerContext): Metadata actual session.

        Returns:
            foo_pb2.FooResponse: A gRPC message containing response information.
        """
        logging.info("Started method: 'FooMethod1'")
        try:
            data_dict = MessageToDict(request, preserving_proto_field_name=True)

            foo_string_field = request.foo_string_field
            foo_repeated_string_field = request.foo_repeated_string_field
            foo_int32_field = request.foo_int32_field
            foo_repeated_int32_field = request.foo_repeated_int32_field
            foo_int64_field = request.foo_int64_field
            foo_repeated_int64_field = request.foo_repeated_int64_field
            foo_float_field = request.foo_float_field
            foo_repeated_float_field = request.foo_repeated_float_field
            foo_bool_field = request.foo_bool_field
            foo_repeated_bool_field = request.foo_repeated_bool_field

            response = foo_pb2.FooResponse(
                foo_response="Sample response",
            )

            logging.info("Finished method: 'FooMethod1'")
            return response

        except Exception as e:
            logging.exception("Method 'FooMethod1' ended with some errors:\n{e}")
            gRPC_exceptions.raise_unknown_grpc_exception(e=e, context=context)


def run_server():
    """
    Function to start a gRPC server for handling incoming requests.

    Raises:
        Exception: An exception is raised if an error occurs during server startup or operation.
    """
    try:
        init_logging()
        config_logs()
        server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=config.WORKERS),
            options=[
                ("grpc.max_send_message_length", config.MAX_MSG_LENGTH),
                ("grpc.max_receive_message_length", config.MAX_MSG_LENGTH),
            ],
        )
        foo_pb2_grpc.add_AuthenticationServiceServicer_to_server(
            AuthenticationService(), server
        )
        server.add_insecure_port("[::]:" + str(config.SERVICE_PORT))
        server.start()
        logging.info("MICROSERVICE IS WORKING")
        server.wait_for_termination()

    except Exception as e:
        if config.LOGGING_MODE == "DEBUG":
            raise
        logging.error("SERVER HAS STOPPED WORKING")
        logging.error(e)


if __name__ == "__main__":
    run_server()
