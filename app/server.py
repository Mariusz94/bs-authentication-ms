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


class FooService:
    def FooMethod1(
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

    def FooMethod2(
        self, request: foo_pb2.FooRequest, context: grpc.ServicerContext
    ) -> default_pb2.Empty:
        """
        Sample function.

        Args:
            request (foo_pb2.FooRequest): A gRPC message containing information.
            context (grpc.ServicerContext): Metadata actual session.

        Returns:
            default_pb2.Empty: A empty gRPC message.
        """
        logging.info("Started method: 'FooMethod2'")
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

            response = default_pb2.Empty()

            logging.info("Finished method: 'FooMethod2'")
            return response

        except Exception as e:
            logging.exception("Method 'FooMethod2' ended with some errors:\n{e}")
            gRPC_exceptions.raise_unknown_grpc_exception(e=e, context=context)

    def FooMethodDownloadFile(
        self, request: foo_pb2.FooFileInfo, context: grpc.ServicerContext
    ) -> foo_pb2.FooFile:
        """
        Sample function.

        Args:
            request (foo_pb2.FooFileInfo): A gRPC message containing information.
            context (grpc.ServicerContext): Metadata actual session.

        Returns:
            foo_pb2.FooFile: A gRPC message containing response file.
        """
        logging.info("Started method: 'FooMethodDownloadFile'")
        try:
            data_dict = MessageToDict(request, preserving_proto_field_name=True)

            foo_file_name = request.foo_file_name

            file_path = os.path.join(os.getcwd(), "assets", "images", "python_img.jpeg")

            with open(file_path, "rb") as image:
                f = image.read()
                image_byte = bytes(f)

            response = foo_pb2.FooFile(
                foo_file_name=foo_file_name,
                foo_file=image_byte,
            )

            logging.info("Finished method: 'FooMethodDownloadFile'")
            yield response

        except Exception as e:
            logging.exception(
                "Method 'FooMethodDownloadFile' ended with some errors:\n{e}"
            )
            gRPC_exceptions.raise_unknown_grpc_exception(e=e, context=context)

    def FooMethodUploadFile(
        self, request_iterator, context: grpc.ServicerContext
    ) -> foo_pb2.FooStatus:
        """
        Sample function.

        Args:
            request_iterator (foo_pb2.FooFile): A gRPC message containing file.
            context (grpc.ServicerContext): Metadata actual session.

        Returns:
            foo_pb2.FooStatus: A gRPC message containing response information.
        """
        logging.info("Started method: 'FooMethodUploadFile'")
        try:
            foo_file_name = ""
            foo_file = None
            for request in request_iterator:
                foo_file_name = request.foo_file_name
                foo_file = request.foo_file

            response = foo_pb2.FooStatus(
                status="SUCCESS",
            )

            logging.info("Finished method: 'FooMethodUploadFile'")
            return response

        except Exception as e:
            logging.exception(
                "Method 'FooMethodUploadFile' ended with some errors:\n{e}"
            )
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
        foo_pb2_grpc.add_FooServiceServicer_to_server(FooService(), server)
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
