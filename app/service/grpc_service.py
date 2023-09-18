from service.connectors import db_connector_service


def login(login: str, password: str) -> dict:
    """
    Method to log in user.

    Args:
        login (str): User login.
        password (str): User password.

    Returns:
        dict: User info.
    """
    dict_data: dict = db_connector_service.login(
        login=login,
        password=password,
    )
    return dict_data
