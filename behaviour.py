class Behaviour:
    def __init__(self, sensobs, active_flag, priority, debug=True):
        # self.bbcon = bbcon
        self.name = self.__class__.__name__
        self.sensobs = sensobs
        self.active_flag = active_flag
        self.priority = priority
        self.halt_request = False
        self.match_degree = 0
        self.weight = self.priority * self.match_degree
        self.motor_rec = 'forward'
        self.debug = debug

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def set_active_flag(self):
        if self.active_flag:
            self.active_flag = not self.consider_deactivation()
        else:
            self.active_flag = self.consider_activation()

    def update(self):
        if self.debug:
            print("Updating behaviour: ", self.name)
        self.sense_and_act()
        self.set_active_flag()
        self.weight = self.match_degree * self.priority
        if self.debug:
            print("- recommended to drive", self.motor_rec)
            print("- active flag: ", self.active_flag)

    def sense_and_act(self):
        pass
