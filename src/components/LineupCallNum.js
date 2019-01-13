import React from 'react';

export default class lineupCallNum extends React.Component {

    handleUpdateNum = (e) => {
        e.preventDefault();
        const formOption = e.target.elements.numPeople.value;
        if (formOption) {
            this.props.updateNumPeopleToCall(formOption);
        } else {
            alert("Please choose a number")
        }
    }

    render() {
        return (
            <div className="numBox">
                <h2>Call people</h2>
                <form onSubmit={this.handleUpdateNum}>
                    <div className="numBox">
                        <input type="number" name="numPeople" />
                        <button className="button">Call People</button>
                    </div>
                </form>
            </div>
        )
    }
}