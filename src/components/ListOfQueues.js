import React from 'react';
import Queue from './Queue'

const ListOfQueues = (props) => (
    <div>
        <h3>Current Queues</h3>
        {
            props.queues.map((queue, index) => 
                <Queue 
                    index={index}
                    key={queue} 
                    queueText={queue} 
                    callPeople={props.callPeople}
                />
            )
        }
    </div>
)

export default ListOfQueues 