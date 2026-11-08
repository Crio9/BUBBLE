from fastapi import FastAPI

from backend.schemas import NoteCreate, NoteRead

app = FastAPI(title="BUBBLE")

notes: dict[int, NoteRead] = {}

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "alive"}

@app.get("/double")
def doubling(x : int = 1) -> dict[str,int]:
    return{"result":x*2}

@app.post("/notes", response_model=NoteRead)
def create_note(note: NoteCreate):
    note_id = len(notes) + 1
    note_read = NoteRead(id=note_id, title=note.title, content=note.content)
    notes[note_id] = note_read
    return note_read

@app.get("/notes", response_model=list[NoteRead])
def read_note():
    return list(notes.values())