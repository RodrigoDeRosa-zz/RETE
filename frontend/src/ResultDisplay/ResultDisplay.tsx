import React, {Component} from "react";

type ResultDisplayProps = {
    resultObject: object
}

type TravelRecommendation = {
    arrival: string,
    departure: string,
    stops: string[]
}

class ResultDisplay extends Component<ResultDisplayProps> {

    render() {
        // Map received result to our known result object
        const recommendation = this.props.resultObject as TravelRecommendation;
        // Draw the result
        return (
            <div>
                <p><b>Arrival:</b> {recommendation.arrival}</p>
                <p><b>Departure:</b> {recommendation.departure}</p>
                <p><b>Stops:</b> {recommendation.stops.map(value => value+", ")}</p>
            </div>
        )
    }

}

export default ResultDisplay;