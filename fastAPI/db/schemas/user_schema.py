from pydantic import BaseModel,Field
from typing import Annotated

class UserCreate(BaseModel):
    username : Annotated[str,Field(max_length=255,description="Username",example="ramesh")]
    email:Annotated[str,Field(max_length=255,description="Username",example="ramesh@gmail.com")]
    password:Annotated[str,Field(max_length=72)]
    is_admin: Annotated[bool, Field(default=False, description="Is the user an admin?")] = False

class UserLogin(BaseModel):
    username : str
    password:str