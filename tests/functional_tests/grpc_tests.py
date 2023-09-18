import os
import sys

import grpc
import pytest
import service.connectors.foo_service as foo_service

from default_msg import default_pb2
from foo_msg import foo_pb2


def test_foo_method_1():
    data: dict = foo_service.foo_method_1()

    assert data["foo_response"] == "Sample response"


def test_foo_method_2():
    data: dict = foo_service.foo_method_2()

    assert len(data) == 0


def test_foo_method_download_file():
    foo_file, data = foo_service.foo_method_download_file()

    assert data["foo_file_name"] == "sample_name.jpg"


def test_foo_method_upload_file():
    file_path = os.path.join(os.getcwd(),"tests", "assets", "images", "python_img.jpeg")

    with open(file_path, "rb") as image:
        f = image.read()
        image_byte = bytes(f)

    data: dict = foo_service.foo_method_upload_file(foo_file=image_byte)

    assert data["status"] == "SUCCESS"
