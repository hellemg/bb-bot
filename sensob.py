from PIL import Image
import os


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
        self.sensor_get_value()
        if self.debug:
            print("¨¨¨¨Updating sensob: ", self.name)
            print("- sensor value:", self.value)

    def reset(self):
        self.value = None

    def sensor_get_value(self):
        pass

    def get_name(self):
        return self.name


class Ultrasonic(Sensob):
    def sensor_get_value(self):
        self.value = int(input("type front-sensor value: "))


class Reflectance(Sensob):
    def __init__(self):
        super(Reflectance, self).__init__()
        self.min_val = 0.2
        self.max_val = 0.8

    def sensor_get_value(self):
        # Where the black part is
        # Low value means dark
        choice = input(print("Choose where the dark is - right/left/middle/black/white (r/l/m/b/w): "))
        self.value = \
            {'r': [1, 1, 1, 1, 0, 0], 'l': [0, 0, 1, 1, 1, 1], 'm': [1, 0, 0, 0, 0, 1], 'b': [0, 0, 0, 0, 0, 0],
             'w': [1, 1, 1, 1, 1, 1]}[choice]


class Camera(Sensob):
    def __init__(self, img_width=100, img_height=100, img_rot=0):
        super(Camera, self).__init__()
        self.value = None
        self.img_width = img_width
        self.img_height = img_height
        self.img_rot = img_rot
        self.filepath = os.getcwd()

    def sensor_get_value(self):
        self.value = Image.open('red.png').convert('RGB')
