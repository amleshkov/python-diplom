import pytest

from .conftest import USER_REGISTER_URL


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
        assert response.status_code == 201
        assert response.json()["Status"]

    def test_user_registration_with_missing_data(self, client):
        data = {}
        response = client.post(USER_REGISTER_URL, data)
        assert response.status_code == 400
        assert response.json()["Errors"] == "Не указаны все необходимые аргументы"

    def test_user_registration_with_existing_email(self, client, user):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "password": "onsUbPiOc@",
            "company": "Acme Inc.",
            "position": "Sales Manager",
        }
        response = client.post(USER_REGISTER_URL, data)
        assert response.status_code == 400
        assert "already exists" in response.json()["Errors"]["email"][0]

    def test_user_registration_with_invalid_password(self, client):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "password": "password",
            "company": "Acme Inc.",
            "position": "Sales Manager",
        }
        response = client.post(USER_REGISTER_URL, data)
        assert response.status_code == 400
        assert (
            response.json()["Errors"]["password"][0] == "This password is too common."
        )
