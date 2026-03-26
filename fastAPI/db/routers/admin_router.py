from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select  
from sqlalchemy.ext.asyncio import AsyncSession
from core.dependencies import get_current_admin_user
import schemas
import models
from utils.database_utils import get_db
from schemas.todo_schema import todoResponse
from typing import List

router=APIRouter()

#read todos for a user (admin only)
@router.get("/users/{user_id}/todos", response_model=List[schemas.todoResponse])
async def read_todos_for_user(user_id:int, db:AsyncSession = Depends(get_db),current_user: models.User = Depends(get_current_admin_user)):
    result = await db.execute(select(models.Todo).where(models.Todo.owner_id == user_id))
    todos = result.scalars().all()
    if not todos:
        raise HTTPException(status_code=404, detail="No todos found for this user")
    return todos

