from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from twilio.rest import Client

account_sid = 'AC57e428058fcdf706c6dab8cab5eb3ce0'
auth_token = '837e209e242a842a38e11b8df2020ddb'
client = Client(account_sid, auth_token)

numbers = ['+19059793674', '+15197213850', '+16478793786']

def msgUser(): 
    for i in numbers:

        message = client.messages \
            .create(
                body='Hey There! Come on down to QNC for some Pizza!',
                from_='+19412293913',
                to=i
            )

        print(message.sid)