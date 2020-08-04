from typing import List, Optional

from rete.memories.alpha_memory import AlphaMemory
from rete.memories.output_memory import OutputMemory
from rete.model.joint import Joint
from rete.model.result import Result


class BetaMemory:

    def __init__(self, joints: List[Joint], alpha_memory: AlphaMemory, output_memory: OutputMemory):
        self.joints: List[Joint] = joints
        # Keep this in memory to avoid multiple unnecessary iterations of self.joints
        self.enabled_joints: List[Joint] = []
        self.alpha: AlphaMemory = alpha_memory
        self.output: OutputMemory = output_memory

    def evaluate(self) -> List[Result]:
        self.evaluate_joints()
        return self.enabled_outputs()

    def should_continue(self) -> bool:
        return len(self.joints) > 0

    def evaluate_joints(self):
        # Remove all the joints that could never possibly be enabled based on the current knowledge
        self.joints = [
            joint
            for joint in self.joints
            if not set(joint.node_ids).intersection(self.alpha.removable_nodes())
        ]
        # Get the ids of the currently enabled nodes
        enabled_nodes_ids = [node.id for node in self.alpha.enabled_nodes]
        # Check which joints can be enabled
        for joint in self.joints:
            joint.evaluate(enabled_nodes_ids)
        # Store the enabled joints
        self.enabled_joints = [joint for joint in self.joints if joint.enabled]

    def enabled_outputs(self) -> Optional[List[Result]]:
        enabled_joint_outputs = [joint.output for joint in self.enabled_joints]
        return self.output.get_all(enabled_joint_outputs)

    def possible_outputs(self):
        return set([joint.output for joint in self.joints])
