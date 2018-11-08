class Sensob:
    def __init__(self, debug=True):
        self.name = self.__class__.__name__
        self.value = None
        self.debug = debug
        self.setup()

    def setup(self):
        pass

    def get_value(self):
        return self.value

    def update(self):
        self.value = self.sensor_get_value()
        if self.debug:
            print("Updating sensob: ", self.name)
            print("- sensor value:", self.value)
        # return self.value

    def reset(self):
        self.value = None

    def sensor_get_value(self):
        pass

    def get_name(self):
        return self.name


class FakeUltrasonic(Sensob):
    def sensor_get_value(self):
        return int(input("type front-sensor value: "))


class FakeReflectance(Sensob):
    def __init__(self):
        super(FakeReflectance, self).__init__()
        self.min_val = 0.2
        self.max_val = 0.8

    def sensor_get_value(self):
        # Where the black part is
        # Low value means dark
        choice = input(print("Choose where the dark is - right/left/middle/black/white (r/l/m/b/w): "))
        return {'r': [1, 1, 1, 1, 0, 0], 'l': [0, 0, 1, 1, 1, 1], 'm': [1, 0, 0, 0, 0, 1], 'b': [0, 0, 0, 0, 0, 0],
                'w': [1, 1, 1, 1, 1, 1]}[choice]
