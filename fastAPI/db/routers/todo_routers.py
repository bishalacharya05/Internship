from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.dependencies import get_current_user,get_current_admin_user
import models
import schemas
from utils.database_utils import get_db
from schemas import todoResponse
from typing import List
from crud import todo_crud

router=APIRouter()

#creating todo

@router.post("/todo",response_model=schemas.todoResponse)
async def post_todo(todo_data:schemas.todocreate, db:AsyncSession=Depends(get_db),current_user: models.User = Depends(get_current_user)):
    return await todo_crud.create_todo(db,todo_data,current_user.id)

#get all todo
@router.get("/todo",response_model=List[todoResponse])
async def get_todo(db: AsyncSession = Depends(get_db)):
    return await todo_crud.get_todo(db)


#get a single todo
@router.get("/todo/{todo_id}",response_model=schemas.todoResponse)
async def get_todo_by_id(todo_id:int, db:AsyncSession= Depends(get_db)):
    db_todo = await todo_crud.get_todo_by_id(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return db_todo

#update a todo
@router.put("/todo/{todo_id}",response_model=schemas.todoResponse)
async def update_todo(todo_id:int, updated_todo:schemas.todocreate, db:AsyncSession=Depends(get_db)):
    db_todo = await todo_crud.update_todo(db, updated_todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return db_todo

#delete function for todo
@router.delete("/todo/{todo_id}")
async def delete_todo(todo_id:int, db:AsyncSession = Depends(get_db)):
    db_todo= await todo_crud.delete_todo(db,todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return {
        "message":"Successfully deleted"
    }

#create todo for a user
# @router.post("/users/{user_id}/todo", response_model=schemas.todoResponse)
# async def create_todo_for_user(user_id:int, todo_data:schemas.todocreate, db:AsyncSession = Depends(get_db),current_user: models.User = Depends(get_current_user)):
#     return await todo_crud.create_todo(db, todo_data, user_id)


