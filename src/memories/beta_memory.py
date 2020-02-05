class BetaMemory:

    def __init__(self, joints, alpha_memory, output_memory):
        self.joints = joints
        self.alpha = alpha_memory
        self.output = output_memory

    def evaluate(self):
        self.evaluate_joints()
        return self.first_enabled_output()

    def evaluate_joints(self):
        for joint in self.joints:
            joint.evaluate([node.id for node in self.alpha.enabled_nodes()])

    def first_enabled_output(self):
        enabled_joint_outputs = [joint.output for joint in self.enabled_joints()]
        return self.output.match(enabled_joint_outputs)

    def enabled_joints(self):
        return [joint for joint in self.joints if joint.enabled]
