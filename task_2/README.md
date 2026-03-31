# Generating JWT authentication using fastAPI in python 
   This task is to implement JWT authentication .IT allows user to log in receive
## Tech Stack 
  -python <br>
  -FastAPI <br>
  -Uvicorn <br>
  -python-jose (for jwt handeling) <br>
  -passlib (for password hashing) <br>
## Steps
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
    

## Screenshots
1.API endpoints 
    <img width="1875" height="869" alt="image" src="https://github.com/user-attachments/assets/19a5c32c-f86c-4ff9-9d8a-6643c9677aaf" />
2.Register request body
    <img width="1853" height="845" alt="image" src="https://github.com/user-attachments/assets/d4d59b6e-0dc0-4173-b3a8-b50b86d05d66" />
3.Register response body
    <img width="1825" height="789" alt="image" src="https://github.com/user-attachments/assets/81c838de-ae03-4537-8c15-7d5b636e123f" />
4.Login request body
    <img width="1877" height="912" alt="image" src="https://github.com/user-attachments/assets/33911bc5-aecd-460b-b33e-b7408574fde0" />
5.Login response body
    <img width="1835" height="864" alt="image" src="https://github.com/user-attachments/assets/33d297a0-aec7-4d71-b9d1-f74e727c0286" />
6.Authorization Swagger UI
    <img width="881" height="772" alt="image" src="https://github.com/user-attachments/assets/15dc5e2c-8b9b-488d-a9ae-1a2776057d77" /> <br>
7.Accessing API endpoint after authentication
    <img width="1862" height="863" alt="image" src="https://github.com/user-attachments/assets/3cc60689-f8d4-43b8-bdd6-133f3facfb82" />
8.Authentication after authorization
    <img width="1852" height="887" alt="image" src="https://github.com/user-attachments/assets/fdb6758e-2257-4d18-bd80-8da798501719" />
9.Response without authentication
    <img width="1862" height="879" alt="image" src="https://github.com/user-attachments/assets/3a0279ac-210b-4e24-a67d-097af221d50a" />

## Author 
Bishal Acharya




    




