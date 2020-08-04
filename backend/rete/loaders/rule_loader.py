import json
from os.path import abspath, join, dirname
from typing import List

from rete.model.condition import Condition
from rete.model.joint import Joint
from rete.model.node import Node
from rete.model.result import Result


class RuleLoader:

    @classmethod
    def load_rules_from_file(cls, path: str) -> dict:
        file_path = f'{abspath(join(dirname(__file__), "../../"))}{path}'
        with open(file_path, 'r') as fd:
            raw_rules = json.load(fd)
        return cls.parse_rules(raw_rules)

    @classmethod
    def load_fields_from_file(cls, path: str) -> dict:
        file_path = f'{abspath(join(dirname(__file__), "../../"))}{path}'
        with open(file_path, 'r') as fd:
            fields_values = json.load(fd)
        return fields_values

    @classmethod
    def parse_rules(cls, rules_dict: dict) -> dict:
        return {
            'nodes': cls.__parse_nodes(rules_dict.get('nodes', [])),
            'joints': cls.__parse_joints(rules_dict.get('joints', [])),
            'outputs': cls.__parse_results(rules_dict.get('outputs', []))
        }

    @classmethod
    def __parse_nodes(cls, raw_nodes: list) -> List[Node]:
        nodes = []
        for node in raw_nodes:
            conditions = [
                Condition().with_field(cond['field']).with_value(cond['value']).with_operation(cond['operation'])
                for cond in node.get('conditions', [])
            ]
            nodes.append(Node().with_id(node['id']).with_conditions(conditions).with_output(node.get('output')))
        return nodes

    @classmethod
    def __parse_joints(cls, raw_joints: dict) -> List[Joint]:
        return [
            Joint().with_id(joint['id']).with_nodes(joint['nodes']).with_output(joint['output'])
            for joint in raw_joints
        ]

    @classmethod
    def __parse_results(cls, raw_results: dict) -> List[Result]:
        return [
            Result().with_id(result['id']).with_object(result['object'])
            for result in raw_results
        ]
