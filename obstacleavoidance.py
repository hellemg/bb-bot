from behaviour import *


class ObstacleAvoidance(Behaviour):
    def __init__(self, sensobs, threshold=2.5):
        super(ObstacleAvoidance, self).__init__(sensobs, active_flag=True, priority=0.95)
        self.ultrasonic = sensobs[0]
        self.front = False
        self.threshold = threshold

    def get_front(self):
        self.front = self.ultrasonic.get_value() < self.threshold

    def sense_and_act(self):
        self.get_front()
        if self.front:
            if self.debug:
                print("- object in front")
            self.match_degree = 1
            self.motor_rec = "right"
        else:
            if self.debug:
                print("- no object in front")
            self.match_degree = 0
            self.motor_rec = "stop"

    def consider_activation(self):
        self.active_flag = True

    def consider_deactivation(self):
        self.active_flag = True
