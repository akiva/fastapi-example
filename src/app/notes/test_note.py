from pytest import raises
from .note import Note

def test_note_missing_title_and_description():
    '''Note requires a title and description'''
    with raises(Exception) as e:
        Note()
    assert e.value.errors() == [
        {
            'loc': ('title',),
            'msg': 'field required',
            'type': 'value_error.missing',
        },
        {
            'loc': ('description',),
            'msg': 'field required',
            'type': 'value_error.missing',
        },
    ]

def test_note_title_and_description_too_short():
    '''Note title must be longer than 3 characters in length'''
    '''and description'''
    with raises(Exception) as e:
        Note(title='A', description='B')
    assert e.value.errors() == [
        {
            'loc': ('title',),
            'msg': 'ensure this value has at least 3 characters',
            'type': 'value_error.any_str.min_length',
            'ctx': {'limit_value': 3 },
        },
        {
            'loc': ('description',),
            'msg': 'ensure this value has at least 3 characters',
            'type': 'value_error.any_str.min_length',
            'ctx': {'limit_value': 3 },
        },
    ]

def test_note_title_and_description_too_long():
    with raises(Exception) as e:
        title=f'{"h" * 51}'
        description=f'{"h" * 51}'
        Note(title=title, description=description)
    assert e.value.errors() == [
        {
            'loc': ('title',),
            'msg': 'ensure this value has at most 50 characters',
            'type': 'value_error.any_str.max_length',
            'ctx': {'limit_value': 50},
        },
        {
            'loc': ('description',),
            'msg': 'ensure this value has at most 50 characters',
            'type': 'value_error.any_str.max_length',
            'ctx': {'limit_value': 50},
        },
    ]

def test_new_note():
    note = Note(title='Foo', description='Bar')
    assert note.title == 'Foo'
    assert note.description == 'Bar'
    assert note.dict() == {'description': 'Bar', 'title': 'Foo'}
