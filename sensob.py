class Sensob:
    def __init__(self):
        self.value = None
        self.setup()

    def setup(self):
        pass

    def get_value(self):
        return self.value

    def update(self):
        self.value = self.sensor_get_value()
        return self.value

    def reset(self):
        self.value = None

    def sensor_get_value(self):
        return None