import React, {Component} from "react";
import BackendConnector from "../BackendConnector/BackendConnector";
import AnswerInput from "../AnswerInput/AnswerInput";
import ResultDisplay from "../ResultDisplay/ResultDisplay";
import NoRecommendationDisplay from "../NoRecommendationDisplay/NoRecommendationDisplay";

type QuestionsPageProps = {
    sessionId: string
}

class QuestionsPage extends Component<QuestionsPageProps> {

    private backendConnector: BackendConnector;

    state = {
        askedField: "",
        question: "",
        hasResult: false,
        resultObject: {},
        noRecommendation: false
    };

    constructor(props: QuestionsPageProps) {
        super(props);
        this.backendConnector = new BackendConnector();
        // Always start with a question
        this.moveForward({}).then(() => {});
    }

    async moveForward(knowledge: object): Promise<void> {
        // Call backend server with new knowledge
        const response = await this.backendConnector.forward(this.props.sessionId, knowledge);
        if (response) {
            // Check if we got to a result
            if (response.data.hasOwnProperty("inference_result")) {
                this.setState({hasResult: true, resultObject: response.data.inference_result});
            } else {
                // If we didn't then we get the next question
                let nextField = response.data.needed_fields[0];
                this.setState({askedField: nextField.field_name, question: nextField.question})
            }
        } else {
            // Error cases means we won't get a recommendation
            this.setState({noRecommendation: true})
        }
    }

    render() {
        if (this.state.hasResult) return (<ResultDisplay resultObject={this.state.resultObject}/>);
        if (this.state.noRecommendation) return (<NoRecommendationDisplay/>);
        return (
            <AnswerInput parent={this} fieldName={this.state.askedField} question={this.state.question}/>
        )
    }

}

export default QuestionsPage;