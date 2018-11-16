import time
from obstacleavoidance import *
from linefollowing import *
from objectdetection import *
from arbitrator import *
from motobs import *
#from motors import *
from sensob import *
#from reflectance_sensors import *
#from camera import *
#from ultrasonic import *


class BBCon:
    def __init__(self, debug=True):
        self.sensobs = [Ultrasonic(), Reflectance(), Camera()]
        self.active_behaviours = []
        self.motobs = [Motobs()]
        self.behaviours = [ObstacleAvoidance(self.sensobs), LineFollowing(self.sensobs), ObjectDetection(self, self.sensobs)]
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
        if self.debug:
            print("¨¨¨¨Deciding active behaviors")
        for ab in self.active_behaviours:
            #if self.debug:
                #print("- Considering active behaviour:", ab.name)
            if not ab.active_flag:
                self.deactivate_behaviour(ab)
                if self.debug:
                    print("-",ab.name,"has been deactivated")
        for b in self.behaviours:
            if b.active_flag and b not in self.active_behaviours:
                self.activate_behaviour(b)
                if self.debug:
                    print("-", b.name,"has been activated")
        self.arbitrator.reset_active_behaviours()
        for ab in self.active_behaviours:
            self.arbitrator.add_active_behaviour(ab)

    def run_one_timestep(self):
        if self.debug:
            print("--------------new timestep---------------")
        for s in self.sensobs:
            s.update()
        for b in self.behaviours:
            b.update()
        self.decide_active_behaviours()
        if self.debug:
            print("Active behaviours")
            for ab in self.active_behaviours:
                print("-", ab.name)
        motor_rec, halt_flag = self.arbitrator.choose_action()
        if halt_flag:
            self.motobs[0].send_request_to_motors('dance', self.timestep)
            self.motobs[0].send_request_to_motors('stop', self.timestep)
            quit()
        self.motobs[0].send_request_to_motors(motor_rec, self.timestep)
        #self.wait(self.timestep)
        for s in self.sensobs:
            s.reset()
