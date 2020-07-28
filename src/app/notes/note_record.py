from pydantic import BaseModel, Field
from .note import Note

class NoteRecord(Note):
    id: int
