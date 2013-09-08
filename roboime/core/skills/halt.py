from .. import Skill


class Halt(Skill):
    """
    This skill will stop the robot by setting its action target
    to its current position.
    """

    parameters = []

    def __init__(self, robot, deterministic=True, **kwargs):
        super(Halt, self).__init__(robot, deterministic=deterministic, **kwargs)

    def _step(self):
        self.robot.base_skill_class = Halt

    def _execute_step(self):
        self.robot.action.absolute_speeds = (0, 0, 0)
        self.robot.skill = self
