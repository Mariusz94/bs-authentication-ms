import pytest
import service.connectors.authentication_service as authentication_service


@pytest.mark.parametrize(
    "login,password",
    [("7654", "pass_1"), ("12344", "pass_2")],
)
def test_login(login: str, password: str):
    data: dict = authentication_service.login(login, password)

    assert "id" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "phone_number" in data
    assert "address" in data
    assert "login" in data
