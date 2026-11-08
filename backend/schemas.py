from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    model_config = ConfigDict(extra="forbid",
    str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=1000)


class NoteUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid",
    str_strip_whitespace=True)

    title: str | None = Field(default=None, min_length=1, max_length=100)
    content: str | None = Field(default=None, min_length=1, max_length=1000)
    
class NoteRead(BaseModel):
    id: int
    title: str
    content: str