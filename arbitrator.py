class Arbitrator:
    def __init__(self, debug=True):
        self.debug = debug
        self.active_behaviours = []

    def choose_action(self):
        chosen_behaviour = None
        max_weight = -5
        for ab in self.active_behaviours:
            # ab.weight: how much to weight the behaviour
            if ab.weight > max_weight:
                max_weight = ab.weight
                chosen_behaviour = ab
        if self.debug:
            print("Chosen behaviour:", chosen_behaviour.name)
            print("- motor_rec:", chosen_behaviour.motor_rec)
            print("- weigth:", chosen_behaviour.weight)
            print("- halt request:", chosen_behaviour.halt_request)
        # choose_behaviour.halt: boolean, whether or not to stop the run
        return (chosen_behaviour.motor_rec, chosen_behaviour.halt_request)

    def add_active_behaviour(self, behaviour):
        self.active_behaviours.append(behaviour)

    def reset_active_behaviours(self):
        self.active_behaviours = []
