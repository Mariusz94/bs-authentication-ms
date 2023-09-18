import config
import grpc
import json

def raise_unknown_grpc_exception(e: Exception, context: grpc.ServicerContext):
    """
    Raises a gRPC exception with status UNKNOWN and exception data.

    Args:
        e (Exception): Exception object.
        context (grpc.ServicerContext): Metadata of the current session.
    """
    if config.LOGGING_MODE == "DEBUG":
        raise
    msg = {"MICROSERVICE_NAME": config.SERVICE_NAME, "ERROR": str(e)}
    msg = json.dumps(msg)
    context.abort(code=grpc.StatusCode.UNKNOWN, details=msg)
