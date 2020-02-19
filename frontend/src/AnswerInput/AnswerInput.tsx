import React, {ChangeEvent, Component} from "react";
import './AnswerInput.css'
import QuestionsPage from "../QuestionsPage/QuestionsPage";

type AnswerInputProps = {
    parent: QuestionsPage,
    fieldName: string,
    question: string
}

class AnswerInput extends Component<AnswerInputProps> {

    state = {
        inputData: ""
    };

    async clicked() {
        await this.props.parent.moveForward({[this.props.fieldName]: this.state.inputData});
        this.setState({inputData: ""})
    }

    handleChange = (event: ChangeEvent<HTMLInputElement>) => {
        const value = event.currentTarget.value !== null ? event.currentTarget.value : "";
        if (Number.isNaN(Number(value))){
            this.setState({inputData: value});
        } else {
            this.setState({inputData: +value});
        }
    };

    render() {
        return (
            <div className="answer-input-holder">
                <label className="question-title">{this.props.question}</label>
                <input className="question-input" onChange={this.handleChange} value={this.state.inputData}/>
                <button className="send-button" onClick={async () => this.clicked()}>SEND</button>
            </div>
        )
    }

}

export default AnswerInput;