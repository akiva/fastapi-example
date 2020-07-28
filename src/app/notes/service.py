from .note import Note
from ..database import models
from sqlalchemy.orm import Session

async def post(db: Session, payload: Note):
    db_item = models.Note(**payload.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
    # query = Note.insert().values(
    #     title=payload.title,
    #     description=payload.description
    # )
    # return await database.execute(query=query)

async def get(db: Session, id: int):
    return db.query(models.Note).filter(models.Note.id == id).first()
    # query = Note.select().where(id == notes.c.id)
    # return await database.fetch_one(query=query)

async def list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()
    # query = Note.select()
    # return await database.fetch_all(query=query)

async def put(db: Session, id: int, payload: Note):
    # return db.query(models.Note).offset(skip).limit(limit).all()
    query = (
        Note
            .update()
            .where(id == notes.c.id)
            .values(title=payload.title, description=payload.description)
            .returning(notes.c.id)
    )
    return await db.execute(query=query)

async def delete(db: Session, id: int):
    return db.query(models.Note).delete().where(id == notes.c.id)
    # query = Note.delete().where(id == notes.c.id)
    # return await database.execute(query=query)
