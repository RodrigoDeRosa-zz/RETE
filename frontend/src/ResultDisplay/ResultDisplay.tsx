import React, {Component} from "react";
import './ResultDisplay.css'

type ResultDisplayProps = {
    resultObject: object
}


class ResultDisplay extends Component<ResultDisplayProps> {

    render() {
        const recommendation = this.props.resultObject as Array<string>
        // Draw the result
        return (
            <div className="result-holder">
                <label className="result-title">Encontramos una sugerencia en base a lo ingresado!</label>
                {
                    recommendation.map((crop, index) => {
                        return <label className="result-line"><b>Cultivo apropiado:</b>{crop}</label>
                    } )
                }
            </div>
        )
    }

}

export default ResultDisplay;