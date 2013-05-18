from .. import Skill
#from ...utils.mathutils import cos, sin, sqrt
from ...utils.mathutils import sqrt
from ...utils.geom import Point
from ...utils.pidcontroller import PidController
#import sys


class Goto(Skill):
    def __init__(self, robot, x, y, angle=False, speed=0.5, ang_speed=0.2, goalkeeper=False):
        super(Goto, self).__init__(robot, True)
        self.angle_controller = PidController(kp=5.8, ki=0, kd=0, integ_max=687.55, output_max=100000)
        #self.angle_controller = PidController(kp=1.324, ki=0, kd=0, integ_max=6.55, output_max=1000)
        self.angle = angle if angle is not None else robot.angle
        self.speed = speed
        self.ang_speed = ang_speed
        self.x = x
        self.y = y
        self.avoid_defense_area = not goalkeeper

    def busy(self):
        return False

    def step(self):
        if self.robot.world.is_in_defense_area(body=Point(self.x, self.y).buffer(self.robot.radius), color=self.robot.color):
            point = self.point_away_from_defense_area
            self.x = point.x
            self.y = point.y

        #TODO: Control!
        s = self.speed

        r = self.robot
        # FIXME: Velocidade angular nao pode ficar ridiculamente grande depois de alguns spins
        #va = ang_speed * (self.a - r.angle)
        self.angle_controller.input = (180 + self.angle - self.robot.angle) % 360 - 180
        self.angle_controller.feedback = 0.0
        self.angle_controller.step()
        va = self.angle_controller.output

        dx, dy = self.x - r.x, self.y - r.y
        if dx * dx + dy * dy > 0:
            size = sqrt(dx * dx + dy * dy)
            vx = s * dx / size
            vy = s * dy / size
        else:
            vx = vy = 0.0

        #print r.action.absolute_speeds
        r.action.absolute_speeds = vx, vy, va

    @property
    def point_away_from_defense_area(self):
        # FIXME: Only works if robot is inside defense area (which, honestly, is the only place you should ever be using this).
        r = self.robot

        target = Point(self.x, self.y)

        defense_area = r.world.defense_area(r.color).buffer(r.radius + 0.1).boundary
        distance = target.distance(defense_area)
        buffered_circumference = target.buffer(distance)
        intersection = buffered_circumference.intersection(defense_area).centroid
        if not intersection.is_empty:
            desired_distance = distance
            modulus = sqrt((intersection.x - self.x) * (intersection.x - self.x) + (intersection.y - self.y) * (intersection.y - self.y))
            dx = desired_distance * (intersection.x - self.x) / modulus
            dy = desired_distance * (intersection.y - self.y) / modulus
            return Point(self.x + dx, self.y + dy)
        else:
            return Point(self.x, self.y)
