from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
import os
from dotenv import load_dotenv
import logging

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

#email configuration
config= ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT= int(os.getenv("MAIL_PORT",587)),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

#pydantic model for email data
class Email_schema(BaseModel):
    email : EmailStr
    subject : str
    body :str

# Background task to send email with error handling
#this method is executed or run after api endpoint return the response.
async def send_email_background(message: MessageSchema):
    """Background task to send email with error handling"""
    try:
        # Create FastMail instance and send the email and config contains the SMTP server details and credentials
        fm = FastMail(config)
        #the message variable contains the email details such as subject, recipient, body and subtype (plain text in this case)
        #message variable is passed to the send_message method of FastMail instance to send the email to the recipient.
        #message variable holds the data from the messageSchema which is created in the send_email endpoint and passed to this background task.
        await fm.send_message(message)
        #after sending the email siccessfully log is created to indicate that email was sent successfully to the recipient.
        logger.info(f"Email sent successfully to {message.recipients}")

        #If email sending is fail due to any reason is recorded in the log with corresponding error message.
    except Exception as e:
        logger.error(f"Failed to send email to {message.recipients}: {str(e)}")
        # You could also store the error in a database or send a notification here

#this endpoint receives email data and triggers the background task to send the email after client sends the request
@app.post("/send-email")
async def send_email(data: Email_schema, background_tasks:BackgroundTasks):
    message = MessageSchema(
        subject=data.subject,
        recipients= [data.email],
        body = data.body,
        subtype="plain"
    )
    
    #message variable contains the email details such as subject, recipient, body and subtype (plain text in this case)
    #And then the message is passed to the background task send_email_background which will handle sending mail to the recipient.
    background_tasks.add_task(send_email_background, message)

    #return repsonse after sending the email to recipient and also log is created to indicate that email is being sent to the recipient.
    logger.info(f"Email will be sent to {data.email}")
    return {"message":f"Email will be sent to {data.email}"}