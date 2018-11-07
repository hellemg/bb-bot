from behaviour import *

class ObstacleAvoidance(Behaviour):
    def __init__(self, bbcon=None, sensobs=None, priority=1, threshold=2.5):
        self.bbcon = bbcon
        self.sensobs = sensobs
        self.timestep = 0.5
        self.priority = priority
        self.active_flag = True
        self.halt_flag = False
        self.match_degree = 0
        self.weight = self.match_degree * self.priority

        self.ultrasonic = sensobs[0]
        self.front = False
        self.threshold = threshold
        self.motor_recommendation = (0, 0)

        #Constant for later use
        self.turn_right = (0.55, -0.55)

    def get_front(self):
        self.front = self.ultrasonic.get_value() < self.threshold
    """
    def set_threshold(self, threshold):
        self.threshold = threshold
    """

    def sense_and_act(self):
        self.get_front()
        if self.front:
            self.match_degree = 1
            self.motor_recommendation = self.turn_right
        else:
            self.match_degree = 0
            self.motor_recommendation = (0, 0)

    def consider_activation(self):
        False

    def consider_deactivation(self):
        False