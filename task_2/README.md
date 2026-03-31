# Generating JWT authentication using fastAPI in python 
   This task is to implement JWT authentication .IT allows user to log in receive
# Tech Stack 
  -python <br>
  -FastAPI <br>
  -Uvicorn <br>
  -python-jose (for jwt handeling) <br>
  -passlib (for password hashing) <br>
# Steps
 1. Create the virtual environment
 2. Activate virtual environment
 3. Create utils.py file and it handles following thigs: <br>
    -> Create access token <br>
    -> Verify token <br>
    -> generate hash password <br>
    -> verify hash password and plain password are same <br>
 4. Create config.py file and it stores all the configuration setting like secret_key, algorithm, and access_token_expire_minutes and secret_keys loaded from .env file
 5. Create main.py file and it handles following things: <br>
    -> Create login and register API end point <br>
    -> Define the simple schema for user data <br>
    -> And also define endpoint which needs authentication to access <br>
    

##
