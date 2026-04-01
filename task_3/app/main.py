from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.routes import employee_router

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(employee_router.routers)