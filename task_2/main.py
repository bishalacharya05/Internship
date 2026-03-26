from fastapi import FastAPI,Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from utils import hash_password, verify_password,create_access_token, verify_token
from datetime import timedelta
from config import ACCESS_TOKEN_EXPIRE_MINUTES




app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

fake_user_db:dict[str,dict]={}

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    username:str



@app.post("/register",response_model=UserOut)
def register_user(user: UserRegister):
    if user.username in fake_user_db:
        return {
            "message":"user already exists"
        }
    hashed = hash_password(user.password)
    fake_user_db[user.username] = {"username": user.username, "hashed_password":hashed}
    return {"username": user.username}

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        return {
            "message":"invlaid authentication"
        }
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
     )
    return {"access_token":token , "token_type":"bearer"}

@app.get("/me",response_model=UserOut)
def read_current_user(token:str = Depends(oauth2_scheme)):
    payload= verify_token(token)
    if payload is None:
        return {
            "message":"invalid or expired token"
        }
    return {
        "username":payload.get("sub")
    }
