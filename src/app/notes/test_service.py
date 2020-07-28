import json
import pytest
from . import service
from .note import Note

# TODO Find a better way to test with mocking the DB

@pytest.mark.skip(reason='Find a way of testing this')
def test_post():
    # payload: Note
    pass

@pytest.mark.skip(reason='Find a way of testing this')
def test_get():
    # id: int
    pass

@pytest.mark.skip(reason='Find a way of testing this')
def test_list():
    pass

@pytest.mark.skip(reason='Find a way of testing this')
def test_put():
    # id: int
    # payload: Note
    pass

@pytest.mark.skip(reason='Find a way of testing this')
def test_delete():
    # id: int
    pass
