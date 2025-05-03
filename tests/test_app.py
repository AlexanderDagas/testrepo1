# tests/test_app.py
import pytest
from app import app, tasks

@pytest.fixture(autouse=True)
def clear_tasks():
    tasks.clear()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_task_valid(client):
    """Test creating a task with valid data"""
    response = client.post('/tasks', json={'task': 'Learn GitHub Actions'})
    assert response.status_code == 201
    assert b"Learn GitHub Actions" in response.data

def test_create_task_invalid(client):
    """Test creating a task with invalid data"""
    response = client.post('/tasks', json={})
    assert response.status_code == 400

def test_get_tasks_empty(client):
    """Test getting tasks when none exist"""
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == {'tasks': []}

def test_get_tasks_with_data(client):
    """Test getting tasks after creating one"""
    client.post('/tasks', json={'task': 'Test task'})
    response = client.get('/tasks')
    assert response.status_code == 200
    assert 'Test task' in response.json['tasks']
