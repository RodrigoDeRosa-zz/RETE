import random
from typing import Tuple

from rete.interface_services.translator import Translator
from rete.loaders.rule_loader import RuleLoader
from rete.memories.alpha_memory import AlphaMemory
from rete.memories.beta_memory import BetaMemory
from rete.memories.output_memory import OutputMemory


class PossibleScenarioCalculator:

    @classmethod
    def search_valid_outcome(cls, memory: AlphaMemory, possible_values: dict) -> dict:
        """ Calculates possible outcomes based on the given knowledge and its possible variations. """
        valid_outcome = {}
        checked_fields = dict()
        # Change different fields to get to a valid status
        while not valid_outcome:
            # Get the last status of knowledge where a result was possible
            knowledge = {**memory.knowledge}
            # Get a an element from the knowledge an replace it
            key = random.choice(list(knowledge.keys()))
            # Always replace with a value that hasn't been tested
            while (value := random.choice(possible_values[key])) in checked_fields.get(key, []):
                continue
            knowledge[key] = value
            # Add checked value to dict
            checked_fields[key] = checked_fields.get(key, []).append(value)
            # Create new memories to process built knowledge
            alpha, beta = cls.create_memories()
            # Process knowledge
            alpha.update_knowledge(knowledge)
            # Check for possible results
            if (result_list := alpha.evaluate()) or (result_list := beta.evaluate()):
                # Translate results
                inference_result = []
                for result in result_list:
                    inference_result.append(Translator.translate_result(result.result_object['most_suitable_crop']))
                # Append result
                valid_outcome = {
                    'results': inference_result,
                    'knowledge': Translator.translate_knowledge_return(knowledge)
                }
        return valid_outcome

    @classmethod
    def create_memories(cls) -> Tuple[AlphaMemory, BetaMemory]:
        rules = RuleLoader.load_rules_from_file('/resources/rules.json')
        output = OutputMemory(rules['outputs'])
        alpha = AlphaMemory(rules['nodes'], output)
        beta = BetaMemory(rules['joints'], alpha, output)
        return alpha, beta
