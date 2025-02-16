# backend/schemas.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# Pydantic schemas for request/response
class TodoCreate(BaseModel):
    title: str
    
class TodoPatch(BaseModel):
    title: Optional[str]
    completed: Optional[bool]
    
class TodoResponse(BaseModel):
    id: int
    title: str
    created_at: datetime
    completed: bool

    model_config = ConfigDict(from_attributes=True)