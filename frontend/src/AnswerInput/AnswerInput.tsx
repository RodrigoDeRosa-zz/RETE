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
        if (this.state.inputData === "") return;
        await this.props.parent.moveForward({[this.props.fieldName]: this.state.inputData});
        this.setState({inputData: ""})
    }

    handleChange = (event: ChangeEvent<HTMLInputElement>) => {
        const value = event.currentTarget.value !== null ? event.currentTarget.value : "";
        if (Number.isNaN(Number(value))){
            this.setState({inputData: value});
        } else if (value === "") {
            this.setState({inputData: ""});
        } else {
            this.setState({inputData: +value})
        }
    };

    render() {
        return (
            <div className="answer-input-holder">
                <label className="question-title">{this.props.question}</label>
                <input type="text" className="question-input" onChange={this.handleChange} value={this.state.inputData}/>
                <button className="send-button" onClick={async () => this.clicked()}>ENVIAR</button>
            </div>
        )
    }

}

export default AnswerInput;