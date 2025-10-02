import pytest
from rest_framework.test import APIClient

USER_REGISTER_URL = "/api/v1/user/register"
USER_CONFIRM_URL = "/api/v1/user/register/confirm"


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user(client):
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "password": "onsUbPiOc@",
        "company": "Acme Inc.",
        "position": "Sales Manager",
    }
    client.post(USER_REGISTER_URL, data)
