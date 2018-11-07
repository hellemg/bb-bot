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

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def update(self):
        if self.active_flag:
            self.active_flag = not self.consider_deactivation()
        else:
            self.active_flag = self.consider_activation()
        self.sense_and_act()
        self.weight = self.match_degree * self.priority

    def sense_and_act(self):
        pass
