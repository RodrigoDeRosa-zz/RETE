import React, {Component} from "react";
import '../KnowledgeStatus/KnowledgeStatus.css'
import './PossibleResults.css'

type PossibleResultsProps = {
    possibleResults: Array<string>
}


class PossibleResults extends Component<PossibleResultsProps> {

    render() {
        console.log(this.props.possibleResults)
        return (
            <div className="knowledge-holder">
                <label className="knowledge-status-title">Resultados posibles con el conocimiento actual</label>
                <div className="knowledge-status-holder">
                    {
                        this.props.possibleResults.map((value, _) => {
                            return <label key={value} className="possible-result-entry">{value}</label>
                        })
                    }
                </div>
            </div>
        )
    }

}

export default PossibleResults;