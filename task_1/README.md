# Sending mail Using FastAPI

This a fastAPI-based backend application that allows users to send emails via an API.
It supports sending emails with subject. message body and recipient address.
## tech Stack
 -FastAPI <br>
 -Python <br>
 -SMTP(for sending emails)<br>
 -Uvicorn
 ## Steps
 1. Create virtual environment:
 2. activate virtual environment
 3. install dependencies
 4. create main.py file
 5. Create API endpoints for handeling email request <br>
     -> we have to configure the email configurations like: <br>
    {
       EMAIL_HOST=smtp.gmail.com <br>
       EMAIL_PORT=587 <br>
       EMAIL_USER=your-email@gmail.com <br>
       EMAIL_PASSWORD=password 
    } <br>
    -> Define schemas for sendong mail <br>
    -> define background task as sending mail <br>
    -> Create http POST method for sending mail <br>
    -> All the confidentials credentials should save on .env file
## Screenshots
   1. Post request
      
      <img width="1830" height="872" alt="image" src="https://github.com/user-attachments/assets/a5ead51e-4160-4359-9c13-8b83abc59a2a" />
   3. Responses
      
      <img width="1802" height="861" alt="image" src="https://github.com/user-attachments/assets/13aadc1f-1d9d-4ab4-8fb0-a7d842ef3d55" />
   4. Successful email

      <img width="615" height="339" alt="image" src="https://github.com/user-attachments/assets/306c743d-2dab-4737-84fa-dd2e5ba455b3" />
## Author
Bishal Acharya
       



    

       


