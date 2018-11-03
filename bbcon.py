import time


class BBCon:
    def __init__(self):
        self.behaviours = []
        self.active_behaviours = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = None

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

    def run_one_timestep(self):
        for s in self.sensobs:
            s.update()
        for b in self.behaviours:
            b.update()
        self.arbitrator.choose_action()
        # TODO: update motobs
        self.wait()
        for s in self.sensobs:
            s.reset()

    def wait(self, seconds=0.5):
        time.sleep(seconds)
