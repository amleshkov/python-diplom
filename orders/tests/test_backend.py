import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
class TestRegisterAccount:
    def test_user_registration(self, client):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "password": "onsUbPiOc@",
            "company": "Acme Inc.",
            "position": "Sales Manager",
        }
        url = "/api/v1/user/register"
        response = client.post(url, data)
        assert response.status_code == 200
        assert response.json()["Status"]
