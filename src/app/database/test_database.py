import pytest
from fastapi.testclient import TestClient
from databases import Database
from sqlalchemy.orm import sessionmaker
from .database import (
    Base,
    DATABASE_URL,
    database,
    engine,
    SessionLocal,
)

@pytest.mark.skip(reason='Find a way of testing this')
def test_base():
    pass

def test_database_url():
    assert DATABASE_URL != ''
    assert DATABASE_URL[:10] == 'postgresql'

def test_database():
    assert isinstance(database, Database)

@pytest.mark.skip(reason='Find a way of testing this')
def test_engine():
    pass

def test_sessionlocal():
    assert isinstance(SessionLocal, sessionmaker)
