from behaviour import *


class ObjectDetection(Behaviour):
    def __init__(self, bbcon, sensobs, target="red", halt_dist=4.5):
        """

        :param bbcon: class BBCon that uses this ObjectDetection-class
        :param sensobs: list, sensobs that the BBCon utilises
        :param target: string, color of object ObjectDetection looks for
        :param halt_dist: float, distance from object that the robot stops
        """
        super(ObjectDetection, self).__init__(sensobs, active_flag=False, priority=0.6)
        self.bbcon = bbcon
        self.camera = self.sensobs[2]
        self.ultrasonic = self.sensobs[0]
        self.halt_dist = halt_dist
        self.target_color = {"red": 0, "green": 1, "blue": 2}[target]
        self.not_target_colors = [i for i in range(3) if i != self.target_color]
        self.color_treshold = 255 / 3

    def consider_deactivation(self):
        return self.halt_request

    def consider_activation(self):
        return not self.bbcon.behaviours[1].active_flag

    def check_pixel_for_target(self, pixel):
        """
        Checks if a pixel contains the target-color
        :param pixel: tuple (3 values)
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
        Find region with most target-color-pixels
        """
        img = self.camera.get_value()
        width, height = img.size
        # Middle is always >= left and right
        left_right_size = int(width / 3)
        middle_size = width - 2 * left_right_size
        target_pixels = {'left': 0, 'forward': 0, 'right': 0}
        for j in range(height):
            for i in range(left_right_size):
                pixel = img.getpixel((i, j))
                if self.check_pixel_for_target(pixel):
                    target_pixels['left'] += 1
                pixel = img.getpixel((left_right_size + middle_size + i, j))
                if self.check_pixel_for_target(pixel):
                    target_pixels['right'] += 1
            for i in range(middle_size):
                pixel = img.getpixel((left_right_size + i, j))
                if self.check_pixel_for_target(pixel):
                    target_pixels['forward'] += 1
        if self.debug:
            print("- left target-color-pixels:", target_pixels['left'])
            print("- forward target-color-pixels:", target_pixels['forward'])
            print("- right target-color-pixels:", target_pixels['right'])
        if sum(target_pixels.values()) < 10:
            # Look around
            self.motor_rec = 'left'
        else:
            self.motor_rec = max(target_pixels, key = target_pixels.get)
        self.match_degree = 0.8
        if 0 < self.ultrasonic.get_value() < self.halt_dist:
            self.halt_request = True
        else:
            self.halt_request = False
