class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        chosen_behaviour = None
        max_weight = 0
        for ab in self.bbcon.active_behaviours:
            # ab.weight: how much to weight the behaviour
            if ab.weight > max_weight:
                max_weight = ab.weight
                chosen_behaviour = ab
        motor_rec = []
        for m in chosen_behaviour.motobs:
            # m.rec: recommended setting for motor for behaviour
            motor_rec.append(m.rec)
        # choose_behaviour.halt: boolean, whether or not to stop the run
        return (motor_rec, chosen_behaviour.halt)
