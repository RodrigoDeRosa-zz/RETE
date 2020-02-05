import uuid

from flask import Flask, request

from rete.memories.alpha_memory import AlphaMemory
from rete.memories.beta_memory import BetaMemory
from rete.loaders.rule_loader import RuleLoader
from rete.memories.output_memory import OutputMemory

app = Flask(__name__)


@app.route('/')
def ping():
    return {'health': 'OK'}


@app.route('/start', methods=['GET'])
def start():
    alpha = AlphaMemory(rules['nodes'], output)
    beta = BetaMemory(rules['joints'], alpha, output)
    sessions[(session_id := str(uuid.uuid4()).replace('-', ''))] = (alpha, beta)
    return {'session_id': session_id}


@app.route('/forward/<session_id>', methods=['POST'])
def forward(session_id):
    if session_id not in sessions:
        return {'message': 'Invalid session id'}, 400
    # Retrieve memories for session
    alpha, beta = sessions[session_id]
    # Update knowledge with received data
    alpha.update_knowledge(request.json)
    # Check for results
    if (result := alpha.evaluate()) or (result := beta.evaluate()):
        return {'recommendation': result.result_object}
    # Get names of fields to ask
    if not (fields_to_ask := alpha.needed_fields()):
        return {'message': 'No recommendation found for the given data'}, 400
    return {'to_ask': list(fields_to_ask)}


if __name__ == '__main__':
    rules = RuleLoader.load_rules('/resources/rules.json')
    output = OutputMemory(rules['outputs'])
    sessions = {}
    app.run(debug=True, port=5001)
