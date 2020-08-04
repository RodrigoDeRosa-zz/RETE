import React, {Component} from "react";
import './QuestionsPage.css';
import BackendConnector from "../BackendConnector/BackendConnector";
import AnswerInput from "../AnswerInput/AnswerInput";
import ResultDisplay from "../ResultDisplay/ResultDisplay";
import NoRecommendationDisplay from "../NoRecommendationDisplay/NoRecommendationDisplay";
import KnowledgeStatus from "../KnowledgeStatus/KnowledgeStatus";
import PossibleResults from "../PossibleResults/PossibleResults";

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
        knowledge: {},
        validAlternative: {},
        possibleResults: [],
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
        if (response?.status === 200) {
            // Check if we got to a result
            if (response.data.hasOwnProperty("inference_result")) {
                this.setState({
                    hasResult: true, 
                    resultObject: response.data.inference_result,
                    knowledge: response.data.knowledge
                });
            } else {
                // If we didn't then we get the next question
                let nextField = response.data.needed_fields[0];
                console.log(response.data);
                this.setState({
                    askedField: nextField.field_name, 
                    question: nextField.question,
                    knowledge: response.data.knowledge,
                    possibleResults: response.data.possible_results
                });
            }
        } else {
            // Error cases means we won't get a recommendation
            this.setState({
                noRecommendation: true, 
                knowledge: response.data.knowledge,
                validAlternative: response.data.valid_alternative
            })
        }
    }

    render() {
        if (this.state.hasResult) 
            return <ResultDisplay resultObject={this.state.resultObject} knowledge={this.state.knowledge}/>
        if (this.state.noRecommendation) 
            return <NoRecommendationDisplay knowledge={this.state.knowledge} alternative={this.state.validAlternative}/>
        const hasKnowledge = Object.keys(this.state.knowledge).length !== 0;
        return (
            <div>
                <AnswerInput parent={this} fieldName={this.state.askedField} question={this.state.question}/>
                {
                    hasKnowledge ? (
                        <div className="status-content-holder">
                            <KnowledgeStatus knowledge={this.state.knowledge}/> 
                            <PossibleResults possibleResults={this.state.possibleResults}/> 
                        </div>
                    ) : <div/>
                }
            </div>
        );
    }

}

export default QuestionsPage;