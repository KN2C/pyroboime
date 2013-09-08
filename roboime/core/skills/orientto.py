from numpy import pi, sign, array
from numpy.linalg import norm

#from ...utils.mathutils import sqrt
from ...utils.pidcontroller import PidController
from .. import Skill


class OrientTo(Skill):
    """
    This skill will orient the robot arount a given point to look to another given point,
    """

    parameters = ["lookpoint"]

    angle_tolerance = 0.5
    distance_tolerance = 0.11
    walkspeed = 0.1

    def __init__(self, robot, lookpoint=None, minpower=0.0, maxpower=1.0, **kwargs):
        """
        """
        super(OrientTo, self).__init__(robot, deterministic=True, **kwargs)
        self.lookpoint = lookpoint
        self.minpower = minpower
        self.maxpower = maxpower
        self.angle_controller = PidController(kp=1.8, ki=0, kd=0, integ_max=687.55, output_max=360)
        self.distance_controller = PidController(kp=1.8, ki=0, kd=0, integ_max=687.55, output_max=360)

    @property
    def final_target(self):
        return self.lookpoint

    def good_position(self):
        good_distance = self.robot.kicker.distance(self.ball) <= self.distance_tolerance
        good_angle = abs(self.delta_angle()) < self.angle_tolerance
        return good_distance and good_angle

    def delta_angle(self):
        delta =  self.robot.angle - self.ball.angle_to_point(self.lookpoint)
        return (180 + delta) % 360 - 180

    def _step(step):
        self.robot.base_skill_class = OrientTo

    def _execute_step(self):
        delta_angle = self.delta_angle()

        self.angle_controller.input = delta_angle
        self.angle_controller.feedback = 0.0
        self.angle_controller.step()

        #d = self.robot.front_cut + self.ball.radius
        d = norm(array(self.robot) - array(self.ball))
        r = self.robot.radius

        w = self.angle_controller.output
        max_w = 180.0 * self.robot.max_speed / r / pi
        if abs(w) > max_w:
            w = sign(w) * max_w
        v = pi * w * d / 180.0

        self.robot.action.speeds = (0.0, v, -w)
