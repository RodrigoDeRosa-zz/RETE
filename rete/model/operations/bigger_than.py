from rete.model.operations.operation import Operation


class BiggerThan(Operation):

    def apply(self, field: str, value: object, knowledge: dict) -> bool:
        return False if not knowledge or not knowledge.get(field, None) else knowledge[field] > value

    def __str__(self) -> str:
        items = ("%s = %r" % (k, v) for k, v in self.__dict__.items())
        return "<%s: {%s}>" % (self.__class__.__name__, ', '.join(items))

    def __repr__(self):
        return str(self)