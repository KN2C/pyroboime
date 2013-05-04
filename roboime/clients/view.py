from Tkinter import Canvas, Frame, Tk, CHORD, NSEW
#import ttk
#from math import pi as PI

from ..base import World
#from ..interface.updater import SimVisionUpdater
from ..interface import SimulationInterface

FIELD_GREEN = '#3a0'
YELLOW = '#ff0'
BLUE = '#00f'
GREEN = '#0f0'
PINK = '#f0f'
BLACK = '#000'
ORANGE = '#f80'


class FieldCanvas(Canvas):

    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)

        #TODO: make the following dynamic
        self.radius = 0.18
        self.ball_radius = 0.05
        self.anglespan = 260
        self.field_length = 6.0
        self.field_width = 4.0
        self.field_radius = 0.5
        self.field_margin = 1.0
        self.goal_depth = 0.2
        self.goal_width = 0.7

        self['bg'] = FIELD_GREEN
        self['width'] = 100 * (self.field_length + 2 * self.field_margin)
        self['height'] = 100 * (self.field_width + 2 * self.field_margin)
        self.robots = {}
        self.balls = {}

        # lines
        self.bounds = self.create_rectangle(
            self._cx(-self.field_length / 2),
            self._cy(-self.field_width / 2),
            self._cx(self.field_length / 2),
            self._cy(self.field_width / 2),
            outline='white',
            width=3)
        self.midline = self.create_line(
            self._cx(0),
            self._cy(-self.field_width / 2),
            self._cx(0),
            self._cy(self.field_width / 2),
            fill='white',
            width=3)
        self.center = self.create_oval(
            self._cx(-self.field_radius),
            self._cy(-self.field_radius),
            self._cx(self.field_radius),
            self._cy(self.field_radius),
            outline='white',
            width=3
        )

    def _cx(self, x):
        'Convert internal x coord to canvas x coord'
        return 100 * (self.field_length / 2 + self.field_margin + x)

    def _cy(self, y):
        'Convert internal x coord to canvas x coord'
        return 100 * (self.field_width / 2 + self.field_margin - y)

    def _cc(self, x, y):
        'Convert to canvas coords.'
        return (self._cx(x), self._cy(y))

    def draw_robot(self, robot):
        if id(robot) in self.robots:
            r = self.robots[id(robot)]
        else:
            r = self.robots[id(robot)] = self.create_arc(
                0, 0, 0, 0,
                outline='',
                style=CHORD,
                extent=self.anglespan)

        self.coords(
            r,
            self._cx(robot.x - self.radius),
            self._cy(robot.y - self.radius),
            self._cx(robot.x + self.radius),
            self._cy(robot.y + self.radius),
        )
        self.itemconfig(r, start=(robot.angle + 180 - self.anglespan / 2))
        self.itemconfig(r, fill=YELLOW if robot.team.is_yellow else BLUE)

    def draw_ball(self, ball):
        if id(ball) in self.balls:
            b = self.balls[id(ball)]
        else:
            b = self.balls[id(ball)] = self.create_oval(
                0, 0, 0, 0,
                outline='')

        self.coords(
            b,
            self._cx(ball.x - self.ball_radius),
            self._cy(ball.y - self.ball_radius),
            self._cx(ball.x + self.ball_radius),
            self._cy(ball.y + self.ball_radius),
        )
        self.itemconfig(b, fill=ORANGE)

    def delete_robot(self, rid):
        if rid in self.robots:
            self.delete(self.robots[rid])
            del self.robots[rid]

    def draw_field(self, world):
        # TODO: redraw field size if changed
        self.draw_ball(world.ball)
        # draw all robots on the field
        for r in world.iterrobots():
            self.draw_robot(r)
        # remove missing robots
        rids = map(lambda r: id(r), world.iterrobots())
        for r in self.robots.iterkeys():
            if r not in rids:
                self.delete_robot(r)


class View(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.world = World()
        #self.updater = SimVisionUpdater(self.world)
        self.interface = SimulationInterface(self.world)

        self.title('Sample python client.')
        # TODO: make this possible
        self.resizable(width=False, height=False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.content = Frame(self)
        self.content.grid(row=0, column=0, sticky=NSEW)

        self.canvas = FieldCanvas(self.content)
        self.canvas.grid(row=0, column=0, sticky=NSEW)

    def redraw(self):
        #if len(self.world.blue_team) > 0:
        if 0 in self.world.blue_team:
            r = self.world.blue_team[0]
            #import pudb; pudb.set_trace()
            #print 'hey'
            a = r.action
            a.x = 0.0
            a.y = 0.0
            a.angle = 0.0
        #try:
        #    self.interface.step()
        #except:
        ##    pass
        ##finally:
        #    self.interface.stop()
        #else:
        #    self.canvas.draw_field(self.world)
        #    # how long should we wait?
        #    self.after(10, self.redraw)
        self.interface.step()
        self.canvas.draw_field(self.world)
        # how long should we wait?
        self.after(10, self.redraw)

    def mainloop(self):
        self.interface.start()
        self.redraw()
        Tk.mainloop(self)
        self.interface.stop()
