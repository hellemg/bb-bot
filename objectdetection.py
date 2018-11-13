from behaviour import *


class ObjectDetection(Behaviour):
    def __init__(self, bbcon, sensobs, target="red", halt_dist = 4.5):
        super(ObjectDetection, self).__init__(sensobs, active_flag=False, priority=0.6)
        self.bbcon = bbcon
        self.camera = self.sensobs[2]
        self.ultrasonic = self.sensobs[0]
        self.halt_dist = halt_dist
        self.target_color = {"red": 0, "green": 1, "blue": 2}[target]
        self.not_target_colors = [i for i in range(3) if i != self.target_color]
        self.color_treshold = 255 / 3

    def consider_deactivation(self):
        #print("xxx OD consider deact")
        #print("returnstuff", self.halt_request)
        return self.halt_request

    def consider_activation(self):
        #If LineFollowing turns of, ObjectDetection should activate
        #print("***OD consider act")
        #print("LF active flag:", self.bbcon.behaviours[1].active_flag)
        #print("my flag: ", not self.bbcon.behaviours[1].active_flag)
        return not self.bbcon.behaviours[1].active_flag

    def check_pixel_for_target(self, pixel):
        """
        :param: tuple (3 values)
        :return: boolean
        """
        return (pixel[self.target_color] > self.color_treshold) and (
                pixel[self.not_target_colors[0]] < self.color_treshold) and (
                       pixel[self.not_target_colors[1]] < self.color_treshold)

    def sense_and_act(self):
        """
        Three regions
        - left: go left
        - middle: go forward
        - right: go right
        New matrix
        - areas that are correct (red yes, blue no, green no) have 1-value, others have 0-value
        Find region
        - count 1s in each region
        """
        img = self.camera.get_value()
        width, height = img.size
        target_matrix = [[0 * c for c in range(width)] for r in range(height)]
        for i in range(width):
            for j in range(height):
                pixel = img.getpixel((i, j))
                # First list in row j, then element i in list
                target_matrix[j][i] = self.check_pixel_for_target(pixel) and 1 or 0
        # Middle is always >= left and right
        left_right_size = int(width / 3)
        middle_size = width - 2 * left_right_size
        left_1s = 0
        middle_1s = 0
        right_1s = 0
        for r in target_matrix:
            for e in r[:left_right_size]:
                if e == 1:
                    left_1s += 1
            for e in r[left_right_size:left_right_size + middle_size]:
                if e == 1:
                    middle_1s += 1
            for e in r[width - left_right_size:]:
                if e == 1:
                    right_1s += 1
        if self.debug:
            print("- left 1s:", left_1s)
            print("- middle 1s:", middle_1s)
            print("- right 1s:", right_1s)
        if (left_1s+middle_1s+right_1s) < 10:
            #Looking around
            self.motor_rec = 'right'
        elif left_1s > middle_1s and left_1s > right_1s:
            self.motor_rec = 'left'
        elif right_1s > middle_1s and right_1s > left_1s:
            self.motor_rec = 'right'
        else:
            self.motor_rec = 'forward'
        self.match_degree = 0.8
        if 0 < self.ultrasonic.get_value() < self.halt_dist:
            self.halt_request = True
        else:
            self.halt_request = False