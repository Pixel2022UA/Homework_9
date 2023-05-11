import os
from dotenv import load_dotenv
from celery import shared_task
from twilio.rest import Client

load_dotenv()


@shared_task
def send_sms(number):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hello from 9 Homework",
        from_="+12708122588",
        to=os.getenv("TWILIO_FROM_NUMBER"),
    )
    print(message.sid)
