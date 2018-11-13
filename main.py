from bbcon import *
from zumo_button import *

if __name__ == '__main__':
    print("Running BBCon")
    BBCon = BBCon()
    ZumoButton().wait_for_press()
    while 1:
        BBCon.run_one_timestep()
