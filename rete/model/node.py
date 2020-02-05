from typing import List, Optional

from rete.model.condition import Condition


class Node:

    def __init__(self):
        self.id: str = ""
        self.conditions: List[Condition] = []
        self.enabled: bool = False
        self.removable: bool = False
        self.output: Optional[str] = None

    def with_id(self, node_id: str):
        self.id = node_id
        return self

    def with_conditions(self, conditions: List[Condition]):
        self.conditions = conditions
        return self

    def with_output(self, output):
        self.output = output
        return self

    def relevant_fields(self) -> List[str]:
        return [condition.field for condition in self.conditions]

    def evaluate(self, knowledge: dict):
        result = True
        # For every condition check if it is met
        for condition in self.conditions:
            meets_condition = condition.apply_to(knowledge)
            # In case the condition failed because the field was invalid for it, we can remove this Node from the tree
            if not meets_condition and condition.field in knowledge:
                self.enabled = False
                self.removable = True
                return
            # The evaluation of all conditions with an AND gate is the final result
            result = meets_condition and result
        self.enabled = result

    def __str__(self) -> str:
        items = ("%s = %r" % (k, v) for k, v in self.__dict__.items())
        return "<%s: {%s}>" % (self.__class__.__name__, ', '.join(items))

    def __repr__(self) -> str:
        return str(self)
