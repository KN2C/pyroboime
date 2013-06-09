from random import random


class State(object):
    def __init__(self, deterministic, name="State"):
        self.deterministic = deterministic
        self.name = name

    def __repr__(self):
        return self.name


class Transition(object):
    def __init__(self, from_state, to_state, probability=1.0, condition=None):
        """
        This class can be used in two ways:
        - subclass it and redefine the condition method
        - pass a condition function while constructing
        """
        self.from_state = from_state
        self.to_state = to_state
        self.probability = probability
        self._condition = condition

    def condition(self):
        if self._condition is not None:
            return self._condition()


class Machine(object):
    #def __init__(self, deterministic, initial_state=None, final_state=None, transitions=[]):
    def __init__(self, deterministic, initial_state=None, transitions=[]):
        self.deterministic = deterministic
        #self.initial_state = initial_state
        #self.final_state = final_state
        self.current_state = initial_state
        self.transitions = transitions

    def execute(self):
        possible_transitions = [t for t in self.transitions if t.from_state is self.current_state and t.condition() ]
        if self.deterministic:
            if possible_transitions:
                self.current_state = possible_transitions[0].to_state
        else:
            total_prob = sum(t.probability for t in possible_transitions)
            rand_prob = total_prob * random()
            tmp_prob = 0.0
            for t in possible_transitions:
                tmp_prob += t.probability
                if rand_prob < tmp_prob:
                    self.current_state = t.to_state
                    break
