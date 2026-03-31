from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.blog_model import Blog
from app.schemas.blog_schemas import *
from app.crud.blog_crud import *
from app.db.database import get_db
from typing import List



router = APIRouter(prefix="/blogs" , tags=["Blogs"])

@router.get("/allblogs/", response_model=List[BlogResponse])
async def get_all(db:AsyncSession=Depends(get_db)):
    return await get_all_blog(db)

@router.post("/blog/",response_model=BlogCreate)
async def create(blog:BlogCreate ,db:AsyncSession=Depends(get_db)):
    return await create_blog(db,blog)

@router.get("/blog/{blog_id}", response_model=BlogResponse)
async def get_single_blog(blog_id:int, db:AsyncSession=Depends(get_db)):
    blog = await get_blog_by_id(blog_id,db)
    if not blog:
        raise HTTPException(status_code=400, detail=f"Blog with id {blog_id} not found")
    return blog

@router.put("/blog/{blog_id}", response_model=BlogResponse)
async def update(blog_id:int, blog_updated:BlogUpdate ,db:AsyncSession=Depends(get_db)):
    blog = await update_blog(blog_id,db,blog_updated)
    if not blog:
        raise HTTPException(status_code=400, detail=f"Blog with id {blog_id} not found")
    return blog

@router.delete("/blog/{blog_id}")
async def delete(blog_id:int, db:AsyncSession=Depends(get_db)):
    blog = await delete_blog(blog_id,db)
    if not blog:
        raise HTTPException(status_code=400, detail=f"Blog with id {blog_id} not found")
    return {
        "message":"blog deleted successfully"
    }



