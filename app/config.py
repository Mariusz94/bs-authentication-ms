import os

from dotenv import load_dotenv

load_dotenv()

"""
Configuration file.
"""

SERVICE_NAME = "python"
"""Microservice name."""

MS_VERSION = str(os.environ.get("MS_VERSION", "NOT AVAILABLE"))
"""Microservice version."""

SERVICE_PORT = int(os.environ.get("SERVICE_PORT", 80))
"""Port where the service is available."""

WORKERS = int(os.environ.get("WORKERS", 1))
"""Number of gRPC workers within a single instance (the number of messages that are processed simultaneously)."""

MAX_MSG_LENGTH = int(os.environ.get("MAX_MSG_LENGTH", -1))
"""Maximum length of gRPC messages received and sent, -1 indicates unlimited size."""

LOGGING_MODE = str(os.environ.get("LOGGING_MODE", "DEBUG"))
"""Logging level for information and errors."""

LOGGER_FORMAT_INFO = "%(asctime)s.%(msecs)03d-%(levelname)s-%(funcName)s()-%(message)s"
"""Logger format for the info level."""

LOGGER_FORMAT_DEBUG = "%(asctime)s.%(msecs)03d-%(levelname)s-%(filename)s.%(funcName)s()-l.%(lineno)d-%(message)s"
"""Logger format for the debug level."""

LOGGER_FORMAT = LOGGER_FORMAT_INFO if LOGGING_MODE == "INFO" else LOGGER_FORMAT_DEBUG
"""Logger format."""

FOO_MS_IP = str(os.environ.get("FOO_MS_IP", "localhost"))
"""Address Foo microservice"""

FOO_MS_PORT = str(os.environ.get("FOO_MS_PORT", "80"))
"""Port Foo microservice"""
