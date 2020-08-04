from typing import List, Optional


class Joint:

    def __init__(self):
        self.id: str = ""
        self.node_ids: List[str] = []
        self.enabled: bool = False
        self.output: Optional[str] = None

    def with_id(self, joint_id: str):
        self.id = joint_id
        return self

    def with_nodes(self, node_ids: List[str]):
        self.node_ids = node_ids
        return self

    def with_output(self, output: str):
        self.output = output
        return self

    def evaluate(self, enabled_nodes: List[str]):
        if set(self.node_ids) <= set(enabled_nodes):
            self.enabled = True

    def __str__(self) -> str:
        items = ("%s = %r" % (k, v) for k, v in self.__dict__.items())
        return "<%s: {%s}>" % (self.__class__.__name__, ', '.join(items))

    def __repr__(self) -> str:
        return str(self)
