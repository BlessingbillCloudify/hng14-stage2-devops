import sys
import os
# This specific line is what you are missing to fix the "No module named main" error:
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from main import app 
import unittest.mock as mock

client = TestClient(app)

@mock.patch("main.r")
def test_create_job(mock_redis):
    mock_redis.lpush.return_value = 1
    mock_redis.hset.return_value = 1
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()

@mock.patch("main.r")
def test_get_job_status(mock_redis):
    mock_redis.hget.return_value = "queued"
    response = client.get("/jobs/test-id")
    assert response.status_code == 200
    assert response.json()["status"] == "queued"

@mock.patch("main.r")
def test_health_check(mock_redis):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
