import React, {Component} from "react";
import "./NoRecommendationDisplay.css"
import KnowledgeStatus from "../KnowledgeStatus/KnowledgeStatus";
import AlternativeDisplay from "../AlternativeDisplay/AlternativeDisplay";

type NoRecommendationDisplayProps = {
    knowledge: object,
    alternative: object
}

class NoRecommendationDisplay extends Component<NoRecommendationDisplayProps> {

    render() {
        console.log(this.props);
        return (
            <div>
                <div className="message-holder">
                    <label className="no-recommendation-message">Disculpe, no fue posible inferir nada en base a la
                    información brindada.</label>
                </div>
                <div className="no-recommendation-data-holder">
                    <KnowledgeStatus knowledge={this.props.knowledge}/>
                    <AlternativeDisplay data={this.props.alternative}/>
                </div>
            </div>
        );
    }

}

export default NoRecommendationDisplay;