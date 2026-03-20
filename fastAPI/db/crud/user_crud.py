from sqlalchemy.ext.asyncio import AsyncSession
import models
import schemas
from utils.auth_utils import hash_password, create_access_token
from sqlalchemy import select
from fastapi import HTTPException
from utils.auth_utils import verify_password

#function for registering user
async def register_user(db:AsyncSession,user_data:schemas.UserCreate,username:str):
    result = await db.execute(select(models.User).where(models.User.username == username))
    user = result.scalars().first()
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_pw= hash_password(user_data.password)
    new_user = models.User(
        username=user_data.username,
        email=user_data.email,
        password=hashed_pw,
        is_admin=user_data.is_admin
        )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {
        "message":"user registered successfully"
    }

#function to login user
async def login_user(db:AsyncSession, username:str, password:str):
    result = await db.execute(select(models.User).where(models.User.username == username))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token = create_access_token({"sub": user.username,
                                        "is_admin": user.is_admin})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
