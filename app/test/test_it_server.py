#!/usr/bin/python

import pytest
from app.src.server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check_api(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert "UP" == data["status"]


def test_create_person_api(client):
    response = client.post('/people')
    assert response.status_code == 200
    data = response.get_json()
    assert "John Doe" == data["name"]
    assert "id" in data
    assert data["id"] is not None
