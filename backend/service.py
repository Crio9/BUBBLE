
from backend.schemas import NoteCreate, NoteUpdate
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.models import Note



class NoteNotFound(Exception):
    pass

def create_note(db: Session, data: NoteCreate) -> Note:
    note = Note(**data.model_dump())

    db.add(note)
    db.commit()
    db.refresh(note)

    return note


def list_notes(db: Session) -> list[Note]:
    statement = select(Note).order_by(Note.id)
    return list(db.scalars(statement).all())


def get_note(db: Session, note_id: int) -> Note:
    note = db.get(Note, note_id)

    if note is None:
        raise NoteNotFound(note_id)

    return note

def update_note(note_id: int, data: NoteUpdate, db: Session) -> Note:
    note = db.get(Note, note_id)

    if note is None:
        raise NoteNotFound(note_id)

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(note, key, value)    
    db.commit()
    db.refresh(note)

    return note

    



def delete_note(note_id: int, db: Session) -> None:
    note = get_note(db, note_id)
    db.delete(note)
    db.commit()
