from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.blog_model import Blog
from app.schemas.blog_schemas import *
from app.crud.blog_crud import *
from app.db.database import get_db
from typing import List
from redis_client import redis_client
import json

router = APIRouter(prefix="/blogs" , tags=["Blogs"])

@router.get("/allblogs/", response_model=List[BlogResponse])
async def get_all(db:AsyncSession=Depends(get_db)):

    #Cache_key is unique identifier of redis cache
    cache_key = "all_blogs"
    
    #In this we are trying to get the data from the cache_key
    cached_data = redis_client.get(cache_key)

    #if cached_data is valid then we convert the cached data i.e json string into python list/dictionary and return the response
    if cached_data:
        print("CACHE HIT")
        return json.loads(cached_data)
    print("CACHE MISS")
    #and if the data is not stored into cache get the data from db using get_all_blog() crud function
    posts = await get_all_blog(db)

    #Then the post i.e is obtained from the db contains SQL alchemy objects and we have to convert it into the dictionary and because redis cannot store redis directly
    posts_data = [
    {c.name: getattr(post, c.name) for c in post.__table__.columns}
    for post in posts
    ]

    #And at last we store data into redis cache
    redis_client.setex(cache_key, 300, json.dumps(posts_data, default=str))
    return posts_data

@router.post("/blog/",response_model=BlogCreate)
async def create(blog:BlogCreate ,db:AsyncSession=Depends(get_db)):
    return await create_blog(db,blog)

@router.get("/blog/{blog_id}", response_model=BlogResponse)
async def get_single_blog(blog_id:int, db:AsyncSession=Depends(get_db)):
    cache_key = f"blog_{blog_id}"
    cache_data = redis_client.get(cache_key)
    if cache_data:
        print("CACHE HIT")
        return json.loads(cache_data)
    print("CACHE MISS")
    post = await get_blog_by_id(blog_id,db)
    post_data = {c.name: getattr(post, c.name) for c in post.__table__.columns}
    redis_client.setex(cache_key,300, json.dumps(post_data,default=str))
    return post_data

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



