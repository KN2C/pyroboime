from multiprocessing import Process, Queue, Event
from math import degrees

from ..communication import sslvision
from .. import base


STOP_TIMEOUT = 1


def _linear_scale(value):
    return value / 1000.0


def _angular_scale(value):
    return degrees(value);


class Update(object):

    def __init__(self, data):
        self.data = data

    def apply(self):
        pass


class BallUpdate(Update):

    def apply(self, world):
        ball = world.ball
        for prop, value in self.data.iteritems():
            setattr(ball, prop, value)


class RobotUpdate(Update):

    def __init__(self, team_color, i, data):
        Update.__init__(self, data)
        self.team_color = team_color
        self.i = i

    def apply(self, world):
        if self.team_color == base.Blue:
            team = world.blue_team
        elif self.team_color == base.Yellow:
            team = world.yellow_team
        robot = team[self.i]
        for prop, value in self.data.iteritems():
            setattr(robot, prop, value)


class GeometryUpdate(Update):

    def apply(self, world):
        for prop, value in self.data.iteritems():
            setattr(world, prop, value)


class Updater(Process):

    def __init__(self):
        Process.__init__(self)
        self.queue = Queue()
        self._exit = Event()

    def run(self):
        while not self._exit.is_set():
            try:
                self.queue.put(self.receive())
            except KeyboardInterrupt:
                break

    def stop(self):
        self._exit.set()
        self.join(STOP_TIMEOUT)
        if self.is_alive():
            #TODO make a nicer warning
            print 'Terminating updater:', self
            self.terminate()

    def receive(self):
        pass


class VisionUpdater(Updater):

    def __init__(self, address):
        Updater.__init__(self)
        self.receiver = sslvision.VisionReceiver(address)

    def receive(self):
        updates = []
        packet = self.receiver.get_packet()

        if packet.HasField('geometry'):
            f = packet.geometry.field
            updates.append(GeometryUpdate({
                'width': _linear_scale(f.field_width),
                'length': _linear_scale(f.field_length),
                'line_width': _linear_scale(f.line_width),
                'boundary_width': _linear_scale(f.boundary_width),
                'referee_width': _linear_scale(f.referee_width),
                'center_radius': _linear_scale(f.center_circle_radius),
                'defense_radius': _linear_scale(f.defense_radius),
                'defense_stretch': _linear_scale(f.defense_stretch),
                'free_kick_distance': _linear_scale(f.free_kick_from_defense_dist),
                'penalty_spot_distance': _linear_scale(f.penalty_spot_from_field_line_dist),
                'penalty_line_distance': _linear_scale(f.penalty_line_from_spot_dist),
                'goal_width': _linear_scale(f.goal_width),
                'goal_depth': _linear_scale(f.goal_depth),
                'goal_wall_width': _linear_scale(f.goal_wall_width),
            }))

        if packet.HasField('detection'):

            timestamp = packet.detection.t_capture

            for b in packet.detection.balls:
                updates.append(BallUpdate({
                    'timestamp': timestamp,
                    'x': _linear_scale(b.x),
                    'y': _linear_scale(b.y),
                }))

            for r in packet.detection.robots_yellow:
                updates.append(RobotUpdate(base.Yellow, r.robot_id, {
                    'timestamp': timestamp,
                    'x': _linear_scale(r.x),
                    'y': _linear_scale(r.y),
                    'angle': _angular_scale(r.orientation),
                }))

            for r in packet.detection.robots_blue:
                updates.append(RobotUpdate(base.Blue, r.robot_id, {
                    'timestamp': timestamp,
                    'x': _linear_scale(r.x),
                    'y': _linear_scale(r.y),
                    'angle': _angular_scale(r.orientation),
                }))

        return updates


class RealVisionUpdater(VisionUpdater):

    def __init__(self):
        VisionUpdater.__init__(self, ('224.5.23.2', 10002))


class SimVisionUpdater(VisionUpdater):

    def __init__(self):
        VisionUpdater.__init__(self, ('224.5.23.2', 11002))

