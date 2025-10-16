import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint_returns_200():
    """Test that root endpoint returns 200 status"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_users_endpoint_returns_200():
    """Test that users endpoint returns 200 status and has data structure"""
    response = client.get("/users")
    assert response.status_code == 200
    # Check it returns JSON with some data structure
    assert isinstance(response.json(), dict)

def test_metrics_endpoint_returns_200():
    """Test that metrics endpoint returns 200 status"""
    response = client.get("/metrics")
    assert response.status_code == 200
    # Metrics should return text/plain with prometheus data
    assert "text/plain" in response.headers.get("content-type", "")
