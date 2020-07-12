import uuid

from flask import Flask, request
from flask_cors import CORS, cross_origin

from rete.interface_services.question_repository import QuestionRepository
from rete.interface_services.translator import Translator
from rete.memories.alpha_memory import AlphaMemory
from rete.memories.beta_memory import BetaMemory
from rete.loaders.rule_loader import RuleLoader
from rete.memories.output_memory import OutputMemory

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def ping():
    return {'health': 'OK'}


@app.route('/start', methods=['POST'])
def start():
    request_body = request.json
    # Parse rules
    rules = RuleLoader.parse_rules(request_body['rules'])
    # Create RETE memory objects
    output = OutputMemory(rules['outputs'])
    alpha = AlphaMemory(rules['nodes'], output)
    beta = BetaMemory(rules['joints'], alpha, output)
    # Create questions repository
    repository = QuestionRepository(request_body.get('questions', {}))
    # Create session and store needed data
    sessions[(session_id := str(uuid.uuid4()).replace('-', ''))] = (alpha, beta, repository)
    return {'session_id': session_id}


@app.route('/forward/<session_id>', methods=['POST'])
def forward(session_id):
    if session_id not in sessions:
        return {'message': 'Invalid session id'}, 400
    # Retrieve memories for session
    alpha, beta, repository = sessions[session_id]
    # Update knowledge with received data
    knowledge = Translator.translate_knowledge(request.json)
    alpha.update_knowledge(knowledge)
    # Check for results
    if (result := alpha.evaluate()) or (result := beta.evaluate()):
        result.result_object['most_suitable_crop'] = Translator.translate_result(result.result_object['most_suitable_crop'])
        return {'inference_result': result.result_object}
    # Get names of fields to ask
    if not (alpha.should_continue() or beta.should_continue()) or not (fields_to_ask := alpha.needed_fields()):
        return {'message': 'No recommendation found for the given data'}, 400
    return {'needed_fields': repository.questions_for(fields_to_ask)}


if __name__ == '__main__':
    # Create default session with resources files
    default_rules = RuleLoader.load_rules_from_file('/resources/rules.json')
    default_repository = QuestionRepository.load_from_file('/resources/questions.json')
    default_output = OutputMemory(default_rules['outputs'])
    default_alpha = AlphaMemory(default_rules['nodes'], default_output)
    default_beta = BetaMemory(default_rules['joints'], default_alpha, default_output)
    # In-memory session control
    sessions = {'default': (default_alpha, default_beta, default_repository)}
    # Start up
    app.run(debug=True, port=5001)
