from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from config import ACCESS_TOKEN_EXPIRE_MINUTES,SECRET_KEY,ALGORITHM
from passlib.context import CryptContext

def create_access_token(data:dict, expires_delta: timedelta=None):

    #We are making the copy of data so that we need not to made changes to original data
    to_encode= data.copy()

    #This checks if custom expiration of time is provided or not while calling the function 
    if expires_delta :
        expire =datetime.utcnow()+expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    #this add expiration to jwt token payload
    to_encode.update({"exp":expire})
    
    #this line of code encode payload
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return encode_jwt

#this function is used to verify the token
def verify_token(token:str):
    try:
        #this line decodes the jwt token and also verifies the signature of the token using the secret key and algorithm
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

        #this line gets subject field from the token and usually subject field contains username and userID
        username: str = payload.get("sub")

        #this line checks if username is present in the token subject field or not if not then it returns None if there is it returns the payload which contains the data of the user such as username and userID
        if username is None:
            return None
        return payload
    except JWTError:
        return None

#this line means use bcrypt algorithm for hashing the password and also it is used to verify the hashed password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#this if for password hashing 
def hash_password(password:str):
    return pwd_context.hash(password)

#this is for verifying hashed password 
def verify_password(plain_passowrd,hashed_password):
    return pwd_context.verify(plain_passowrd,hashed_password)

