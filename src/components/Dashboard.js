import React from 'react';
import ListOfQueues from './ListOfQueues';
import CreateQueue from './CreateQueue';
import LineupCallNum from './LineupCallNum';
import axios from 'axios'

export default class Dashboard extends React.Component {
    state = {
        newQueue: '',
        queues: [],
        numPeopleToCall: 10
    }

    addLine = (input) => {
        if (!input) {
            return 'Enter valid value to add item';
          } else if (this.state.queues.indexOf(input) > -1) {
            return 'This option already exists';
          }
      
          this.setState((prevState) => ({
                newQueue: input,
                queues: prevState.queues.concat(input)
          }));

          const newLine = {
                length: this.state.queues.length,
                array: this.state.queues
          }

          axios.post(`/api/addLine`, { newLine })
    }

    callPeople = (index) => {
        const numPeople = {
            number: this.state.numPeopleToCall ,
            queue: index
        }
        alert("Calling the next " + this.state.numPeopleToCall + " people")
        axios.post(`/api/callPeople`, { numPeople })
    }

    updateNumPeopleToCall = (num) => {
        this.setState(() => ({
            numPeopleToCall: num,
        }))
    }

    render() {
        return (
        <div className="container">
            <div className="header">
                <h1>Welcome to Crowd Control</h1>
                <h2>Dashboard</h2>
            </div>
            <ListOfQueues queues={this.state.queues} callPeople={this.callPeople} deleteQueue={this.deleteQueue} />
            <CreateQueue addLine={this.addLine}/>
            <LineupCallNum updateNumPeopleToCall={this.updateNumPeopleToCall} />
        </div>)
    }
}