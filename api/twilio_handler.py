from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from twilio.rest import Client

account_sid = 'AC57e428058fcdf706c6dab8cab5eb3ce0'
auth_token = '837e209e242a842a38e11b8df2020ddb'
client = Client(account_sid, auth_token)

app = Flask(__name__)

# Counter Variable to track the number of lines
lines = ['Lunch - Pizza', 'Dinner - Thai', 'VR Games']
numberOfLines = 3 

def checkNum(num):
    try:
        return int(num)
    except ValueError:
        return None

# Sends a response message when a number is texted
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    resp = MessagingResponse()
    # lines = addLineToBase()
    # Get the message and number the user sent our Twilio number
    body = request.values.get('Body', None).lower().strip()
    msg = ""
    
    # Determine the right reply for this message
    if body == 'hello':
        msg = "welcome to starterhacks. Don't want to wait in lineups? msg lines to this number to see what you can wait for."
    elif body == 'help':
         msg ="Need some help? type lines to see what you can wait for, and respond with the corresponding index to get in line"
    elif body == 'lines':
         msg = "Here are the lines:" + str(lines) + " Please respond with the index of the line you want to lineup" 
    elif checkNum(body) != None:
        if int(body) > numberOfLines:
             msg = "Please send a valid response"
        else:
             msg = "You have been added to " + lines[int(body)]
    else: 
        msg = "Please send a valid resp"

    resp.message(msg)

    return str(resp)

def pushMessages(numbers, lineNumber):
    for number in numbers: 
        message = client.messages \
        .create(
            body='Line Number ' + lineNumber + '. Come on down.',
            from_='+19412293913',
            to=number)
   

if __name__ == "__main__":
    app.run(debug=True, port=80)
