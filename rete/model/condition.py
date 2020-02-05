from rete.model.operations import BiggerThan
from rete.model.operations import BiggerThanEquals
from rete.model.operations import Equals
from rete.model.operations import LessThan
from rete.model.operations import LessThanEquals
from rete.model.operations import Operation


class Condition:

    def __init__(self):
        self.operation: Operation = Operation()
        self.field: str = ""
        self.value: object = None

    def with_field(self, field: str):
        self.field = field
        return self

    def with_value(self, value: object):
        self.value = value
        return self

    def with_operation(self, operation: str):
        if operation == "eq":
            self.operation = Equals()
        elif operation == "bt":
            self.operation = BiggerThan()
        elif operation == "lt":
            self.operation = LessThan()
        elif operation == "bte":
            self.operation = BiggerThanEquals()
        elif operation == "lte":
            self.operation = LessThanEquals()
        return self

    def apply_to(self, knowledge: dict):
        return self.operation.apply(self.field, self.value, knowledge)

    def __str__(self) -> str:
        items = ("%s = %r" % (k, v) for k, v in self.__dict__.items())
        return "<%s: {%s}>" % (self.__class__.__name__, ', '.join(items))

    def __repr__(self):
        return str(self)

