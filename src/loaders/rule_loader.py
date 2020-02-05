import json
from os.path import abspath, join, dirname

from src.model.condition import Condition
from src.model.joint import Joint
from src.model.node import Node
from src.model.result import Result


class RuleLoader:

    @staticmethod
    def load_rules(path: str):
        file_path = f'{abspath(join(dirname(__file__), "../../"))}{path}'
        with open(file_path, 'r') as fd:
            raw_rules = json.load(fd)
        rules = {'nodes': [], 'joints': [], 'outputs': []}
        for node in raw_rules.get('nodes', []):
            conditions = []
            for condition in node.get('conditions', []):
                conditions.append(
                    Condition()
                        .with_field(condition['field'])
                        .with_value(condition['value'])
                        .with_operation(condition['operation'])
                )
            rules['nodes'].append(
                Node()
                    .with_id(node['id'])
                    .with_conditions(conditions)
                    .with_output(node.get('output'))
            )
        for joint in raw_rules.get('joints', []):
            rules['joints'].append(
                Joint()
                    .with_id(joint['id'])
                    .with_nodes(joint['nodes'])
                    .with_output(joint['output'])
            )
        for output in raw_rules.get('outputs', []):
            rules['outputs'].append(
                Result()
                    .with_id(output['id'])
                    .with_object(output['object'])
            )
        return rules
