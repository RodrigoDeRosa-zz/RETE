from typing import Optional, List

from rete.model.result import Result


class OutputMemory:

    def __init__(self, outputs: List[Result]):
        self.outputs = outputs

    def find_first(self, enabled_outputs) -> Optional[Result]:
        for output in self.outputs:
            if output.id in enabled_outputs:
                return output

    def get_all(self, enabled_outputs) -> Optional[List[Result]]:
        outputs = []
        for output in self.outputs:
            if output.id in enabled_outputs:
                outputs.append(output)
        return outputs
