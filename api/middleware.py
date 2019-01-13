from sql_db import *
from flask import Flask, request, redirect
from twilio_handler import *
from temp_file import *

app = Flask(__name__)

@app.route("/api/addLine", methods=["POST"])
def addLineToBase():
    lineCounter = request.json['newLine']['length']
    arrayOfQueues = request.json['newLine']['array']
    addLine(lineCounter)
    return 'abc'

@app.route("/api/callPeople", methods=['GET', 'POST'])
def callPeople():
    numPeopleToCall = request.json['numPeople']['number']
    queueNumber = request.json['numPeople']['queue']
    arrayOfNumbers = fulfilQueue(numPeopleToCall, queueNumber)
    msgUser()
    pushMessages(arrayOfNumbers, queueNumber)
    return 'def'

if __name__ == "__main__":
    app.run(debug=True, port=3000)

def populateTwilioArray(someArray):
    return someArray


