from fastapi import FastAPI
from contextlib import asynccontextmanager


from backend import models
from backend.routes import router as notes_router
from backend.database import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()

app = FastAPI(title="BUBBLE", lifespan=lifespan)
app.include_router(notes_router)



@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "alive"}
