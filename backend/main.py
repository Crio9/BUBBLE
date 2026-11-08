from fastapi import FastAPI

app = FastAPI(title="BUBBLE")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
