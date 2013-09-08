from multiprocessing import Process, Queue, Event, Lock

from ..utils import keydefaultdict
from ..base import World
from ..core import skills
from ..core import Skill


class Controller(object):

    def __init__(self, interface, colour, world=None):
        if world is not None:
            self.world = world
        else:
            self.world = World()
        self.interface = interface
        self.color = colour
        self.skill_dict = keydefaultdict(lambda r: {
            name: getattr(skills, name)(r)
            for name
            in dir(skills)
            if hasattr(getattr(skills, name), "__bases__")
            and Skill in getattr(skills, name).__bases__
        })
        self.command_queue = Queue()

    def step(self):
        command_list = self.command_queue.get()

        self.interface.step_updaters()
        for robot in self.team:
            if robot.uid in command_list:
                robot_command = command_list[robot.uid]
                skill = self.skill_dict[robot][robot_command["_class"]]
                for attr, value in robot_command.iteritems():
                    if attr == "_class":
                        continue
                    setattr(skill, attr, value)
                # Set skill parameter before stepping once we separate
                skill._execute_step()
        # Publish robot actions to the action queue
        self.interface.step_commanders()

    @property
    def team(self):
        return self.world.team(self.color)
