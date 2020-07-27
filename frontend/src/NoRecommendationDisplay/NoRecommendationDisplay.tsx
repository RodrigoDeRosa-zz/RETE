import React, {Component} from "react";
import "./NoRecommendationDisplay.css"

type NoRecommendationDisplayProps = {}

class NoRecommendationDisplay extends Component<NoRecommendationDisplayProps> {

    render() {
        return (
            <div className="message-holder">
                <label className="no-recommendation-message">Disculpe, no fue posible inferir nada en base a la
                información brindada.</label>
            </div>
        )
    }

}

export default NoRecommendationDisplay;