class Behaviour:
    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensobs = None
        self.motor_rec = None
        self.active_flag = True
        self.halt_request = None
        self.priority = None
        self.match_degree = None
        self.weight = None

    def consider_deactivation(self, deactivate):
        """
        :param deactivate: boolean
        """
        if self.active_flag and deactivate:
            self.active_flag = False

    def consider_activation(self, activate):
        """
        :param activate: boolean
        """
        if not self.active_flag and activate:
            self.active_flag = True

    def update(self):
        # TODO: update acitivity status (what does this mean?)
        self.sense_and_act()
        self.weight = self.match_degree * self.priority

    def sense_and_act(self):
        pass


class ObstacleAvoidance:
    def __init__(self, bbcon=None, sensobs=None, priority=0, threshold=2.5):
        self.bbcon = bbcon
        self.sensobs = sensobs
        self.timestep = 0.5
        self.priority = priority
        self.active_flag = True
        self.halt_flag = False
        self.match_degree = 0
        self.weight = self.match_degree * self.priority

        self.ultrasonic = sensobs[0]
        self.ir_sensor = sensobs[1]
        self.sides = [False, False]
        self.front = False
        self.threshold = threshold
        self.motor_recommendation = (0, 0)

        #Constants for later use
        self.turn_right = (0.55, -0.55)
        self.turn_left = (-0.55, 0.55)
        self.turn_around = (-0.8, 0.8)
        self.turn_left_slight = (-0.2, 0.2)
        self.turn_right_slight = (0.2, -0.2)

    def get_sides(self):
        self.sides = self.ir_sensor.get_value()

    def get_front(self):
        self.front = self.ultrasonic.get_value() < self.threshold
    """
    def set_threshold(self, threshold):
        self.threshold = threshold
    """

    def sense_and_act(self):
        self.get_sides()
        self.get_front()
        match = 1
        left, right = self.sides
        if self.front:
            motors = self.turn_around
            if not right:
                motors = self.turn_right
            elif not left:
                motors = self.turn_left
        elif left and right:
            motors = self.turn_around
        elif left:
            motors = self.turn_right_slight
        elif right:
            motors = self.turn_left_slight
        else:
            match = 0
            motors = (0, 0)
        self.match_degree = match
        self.weight = match * self.priority
        self.motor_recommendation = motors
