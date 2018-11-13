from bbcon import *
from zumo_button import *
from robodemo import *


def dancer():
    ZumoButton().wait_for_press()
    m = Motors()
    m.forward(.2, 3)
    m.backward(.2, 3)
    m.right(.5, 3)
    m.left(.5, 3)
    m.backward(.3, 2.5)
    m.set_value([.5, .1], 10)
    m.set_value([-.5, -.1], 10)


if __name__ == '__main__':
    print("Running BBCon")

    dancer()
    """
    BBCon = BBCon()
    ZumoButton().wait_for_press()
    while 1:
        BBCon.run_one_timestep()
    """
