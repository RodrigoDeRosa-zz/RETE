class OutputMemory:

    def __init__(self, outputs):
        self.outputs = outputs

    def match(self, enabled_outputs):
        for output in self.outputs:
            if output.id in enabled_outputs:
                return output
