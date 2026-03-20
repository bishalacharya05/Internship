from fastapi import APIRouter, Depends
import schemas
from sqlalchemy.ext.asyncio import AsyncSession
from utils.database_utils import get_db
from crud import user_crud

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

