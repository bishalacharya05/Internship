from pydantic import BaseModel
from datetime import datetime


class BlogBase(BaseModel):
    title:str
    description:str
    author:str
    created_date:datetime | None

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BlogBase):
    pass

class BlogResponse(BaseModel):
    title:str
    description:str
    author:str

    class Config:
        from_attributes = True