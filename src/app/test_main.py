import pytest
from fastapi.testclient import TestClient
from .main import app

def test_meta():
    # TODO Compare to values in settings or .env
    assert app.title == 'FastAPI example'
    assert app.description == 'My example FastAPI CRUD application'
    assert app.version == '0.1.0'

@pytest.mark.skip(reason='Find a way to confirm mounted routers')
def test_mounted_routers():
    pass

@pytest.mark.skip(reason='Find a way of testing this')
def test_startup():
    pass

@pytest.mark.skip(reason='Find a way of testing this')
def test_shutdown():
    pass
