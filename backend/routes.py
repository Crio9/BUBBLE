from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import service
from backend.database import get_db
from backend.schemas import NoteCreate, NoteRead, NoteUpdate


router = APIRouter(prefix="/notes", tags=["Notes"])
DbSession = Annotated[Session, Depends(get_db)]


@router.post("", response_model=NoteRead, status_code=201)
def create_note(data: NoteCreate, db: DbSession):
    return service.create_note(db, data)

@router.get("", response_model=list[NoteRead])
def list_notes(db: DbSession):
    return service.list_notes(db)


@router.get("/{note_id}", response_model=NoteRead)
def get_note(note_id: int, db: DbSession):
    try:
        return service.get_note(db, note_id)
    except service.NoteNotFound:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        ) from None


@router.patch("/{note_id}", response_model=NoteRead)
def update_note(note_id: int, data: NoteUpdate, db: DbSession):
    try:
        return service.update_note(note_id, data,db)
    except service.NoteNotFound:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        ) from None


@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: int,db: DbSession):
    try:
        service.delete_note(note_id,db)
    except service.NoteNotFound:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        ) from None

    return Response(status_code=204)
