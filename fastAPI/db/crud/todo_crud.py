from sqlalchemy.ext.asyncio import AsyncSession
import models,schemas
from sqlalchemy import select


#function for creating todo
async def create_todo(db: AsyncSession, todo_data: schemas.todocreate,user_id:int):
    new_todo = models.Todo(**todo_data.model_dump(), owner_id=user_id)
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo

#function for fetching todo
async def get_todo(db:AsyncSession):
    result = await db.execute(select(models.Todo))
    return  result.scalars().all()

#function to get a single todo by ID
async def get_todo_by_id(db:AsyncSession, todo_id:int):
     result =await db.execute(select(models.Todo).where(models.Todo.id == todo_id))
     return result.scalars().first()
     

#function to update todo by ID
async def update_todo(db:AsyncSession, updated_todo:schemas.todocreate, todo_id:int):
    result =  await db.execute(select(models.Todo).where(models.Todo.id == todo_id))
    todo = result.scalars().first()
    if todo:
        todo.title=updated_todo.title
        todo.completed = updated_todo.completed
        todo.description = updated_todo.description
        await db.commit()
        await db.refresh(todo)
    return todo

#function to delete todo by ID
async def delete_todo(db:AsyncSession, todo_id:int):
    result = await db.execute(select(models.Todo).where(models.Todo.id == todo_id))
    todo = result.scalars().first()
    if todo:
        await db.delete(todo)
        await db.commit()
    return todo