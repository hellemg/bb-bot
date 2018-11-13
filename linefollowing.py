from behaviour import *


class LineFollowing(Behaviour):
    def __init__(self, sensobs):
        super(LineFollowing, self).__init__(sensobs, active_flag=True, priority=0.6)
        self.have_been_active = True
        self.reflectance = self.sensobs[1]
        # Sensorvalue range: [0,1]. 0 means dark
        self.min_sensor_value = 0.4#min(self.reflectance.min_val)
        self.max_sensor_value = 1#max(self.reflectance.max_val)
        self.middle_sensor_value = (self.min_sensor_value + self.max_sensor_value) / 2
        self.sensor_values = [-1, -1, -1, -1, -1, -1]

    def consider_activation(self):
        """
        Activate if:
        - You haven't been activated earlier
        """
        returnstuff = not self.have_been_active
        # self.have_been_active = True
        if self.debug:
            print("LF consider activation. returnstuff and have been active:", returnstuff, self.have_been_active)
        return returnstuff

    def consider_deactivation(self):
        """
        Deactivate if:
        - Everything is dark (reached a blob)
        """
        print("LF consider deact:", self.motor_rec)
        return self.motor_rec == 'stop'

    def get_bottom(self):
        self.sensor_values = self.reflectance.get_value()

    def change(self, j, k):
        # Is the sensor-value at index j different from the one at index k?
        if self.sensor_values[j] != self.sensor_values[k]:
            return True
        return False

    def index_of_change(self):
        # Returns index of change (2-6). If no change, returns 10. Only checks first change
        for i in range(5):
            if self.change(i, i + 1):
                return i + 1
        return 10

    def is_white(self, j):
        # Is the sensor-value at index j white
        return self.sensor_values[j] == 1

    def is_black(self, j):
        # Is the sensor-value at index j black
        return self.sensor_values[j] == 0

    def sense_and_act(self):
        """
        Cases:
        - Everything is dark: Stop
        - Middle is dark: Go straight ahead
        - Everything is white: Continue straight ahead
        - One side is dark: Turn to dark side
        """
        # Sets self.sensor_values to 6-element array
        self.get_bottom()
        # Making it black and white
        for i, e in enumerate(self.sensor_values):
            if e < self.middle_sensor_value:
                self.sensor_values[i] = 0
            else:
                self.sensor_values[i] = 1
        # Find change if it exists
        change_index = self.index_of_change()
        if self.is_white(0):
            if change_index != 10:
                # Black stripe in the middle
                if self.is_white(5):
                    if self.debug:
                        print("- black in the middle, white on edges")
                    self.motor_rec = 'forward'
                    self.match_degree = 0.8
                # Black to the right, follow it
                else:
                    if self.debug:
                        print("- black to the right, white to the left")
                    self.motor_rec = 'right'
                    self.match_degree = (change_index - 1) * 2 / 10
            else:
                # Everything is white
                if self.debug:
                    print("- everything is white")
                self.motor_rec = 'forward'
                self.match_degree = 0.8
        elif self.is_black(0):
            if change_index != 10:
                # Black to the left, follow it
                if self.debug:
                    print("- black to the left, white to the right")
                self.motor_rec = 'left'
                self.match_degree = 1 - (change_index - 1) * 2 / 10
            else:
                # Everything is black, woho!
                if self.debug:
                    print("- everything is black")
                self.motor_rec = 'stop'
                self.match_degree = 1
