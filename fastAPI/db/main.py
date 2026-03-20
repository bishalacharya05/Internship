from fastapi import FastAPI
from utils.database_utils import create_tables
from routers import user_routers, todo_routers ,admin_router

app=FastAPI(title="todo API")

app.include_router(user_routers.router , prefix="/users", tags=["users"])
app.include_router(todo_routers.router, prefix="/todos", tags=["todos"])
app.include_router(admin_router.router, prefix="/admin", tags=["admin"])

@app.on_event("startup")
async def startup():
    await create_tables()


