import time
from obstacleavoidance import *
from arbitrator import *
from motobs import *
from sensob import *

class BBCon:
    def __init__(self, debug = True):
        self.sensobs = [FakeUltrasonic()]
        self.active_behaviours = []
        self.motobs = [Motobs()]
        self.behaviours = [ObstacleAvoidance(self.sensobs)]
        self.arbitrator = Arbitrator()
        self.timestep = 1
        self.debug = debug

    def add_behaviour(self, behaviour):
        self.behaviours.append(behaviour)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def activate_behaviour(self, behaviour):
        if not behaviour in self.behaviours:
            raise ValueError("Unknown behaviour: %r" % behaviour)
        self.active_behaviours.append(behaviour)

    def deactivate_behaviour(self, behaviour):
        if not behaviour in self.active_behaviours:
            raise ValueError("Not active behaviour: %r" % behaviour)
        self.active_behaviours.remove(behaviour)

    def wait(self, seconds):
        time.sleep(seconds)

    def decide_active_behaviours(self):
        for ab in self.active_behaviours:
            if ab.consider_deactivation():
                self.deactivate_behaviour(ab)
        for b in self.behaviours:
            if b.consider_activation():
                self.activate_behaviour(b)
        for ab in self.active_behaviours:
            self.arbitrator.add_active_behaviour(ab)

    def run_one_timestep(self):
        for s in self.sensobs:
            s.update()
        for b in self.behaviours:
            b.update()
        self.decide_active_behaviours()
        motor_rec, halt_flag = self.arbitrator.choose_action()
        self.motobs[0].send_request_to_motors(motor_rec, self.timestep)
        self.wait(self.timestep)
        for s in self.sensobs:
            s.reset()
        if halt_flag:
            quit()

