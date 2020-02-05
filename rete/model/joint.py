from typing import List

from rete.model.node import Node


class Joint:

    def __init__(self):
        self.id: str = ""
        self.node_ids: List[str] = []
        self.enabled = False
        self.output = None

    def with_id(self, joint_id: str):
        self.id = joint_id
        return self

    def with_nodes(self, node_ids: List[str]):
        self.node_ids = node_ids
        return self

    def with_output(self, output):
        self.output = output
        return self

    def evaluate(self, enabled_nodes: List[Node]):
        if set(self.node_ids) <= set(enabled_nodes):
            self.enabled = True
