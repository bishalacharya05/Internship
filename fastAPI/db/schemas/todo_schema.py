from pydantic import BaseModel,Field


class todobase(BaseModel):
    id:int
    title: str
    description: str
    completed: bool

class todocreate(BaseModel):
    title: str
    description: str
    completed: bool

class todoupdate(BaseModel):
    title: str
    description: str
    completed: bool

class todoResponse(todobase):
    id:int
    owner_id:int

    class Config:
        form_attributes = True