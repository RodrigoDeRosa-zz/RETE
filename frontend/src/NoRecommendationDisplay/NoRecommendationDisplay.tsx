import React, {Component} from "react";

type NoRecommendationDisplayProps = {}

class NoRecommendationDisplay extends Component<NoRecommendationDisplayProps> {

    render() {
        return (
            <p>Sorry, we couldn't infer nothing with the knowledge we have.</p>
        )
    }

}

export default NoRecommendationDisplay;