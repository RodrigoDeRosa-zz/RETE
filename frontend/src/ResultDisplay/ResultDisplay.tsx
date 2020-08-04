import React, {Component} from "react";
import './ResultDisplay.css'
import KnowledgeStatus from "../KnowledgeStatus/KnowledgeStatus";

type ResultDisplayProps = {
    resultObject: object,
    knowledge: object
}


class ResultDisplay extends Component<ResultDisplayProps> {

    render() {
        const recommendation = this.props.resultObject as Array<string>
        // Draw the result
        return (
            <div>
                <div className="result-holder">
                    <label className="result-title">Encontramos una sugerencia en base a lo ingresado!</label>
                    {
                        recommendation.map((crop, _) => {
                            return <label className="result-line"><b>Cultivo apropiado: </b>{crop}</label>
                        } )
                    }
                </div>
                <KnowledgeStatus knowledge={this.props.knowledge}/>
            </div>
        );
    }

}

export default ResultDisplay;