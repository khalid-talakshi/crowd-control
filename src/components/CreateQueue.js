import React from 'react'

export default class CreateEvent extends React.Component {

    state = {
        error: undefined
    };

    handleAddLine = (e) => {
        e.preventDefault();
        const formOption = e.target.elements.name.value.trim();
        const error = this.props.addLine(formOption);
        this.setState(() => ({ error }));
        if (!error) {
            e.target.elements.name.value = '';
        }
    }

    render() {
        return(
            <div>
                <h2>Create Line</h2>
                {this.state.error && <p className="add-option-error">{this.state.error}</p>}
                <form onSubmit={this.handleAddLine}>
                    <input name="name" type="text" />
                    <button>Add Line</button>
                </form>
            </div>
        )
    }
}