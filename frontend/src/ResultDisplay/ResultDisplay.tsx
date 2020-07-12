import React, {Component} from "react";
import './ResultDisplay.css'

type ResultDisplayProps = {
    resultObject: object
}

type CropRecommendation = {
    most_suitable_crop: string,
}

class ResultDisplay extends Component<ResultDisplayProps> {

    render() {
        // Map received result to our known result object
        const recommendation = this.props.resultObject as CropRecommendation;
        // Draw the result
        return (
            <div className="result-holder">
                <label className="result-title">Encontramos una sugerencia en base a lo ingresado!</label>
                <label className="result-line"><b>Cultivo más apropiado:</b> {recommendation.most_suitable_crop}</label>
            </div>
        )
    }

}

export default ResultDisplay;