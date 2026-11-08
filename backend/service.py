from itertools import count

from backend.schemas import NoteCreate, NoteRead, NoteUpdate


class NoteNotFound(Exception):
    pass


_notes: dict[int, NoteRead] = {}
_ids = count(start=1)


def create_note(data: NoteCreate) -> NoteRead:
    note = NoteRead(
        id=next(_ids),
        **data.model_dump(),
    )
    _notes[note.id] = note
    return note


def list_notes() -> list[NoteRead]:
    return list(_notes.values())


def get_note(note_id: int) -> NoteRead:
    note = _notes.get(note_id)

    if note is None:
        raise NoteNotFound(note_id)

    return note


def update_note(note_id: int, data: NoteUpdate) -> NoteRead:
    current = get_note(note_id)
    changes = data.model_dump(exclude_unset=True)

    updated = NoteRead(
        **(current.model_dump() | changes)
    )

    _notes[note_id] = updated
    return updated


def delete_note(note_id: int) -> None:
    note = _notes.get(note_id)

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        ) from None
    else: 
        del _notes[note_id]
        return Response(status_code=204)
