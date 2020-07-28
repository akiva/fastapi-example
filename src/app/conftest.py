import pytest
from starlette.testclient import TestClient
from .main import app
from .database.database import TestingSessionLocal
import os

# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()

@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('DATABASE_URL', os.getenv('TEST_DATABASE_URL'))

@pytest.fixture(scope='module')
def test_app():
    # app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
