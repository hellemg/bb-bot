from behaviour import *

class LineFollowing(Behaviour):
    def __init__(self):
        super(LineFollowing, self).__init__()
        self.have_been_active = False
        #Range: [0,1]. Low values means dark
        #self.value = [-1, -1, -1, -1, -1, -1]

    def consider_activation(self):
        """
        Activate if:
        - You haven't been activated earlier
        """
        return not self.have_been_active

    def consider_deactivation(self):
        # TODO: Implement
        """
        Deactivate if:
        - Everything is dark (reached a blob)
        """

    def sense_and_act(self):
        # TODO: Implement
        """
        Cases:
        - Everything is dark: Continue straight ahead
        - Everything is white: Continue straight ahead
        - One side is dark: Turn to dark side
        - Middle is dark: Go straight ahead
        """


