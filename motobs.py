class Motobs():
    def __init__(self, debug=True):
        self.value = (0, 0)
        self.debug = debug
        self.name = "Motobs"

    def forward(self, speed=0.25, dur=None):
        if self.debug:
            print("Going forward for %.2f seconds" % dur)
        pass

    def backward(self, speed=0.25, dur=None):
        if self.debug:
            print("Going backwards for %.2f seconds" % dur)

    def left(self, speed=0.25, dur=None):
        if self.debug:
            print("Going left for %.2f seconds" % dur)

    def right(self, speed=0.25, dur=None):
        if self.debug:
            print("Going right for %.2f seconds" % dur)

    def stop(self):
        if self.debug:
            print("Stopping")

    def dance(self):
        if self.debug:
            print("Victory dance!")

    def send_request_to_motors(self, motor_rec, dur):
        if motor_rec == "forward":
            self.forward(dur=dur)
        elif motor_rec == "backward":
            self.backward(dur=dur)
        elif motor_rec == "left":
            self.left(dur=dur)
        elif motor_rec == "right":
            self.right(dur=dur)
        elif motor_rec == "stop":
            self.stop()
        elif motor_rec == "dance":
            self.dance()
