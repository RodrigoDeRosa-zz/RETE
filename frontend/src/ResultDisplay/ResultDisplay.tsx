import React, {Component} from "react";
import './ResultDisplay.css'

type ResultDisplayProps = {
    resultObject: object
}

type CropRecommendation = {
    suitable_crops: Array<string>,
}

class ResultDisplay extends Component<ResultDisplayProps> {

    render() {
        // Map received result to our known result object
        const recommendation = this.props.resultObject as CropRecommendation;
        // Draw the result
        return (
            <div className="result-holder">
                <label className="result-title">Encontramos una sugerencia en base a lo ingresado!</label>
                {
                    recommendation.suitable_crops.map((crop, index) => {
                        return <label className="result-line"><b>Cultivo más apropiado:</b>{crop}</label>
                    } )
                }
            </div>
        )
    }

}

export default ResultDisplay;