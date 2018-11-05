import RPi.GPIO as GPIO
from sensob import *


class IRProximitySensor(Sensob):
    def __init__(self):
        super(IRProximitySensor, self).__init__()
        self.value = None
        self.read_pin_1 = 8
        self.read_pin_2 = 10
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)

    def sensor_get_value(self):
        GPIO.setup(self.read_pin_1, GPIO.IN)
        GPIO.setup(self.read_pin_2, GPIO.IN)
        read_val_1 = GPIO.input(self.read_pin_1)
        read_val_2 = GPIO.input(self.read_pin_2)
        # Invert the values, so that True means something is close
        return [not read_val_1, not read_val_2]
