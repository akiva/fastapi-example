from . import service
from .note import Note
from .note_record import NoteRecord
from fastapi import Depends, APIRouter, HTTPException, Path
from typing import List
from sqlalchemy.orm import Session
from ..database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=NoteRecord, status_code=201)
async def create_note(payload: Note, db: Session = Depends(get_db),):
    note_id = await service.post(db, payload)
    response_object = {
        'id': note_id,
        'title': payload.title,
        'description': payload.description,
    }
    return response_object

@router.get('/{id}/', response_model=NoteRecord)
async def read_note(
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
):
    note = await service.get(db, id)
    if not note:
        raise HTTPException(status_code=404, detail='Note not found')
    return note

@router.get('/', response_model=List[NoteRecord])
async def read_all_notes(db: Session = Depends(get_db),):
    return await service.list(db)

@router.put('/{id}/', response_model=NoteRecord)
async def update_note(
    payload: Note,
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
):
    note = await service.get(db, id)
    if not note:
        raise HTTPException(status_code=404, detail='Note not found')
    note_id = await service.put(db, id, payload)
    response_object = {
        'id': note_id,
        'title': payload.title,
        'description': payload.description,
    }
    return response_object

@router.delete('/{id}/', response_model=NoteRecord)
async def delete_note(
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
):
    note = await service.get(db, id)
    if not note:
        raise HTTPException(status_code=404, detail='Note not found')
    await service.delete(db, id)
    return note
