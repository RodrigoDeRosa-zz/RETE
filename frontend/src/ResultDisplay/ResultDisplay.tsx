import React, {Component} from "react";
import './ResultDisplay.css'

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
            <div className="result-holder">
                <label className="result-title">RECOMMENDATION FOUND!</label>
                <label className="result-line"><b>Arrival:</b> {recommendation.arrival}</label>
                <label className="result-line"><b>Departure:</b> {recommendation.departure}</label>
                <label className="result-line"><b>Stops:</b> {recommendation.stops.map(value => value+", ")}</label>
            </div>
        )
    }

}

export default ResultDisplay;