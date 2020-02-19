import React, {Component} from "react";
import "./NoRecommendationDisplay.css"

type NoRecommendationDisplayProps = {}

class NoRecommendationDisplay extends Component<NoRecommendationDisplayProps> {

    render() {
        return (
            <div className="message-holder">
                <label className="no-recommendation-message">Sorry, we couldn't infer nothing with the knowledge we
                    have.</label>
            </div>
        )
    }

}

export default NoRecommendationDisplay;