class Result:

    def __init__(self):
        self.id: str = ""
        self.result_object: dict = {}

    def with_id(self, result_id: str):
        self.id = result_id
        return self

    def with_object(self, obj: dict):
        self.result_object = obj
        return self
