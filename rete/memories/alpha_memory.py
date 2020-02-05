from typing import List, Optional, Dict

from rete.memories.output_memory import OutputMemory
from rete.model.node import Node
from rete.model.result import Result


class AlphaMemory:

    def __init__(self, nodes: List[Node], output_memory: OutputMemory):
        self.nodes: List[Node] = nodes
        self.output: OutputMemory = output_memory
        # Keep this in memory to avoid multiple unnecessary iterations of self.nodes
        self.enabled_nodes: List[Node] = []
        self.knowledge: Dict[str, object] = {}

    def update_knowledge(self, knowledge: dict):
        self.knowledge = {**self.knowledge, **knowledge}

    def evaluate(self) -> Optional[Result]:
        self.evaluate_nodes()
        return self.first_enabled_output()

    def evaluate_nodes(self):
        # Evaluate all nodes
        for node in self.nodes:
            node.evaluate(self.knowledge)
        # Keep only those that have sense to analyze again based on the current knowledge
        self.nodes = [node for node in self.nodes if not node.removable]
        # Store the enabled nodes
        self.enabled_nodes = [node for node in self.nodes if node.enabled]

    def first_enabled_output(self) -> Optional[Result]:
        enabled_node_outputs = [node.output for node in self.enabled_nodes]
        return self.output.find_first(enabled_node_outputs)

    def needed_fields(self) -> set:
        # The needed fields to progress in our solution search are those that our remaining nodes need to evaluate
        # and our knowledge still doesn't have
        fields_to_ask = set()
        for node in self.nodes:
            fields_to_ask = fields_to_ask.union(set(node.relevant_fields()).difference(set(self.knowledge.keys())))
        return fields_to_ask
