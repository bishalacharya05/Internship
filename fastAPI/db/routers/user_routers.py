from typing import List

from fastapi import APIRouter, Depends,HTTPException
import schemas
from sqlalchemy.ext.asyncio import AsyncSession
from utils.database_utils import get_db
from core.dependencies import get_current_user
from crud import user_crud,todo_crud
from sqlalchemy import select
import models
import schemas
router = APIRouter()


@router.post("/register")
async def register(user_data:schemas.UserCreate, db:AsyncSession = Depends(get_db)):
    await user_crud.register_user(db,user_data,user_data.username)
    return {
        "message":"user registered successfully"
    }

@router.post("/login")
async def login(user_data:schemas.UserLogin, db:AsyncSession = Depends(get_db)):
    return await user_crud.login_user(db, user_data.username, user_data.password)


@router.get("/all_todo/{user_id}/todos",response_model=List[schemas.todoResponse])
async def get_all_todo_by_UserID(user_id:int,db:AsyncSession=Depends(get_db), current_user:models.User=Depends(get_current_user)):
    result = await db.execute(select(models.Todo).where(models.Todo.owner_id == user_id))
    todos = result.scalars().all()
    if not todos:
        raise HTTPException(status_code=404, detail="No todos found for this user")
    return todos

@router.get("/specific_todo/{user_id}/{todo_id}/todo",response_model=schemas.todoResponse)
async def get_todo_by_userID_and_todoID(user_id:int,todo_id:int, db:AsyncSession=Depends(get_db),current_user:models.User=Depends(get_current_user)):
    result = await db.execute(select(models.Todo).where(models.Todo.owner_id == user_id, models.Todo.id == todo_id))
    todo= result.scalars().first()
    if not todo:
        raise HTTPException(status_code=404, detail="No todo found for this user")
    return todo

@router.put("/todo/{user_id}/{todo_id}", response_model=schemas.todoResponse)
async def update_todo_by_userID(todo_id: int, todo_data: schemas.todocreate, user_id: int, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    # Ensureing the todo exists and belongs to this user
    todo = await todo_crud.get_todo_by_id(db, todo_id)
    if not todo or todo.owner_id != user_id:
        raise HTTPException(status_code=404, detail="Todo not found for this user")
    updated_todo = await todo_crud.update_todo(db, todo_data, todo_id)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Unable to update todo")
    return updated_todo

@router.delete("/todo/{user_id}")
async def delete_to_by_userID(user_id:int, db:AsyncSession =Depends(get_db),create_user:AsyncSession =Depends(get_current_user)):
    todos = await todo_crud.delete_todo_by_user(db,user_id)
    if not todos:
        raise HTTPException(status_code=404, detail="Unable to update todo")
    return todos