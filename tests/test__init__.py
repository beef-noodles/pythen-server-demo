import pytest
from flask import Flask
from src import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_app_creation(app):
    assert isinstance(app, Flask)
    assert app.config["TESTING"] is True


def test_health_route(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200


def test_cases_route(client):
    response = client.get("/api/v1/cases")

    assert response.status_code == 401


def test_authentication(client):
    headers = {"X-api-key": "invalid_token"}

    response = client.get("/api/v1/cases", headers=headers)

    assert response.status_code == 401
    assert response.json == {"message": "Access denied: Invalid or expired token."}
