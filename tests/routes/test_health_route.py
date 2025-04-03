import pytest
from flask import Flask
from flask.testing import FlaskClient
from datetime import datetime
from unittest.mock import patch
from src.routes.health_route import health_bp

@pytest.fixture
def app() -> Flask:
  app = Flask(__name__)
  app.register_blueprint(health_bp, url_prefix='/health')
  return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
  return app.test_client()

@patch('src.routes.health_route.health_dto.to_response')
def test_health_check(mock_to_response, client: FlaskClient):
  mock_response = {
    "status": "UP",
    "datetime": datetime.now()
  }
  mock_to_response.return_value = mock_response

  response = client.get('/health')

  assert response.status_code == 200
  assert response.json.get('status') == 'UP'
  mock_to_response.assert_called_once()
