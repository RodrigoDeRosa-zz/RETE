import React, {Component} from "react";
import './AlternativeDisplay.css'

type AlternativeData = {
    knowledge: object,
    results: Array<string>
}

type AlternativeDisplayProps = {
    data: object
}


class AlternativeDisplay extends Component<AlternativeDisplayProps> {

    render() {
        const data = this.props.data as AlternativeData;
        console.log(data);
        return (
            <div className="alternative-holder">
                <label className="alternative-holder-title">Alternativa: </label>
                <div className="alternative-knowledge-holder">
                    <label className="alternative-knowledge-title">Condiciones requeridas</label>
                    <div className="alternative-knowledge-entries-holder">
                        {
                            Object.entries(data.knowledge).map((entry, _) => {
                                return (
                                    <div className="alternative-entry-holder">
                                        <label className="alternative-entry-key">{entry[0]}:</label>
                                        <label className="alternative-entry-value">{entry[1]}</label>
                                    </div>
                                );
                            })
                        }
                    </div>
                </div>
                <div className="alternative-result-holder">
                    <label className="alternative-result-title">Resultados obtenidos</label>
                    <div className="alternative-result-line-holder">
                        {
                            data.results.map((crop, _) => {
                                return <label className="alternative-result-line"><b>Cultivo apropiado: </b>{crop}</label>
                            })
                        } 
                    </div>
                </div>
            </div>
        );
    }

}

export default AlternativeDisplay;