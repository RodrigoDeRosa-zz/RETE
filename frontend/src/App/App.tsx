import React, {Component} from 'react';
import './App.css';
import BackendConnector from "../BackendConnector/BackendConnector";
import QuestionsPage from "../QuestionsPage/QuestionsPage";

type AppProps = {}

class App extends Component<AppProps> {

    private backendConnector: BackendConnector;

    state = {
        serverOn: null
    };

    constructor(props: AppProps) {
        super(props);
        this.backendConnector = new BackendConnector();
    }

    async componentDidMount(): Promise<void> {
        if (await this.backendConnector.ping()) {
            this.setState({serverOn: true});
        } else this.setState({serverOn: false})
    }

    render() {
        // Check connection to backend server
        let html;
        if (this.state.serverOn === null) html = <p>Checking connection to backend server...</p>;
        else if (this.state.serverOn) html = <QuestionsPage sessionId="default"/>;
        else html = <p>Failed to connect to backend server.</p>;
        // Render application
        return (
            <div>
                {html}
            </div>
        );
    }
}

export default App;
