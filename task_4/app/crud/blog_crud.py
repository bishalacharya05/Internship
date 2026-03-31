from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.blog_model import Blog
from app.schemas.blog_schemas import *



async def create_blog(db: AsyncSession, blog_data: BlogCreate):
    new_blog = Blog(**blog_data.model_dump())
    db.add(new_blog)
    await db.commit()
    await db.refresh(new_blog)
    return new_blog

async def get_all_blog(db:AsyncSession):
    blogs = await db.execute(select(Blog))
    result= blogs.scalars().all()
    return result

async def get_blog_by_id(blog_id:int , db:AsyncSession):
    blog = await db.execute(select(Blog).where(blog_id==Blog.id))
    result = blog.scalar_one_or_none()
    return result

async def update_blog(blog_id:int,db:AsyncSession, blog:BlogUpdate):
    db_blog = await db.execute(select(Blog).where(blog_id==Blog.id))
    result = db_blog.scalar_one_or_none()

    if result:
        #(exclude_unset=True) ignores fields that were not provided in the request.
        for key, value in blog.model_dump(exclude_unset=True).items():
            setattr(result,key,value)
        await db.commit()
        await db.refresh(result)
        return result
    else:
        return {
            "message":f"User with the id {blog_id} not found "
        }
    
async def delete_blog(blog_id:int, db:AsyncSession):
    db_blog = await db.execute(select(Blog).where(blog_id==Blog.id))
    result = db_blog.scalar_one_or_none()
    if result:
        await db.delete(result)
        await db.commit()
        return result
    else:
        return {
            "message":f"User with the id {blog_id} not found "
        }
 
        
        
    
