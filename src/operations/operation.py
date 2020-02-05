class Operation:

    def apply(self, field: str, value: object, knowledge: dict) -> bool:
        raise RuntimeError("Abstract class method called. Operation::apply.")
