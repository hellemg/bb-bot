class Sensob:
    def __init__(self):
        self.value = None

    def update(self):
        pass

    def get_value(self):
        pass

    def reset(self):
        self.value = None

class IR(Sensob):
    def __int__(self):
        super(IR, self).__int__()
