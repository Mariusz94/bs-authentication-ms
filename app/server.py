import logging
import sys
from concurrent import futures

import config
import grpc
import service.grpc_exceptions.grpc_exceptions as gRPC_exceptions
from service import grpc_service
from service.logs_service.app_logs import config_logs, init_logging

sys.path.append(r"./grpc_file")

from grpc_file.bs_authentication_msg import authentication_pb2, authentication_pb2_grpc
from grpc_file.default_msg import default_pb2


class AuthenticationService:
    def Login(
        self,
        request: authentication_pb2.LoginData,
        context: grpc.ServicerContext,
    ) -> authentication_pb2.UserInfo:
        """
        Method used to log in user.

        Args:
            request (authentication_pb2.LoginData): A gRPC message containing user information.
            context (grpc.ServicerContext): Metadata actual session.

        Returns:
            authentication_pb2.UserInfo: A gRPC message containing response information.
        """
        logging.info("Started method: 'Login'")
        try:
            login = request.login
            password = request.password

            data: dict = grpc_service.login(login=login, password=password)
            response = authentication_pb2.UserInfo(
                id=data["id"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                phone_number=data["phone_number"],
                address=data["address"],
                login=data["login"],
            )

            logging.info("Finished method: 'Login'")
            return response

        except Exception as e:
            logging.exception("Method 'Login' ended with some errors:\n{e}")
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
        authentication_pb2_grpc.add_AuthenticationServiceServicer_to_server(
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
