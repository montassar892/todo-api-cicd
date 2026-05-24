import pytest
from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200

def test_get_todos_empty(client):
    res = client.get('/todos')
    assert res.status_code == 200
    assert res.get_json() == []

def test_add_todo(client):
    res = client.post('/todos', json={"task": "Buy milk"})
    assert res.status_code == 201

def test_add_todo_missing_task(client):
    res = client.post('/todos', json={})
    assert res.status_code == 400