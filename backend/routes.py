from fastapi import APIRouter, HTTPException, Response

from backend import service
from backend.schemas import NoteCreate, NoteRead, NoteUpdate


router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("", response_model=NoteRead, status_code=201)
def create_note(data: NoteCreate):
    return service.create_note(data)


@router.get("", response_model=list[NoteRead])
def list_notes():
    return service.list_notes()


@router.get("/{note_id}", response_model=NoteRead)
def get_note(note_id: int):
    try:
        return service.get_note(note_id)
    except service.NoteNotFound:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        ) from None


@router.patch("/{note_id}", response_model=NoteRead)
def update_note(note_id: int, data: NoteUpdate):
    try:
        return service.update_note(note_id, data)
    except service.NoteNotFound:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        ) from None


@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: int):
    try:
        service.delete_note(note_id)
    except service.NoteNotFound:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        ) from None

    return Response(status_code=204)