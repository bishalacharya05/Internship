from fastapi import FastAPI
from app.db.database import engine
from app.models.blog_model import Base
from app.api.routers.router_blog import router as blog_router


app= FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(blog_router)
