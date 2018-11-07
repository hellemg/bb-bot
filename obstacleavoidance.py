from behaviour import *

class ObstacleAvoidance(Behaviour):
    def __init__(self, sensobs, priority=1, threshold=2.5, debug = True):
        super(ObstacleAvoidance, self).__init__()
        self.sensobs = sensobs
        self.priority = priority
        self.active_flag = True
        self.halt_request = False
        self.match_degree = 0
        self.weight = self.match_degree * self.priority

        self.ultrasonic = sensobs[0]
        self.front = False
        self.threshold = threshold
        self.motor_recommendation = "stop"
        self.debug = debug

    def get_front(self):
        self.front = self.ultrasonic.get_value() < self.threshold

    def sense_and_act(self):
        self.get_front()
        if self.front:
            if self.debug:
                print("- object in front")
            self.match_degree = 1
            self.motor_recommendation = "right"
        else:
            if self.debug:
                print("- no object in front")
            self.match_degree = 0
            self.motor_recommendation = "stop"

    def consider_activation(self):
        return True

    def consider_deactivation(self):
        return False