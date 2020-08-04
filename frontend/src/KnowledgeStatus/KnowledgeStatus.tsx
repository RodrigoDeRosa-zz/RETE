import React, {Component} from "react";
import './KnowledgeStatus.css'

type KnowledgeStatusProps = {
    knowledge: object
}


class KnowledgeStatus extends Component<KnowledgeStatusProps> {

    render() {
        return (
            <div className="knowledge-holder">
                <label className="knowledge-status-title">Datos ingresados</label>
                <div className="knowledge-status-holder">
                    {
                        Object.entries(this.props.knowledge).map((entry, _) => {
                            return (
                                <div className="knowledge-entry-holder">
                                    <label className="knowledge-entry-key">{entry[0]}:</label>
                                    <label className="knowledge-entry-value"> {entry[1]}</label>
                                </div>
                            )
                        })
                    }
                </div>
            </div>
        );
    }

}

export default KnowledgeStatus;