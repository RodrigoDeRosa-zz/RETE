class AlphaMemory:

    def __init__(self, nodes, output_memory):
        self.nodes = nodes
        self.output = output_memory
        self.knowledge = {}

    def update_knowledge(self, knowledge: dict):
        self.knowledge = {**self.knowledge, **knowledge}

    def evaluate(self):
        self.evaluate_nodes()
        return self.first_enabled_output()

    def evaluate_nodes(self):
        for node in self.nodes:
            node.evaluate(self.knowledge)
        self.nodes = [node for node in self.nodes if not node.removable]

    def first_enabled_output(self):
        enabled_node_outputs = [node.output for node in self.enabled_nodes()]
        return self.output.match(enabled_node_outputs)

    def needed_fields(self) -> set:
        fields_to_ask = set()
        for node in self.nodes:
            fields_to_ask = fields_to_ask.union(set(node.relevant_fields()).difference(set(self.knowledge.keys())))
        return fields_to_ask

    def enabled_nodes(self):
        return [node for node in self.nodes if node.enabled]
