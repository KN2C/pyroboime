#
# Copyright (C) 2013 RoboIME
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
from .. import Tactic
from ...utils.statemachine import Transition
from ..skills.gotolooking import GotoLooking


class ZigZag(Tactic):
    """Goto A then look to B then goto B then look to A then repeat, that's it. """

    def __init__(self, robot, point_a, point_b, deterministic=True):
        self.goto_a = GotoLooking(robot, name='Goto A', target=point_a, lookpoint=point_a, deterministic=deterministic)
        self.orient_a = GotoLooking(robot, name='Orient A', target=point_a, lookpoint=point_b, deterministic=deterministic)
        self.goto_b = GotoLooking(robot, name='Goto B', target=point_b, lookpoint=point_b, deterministic=deterministic)
        self.orient_b = GotoLooking(robot, name='Orient B', target=point_b, lookpoint=point_a, deterministic=deterministic)

        super(ZigZag, self).__init__(robot, deterministic=deterministic, initial_state=self.goto_a, transitions=[
            Transition(self.goto_a, self.orient_a, condition=self.goto_a.arrived),
            Transition(self.orient_a, self.goto_b, condition=self.orient_a.oriented),
            Transition(self.goto_b, self.orient_b, condition=self.goto_b.arrived),
            Transition(self.orient_b, self.goto_a, condition=self.orient_b.oriented),
        ])
