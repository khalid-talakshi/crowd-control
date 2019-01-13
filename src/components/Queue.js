import React from 'react';

const Queue = (props) => (
    <div>
        <p>{props.queueText}</p>
        <button onClick={() => props.callPeople(props.index)}>Call</button>
        <button>Delete</button>
    </div>
)

export default Queue