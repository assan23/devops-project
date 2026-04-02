import pytest
from app import app

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_about_page():
    response = app.test_client().get('/about')
    assert response.status_code == 200

def test_api_tasks():
    response = app.test_client().get('/api/tasks')
    assert response.status_code == 200