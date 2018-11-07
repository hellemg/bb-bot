from behaviour import *

class ObjectDetection(Behaviour):
    def __int__(self, bbcon, sensobs, target_color = "red", priority = 0.6):
        super(ObjectDetection, self).__int__()
        self.sensobs = sensobs
        self.motor_rec = (0,0)
        self.active_flag = True
        self.halt_request = False
        self.priority = None
        self.match_degree = 0
        self.weight = self.match_degree * self.priority
        self.name = "ObjectDetection"

        self.timestep == 0.8

        self.camera = sensobs[2]
        self.ultrasonic = sensobs[0]
        self.halt_dist = 3
        self.debug = False
        self.target_color = {"red": 0, "green": 1, "blue":2}
        self.color_margin = 0.8
        self.diameter = 2
        self.midMargin = 20

        def sence_and_act(self):
            img = self.camera.get_value()
            result = self.analyze(img)
            if result:
                x, y = result
                if x < self.camera.img_width // 2 - self.midMargin:
                    self.motor_recommendation = (0.0, 0.3)
                    self.timestep = 2 * (self.camera.img_width // 2 - x) / self.camera.img_width
                    self.match_degree = 0.7
                elif x > self.camera.img_width // 2 + self.midMargin:
                    self.motor_recommendation = (0.3, 0.0)
                    self.timestep = 2 * (x - self.camera.img_width // 2) / self.camera.img_width
                    self.match_degree = 0.7
                else:
                    if self.ultrasonic.value < self.halt_dist:
                        self.halt_flag = True
                    else:
                        self.motor_recommendation = (0.3, 0.3)
                        self.match_degree = 0.9
                        self.timestep = 0.5
            else:
                self.motor_recommendation = (0, 0)
                self.match_degree = 0

        def analyze(self, img):
            if img:
                coords = {}
                for i in range(img.size[0]):
                    for j in range(img.size[1]):
                        p = img.getpixel((i, j))
                        correct = True
                        amount = 0
                        for c in (0, 1, 2):
                            if c == self.target_color: continue
                            avg = sum(p) / 3
                            diff = int(p[self.target_color] * self.color_margin - p[c])
                            if diff < 0 or avg > 150 or avg < 20:
                                correct = False
                                break
                            amount += diff
                        if correct:
                            coords[(i, j)] = int(amount // 2)
                            if self.debug:
                                img.putpixel((i, j), (amount, amount, amount))
                        elif self.debug:
                            img.putpixel((i, j), (0, 0, 255))
                for i in range(2):
                    newCoords = {}
                    for k, v in coords.items():
                        delete = False
                        for i in range(self.diameter):
                            for j in range(self.diameter):
                                x = k[0] + i - self.diameter // 2
                                y = k[1] + j - self.diameter // 2
                                if not (x, y) in coords:
                                    delete = True
                                    break
                        if not delete:
                            newCoords[k] = v
                        elif self.debug:
                            img.putpixel((k[0], k[1]), (0, 0, 255))
                    coords = newCoords
                xl = []
                yl = []
                size = 0
                for k, v in coords.items():
                    xl.extend([k[0]] * (v // 5))
                    yl.extend([k[1]] * (v // 5))
                    size += v // 5
                if size:
                    xavg = int(sum(xl) / size)
                    yavg = int(sum(yl) / size)
                    if self.debug:
                        img.putpixel((xavg, yavg), (255, 0, 0))
                        img.save('debug.png')
                    return (xavg, yavg)
                else:
                    if self.debug:
                        img.save('debug.png')
                    return False