from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.routes import employee_router
from app.models.employee_model import Employee

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(employee_router.routers)