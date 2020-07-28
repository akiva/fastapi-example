from pytest import raises
from .note import Note
from .note_record import NoteRecord

def test_note_record_requires_note_db_record():
    '''NoteRecord requires a Note record'''
    with raises(Exception) as e:
        note = {'title': 'Foo', 'description': 'Bar'}
        NoteRecord(**note)
    assert e.value.errors() == [
        {
            'loc': ('id',),
            'msg': 'field required',
            'type': 'value_error.missing',
        },
    ]

def test_note_record():
    '''NoteRecord decorates Note with database ID'''
    input = {'id': 1, 'title': 'Foo', 'description': 'Bar'}
    note_record = NoteRecord(**input)
    assert note_record.id == 1
    assert note_record.title == 'Foo'
    assert note_record.description == 'Bar'
    assert note_record.dict() == {
        'id': 1,
        'description': 'Bar',
        'title': 'Foo'
    }
