import axios, {AxiosResponse} from 'axios';

class BackendConnector {

    async ping(): Promise<boolean> {
        return await axios.get('http://localhost:5001/')
            .then(_ => {
                return true;
            })
            .catch(error => {
                console.log(error);
                return false;
            });
    }

    async start(rules: object): Promise<AxiosResponse|null> {
        return await axios.post('http://localhost:5001/start', rules)
            .then(response => {
                return response;
            })
            .catch(error => {
                console.log(error);
                return null;
            });
    }

    async forward(sessionId: string, knowledge: object): Promise<AxiosResponse> {
        return await axios.post('http://localhost:5001/forward/' + sessionId, knowledge)
            .then(response => {
                return response;
            })
            .catch(error => {
                console.log(error);
                return error.response;
            });
    }

    async restart(sessionId: string): Promise<AxiosResponse|null> {
        return await axios.post('http://localhost:5001/restart/' + sessionId)
            .then(response => {
                return response;
            })
            .catch(error => {
                console.log(error);
                return null;
            });
    }
}

export default BackendConnector;