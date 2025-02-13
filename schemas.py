# backend/schemas.py
from pydantic import BaseModel, ConfigDict

# Pydantic schemas for request/response
class TodoCreate(BaseModel):
    title: str

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

    model_config = ConfigDict(from_attributes=True)