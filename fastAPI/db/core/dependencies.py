from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from utils.database_utils import get_db
from jose import JWTError, jwt
from fastapi import HTTPException, status
from models import User
from sqlalchemy import select
from utils.auth_utils import oauth2_scheme
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

'''this function does 3 things:
  1.Gets token from request header
  2.Gets DB session
  3.Validates user
'''
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    token = credentials.credentials

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    
    try:
        # takes jwt token from the request and verify using secret_key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        #gets the user name form the token
        username: str = payload.get("sub")

        #if username is not valid based on the token then throw credentials_exception
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception
    return user

async def get_current_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.is_admin==True:
        return current_user
    raise HTTPException(status_code=403, detail="Admin privileges required")
    