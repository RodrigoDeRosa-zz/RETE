from typing import List, Optional, Dict

from rete.memories.output_memory import OutputMemory
from rete.model.node import Node
from rete.model.result import Result


class AlphaMemory:

    def __init__(self, nodes: List[Node], output_memory: OutputMemory):
        self.nodes: List[Node] = nodes
        self.output: OutputMemory = output_memory
        self.knowledge: Dict[str, object] = {}
        # Keep this in memory to avoid multiple unnecessary iterations of self.nodes
        self.enabled_nodes: List[Node] = []
        # List that keeps removed nodes only for a while, to allow Beta memory to eliminate unneeded nodes
        self.__removable_nodes: List[Node] = []

    def update_knowledge(self, knowledge: dict):
        # Update knowledge
        self.knowledge = {**self.knowledge, **knowledge}

    def evaluate(self) -> List[Result]:
        self.evaluate_nodes()
        return self.enabled_outputs()

    def evaluate_nodes(self):
        # Evaluate all nodes
        for node in self.nodes:
            node.evaluate(self.knowledge)
        # Store the removable nodes momentarily for beta memory updating
        self.__removable_nodes = [node for node in self.nodes if node.removable]
        # Keep only those that have sense to analyze again based on the current knowledge
        self.nodes = list(set(self.nodes).difference(set(self.__removable_nodes)))
        # Store the enabled nodes
        self.enabled_nodes = [node for node in self.nodes if node.enabled]

    def should_continue(self) -> bool:
        return next(filter(lambda node: node.output is not None, self.nodes), None) is not None

    def enabled_outputs(self) -> Optional[List[Result]]:
        enabled_node_outputs = [node.output for node in self.enabled_nodes]
        return self.output.get_all(enabled_node_outputs)

    def needed_fields(self) -> set:
        # The needed fields to progress in our solution search are those that our remaining nodes need to evaluate
        # and our knowledge still doesn't have
        fields_to_ask = set()
        for node in self.nodes:
            fields_to_ask = fields_to_ask.union(set(node.relevant_fields()).difference(set(self.knowledge.keys())))
        return fields_to_ask

    def removable_nodes(self):
        """ This method can be called only once, as it will clear the list. """
        output = self.__removable_nodes
        self.__removable_nodes = []
        return output
