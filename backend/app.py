import uuid

from flask import Flask, request
from flask_cors import CORS

from rete.interface_services.question_repository import QuestionRepository
from rete.interface_services.translator import Translator
from rete.memories.alpha_memory import AlphaMemory
from rete.memories.beta_memory import BetaMemory
from rete.loaders.rule_loader import RuleLoader
from rete.memories.output_memory import OutputMemory
from rete.possible_scenario_calculator import PossibleScenarioCalculator

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
    # Get accepted values for every field
    field_values = request_body.get('field_values', {})
    # Create session and store needed data
    sessions[(session_id := str(uuid.uuid4()).replace('-', ''))] = (alpha, beta, repository, field_values)
    return {'session_id': session_id}


@app.route('/forward/<session_id>', methods=['POST'])
def forward(session_id):
    if session_id not in sessions:
        return {'message': 'Invalid session id'}, 400
    # Retrieve memories for session
    alpha, beta, repository, field_values = sessions[session_id]
    # Update knowledge with received data
    knowledge = Translator.translate_knowledge(request.json)
    alpha.update_knowledge(knowledge)
    # Check for results
    if (result_list := alpha.evaluate()) or (result_list := beta.evaluate()):
        inference_result = []
        for result in result_list:
            inference_result.append(Translator.translate_result(result.result_object['most_suitable_crop']))
        return {
            'inference_result': inference_result,
            'knowledge': Translator.translate_knowledge_return(alpha.knowledge)
        }
    # Get names of fields to ask
    if not (alpha.should_continue() or beta.should_continue()) or not (fields_to_ask := alpha.needed_fields()):
        valid_alternative = PossibleScenarioCalculator.search_valid_outcome(alpha, field_values)
        return {
                   'message': 'No recommendation found for the given data',
                   'knowledge': Translator.translate_knowledge_return(alpha.knowledge),
                   'valid_alternative': valid_alternative
               }, 400
    # Return needed fields for question asking
    return {
        'needed_fields': repository.questions_for(fields_to_ask),
        'knowledge': Translator.translate_knowledge_return(alpha.knowledge),
        'possible_results': [Translator.translate_result(output) for output in beta.possible_outputs()]
    }


if __name__ == '__main__':
    # Create default session with resources files
    default_rules = RuleLoader.load_rules_from_file('/resources/rules.json')
    default_repository = QuestionRepository.load_from_file('/resources/questions.json')
    default_output = OutputMemory(default_rules['outputs'])
    default_alpha = AlphaMemory(default_rules['nodes'], default_output)
    default_beta = BetaMemory(default_rules['joints'], default_alpha, default_output)
    default_field_values = RuleLoader.load_fields_from_file('/resources/fields.json')
    # In-memory session control
    sessions = {'default': (default_alpha, default_beta, default_repository, default_field_values)}
    # Start up
    app.run(debug=True, port=5001)
