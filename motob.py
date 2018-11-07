#import motors
class Motob:
    def __init__(self):
        self.value = [0,0]

    def update(self, direction_right, reverse, rotation): 
        if reverse: 
            r = -1
        else:
            r = 1
        if rotation == 0:
            self.value = [r,r]
        else:
            if direction_right:
               self.value = [r,(1-rotation/90)*r]
            else: #direction left
                self.value = [r*(1-rotation/90), r]
        self.operationalize()
    def operationalize(self):
        return
        motor.set_value(self.value)

m = Motob();
m.update(False, False, 10)
