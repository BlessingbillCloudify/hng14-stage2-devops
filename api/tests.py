import pytest
from fastapi.testclient import TestClient
from main import app
import unittest.mock as mock

client = TestClient(app)

@mock.patch("main.r") # This "Mocks" (fakes) the Redis connection
def test_create_job(mock_redis):
    mock_redis.lpush.return_value = 1
    mock_redis.hset.return_value = 1
    
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()

@mock.patch("main.r")
def test_get_job_status(mock_redis):
    # Fake a successful status return
    mock_redis.hget.return_value = "queued"
    
    response = client.get("/jobs/test-id")
    assert response.status_code == 200
    assert response.json()["status"] == "queued"

@mock.patch("main.r")
def test_health_check(mock_redis):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
