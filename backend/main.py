from fastapi import FastAPI

from backend.schemas import NoteCreate, NoteRead

app = FastAPI(title="BUBBLE")

notes: dict[int, NoteRead] = {}

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "alive"}
