# File for coding the setup of the modeled scenario.
# This file is meant to be bare-minimum in the first stages of modeling.

# This can be updated later to have automated object creation.
# (i.e. appending device objects to a device list)

from Tower import Tower
from Device import Device

class Parameters():
    # Initial set up for modeling scenario
    def __init__(self):
        print("Creating Towers and Devices..\n")
        t1 = Tower("West tower", (.25,.50), 5, True)
        t2 = Tower("East tower", (.75, .50), 5, True)

        d1 = Device("Bob", [.50, .25], 5, True)
        d2 = Device("Alice", [.25,.50], 5, True)
        
        self.d1 = d1
        self.d2 = d2
        self.t1 = t1
        self.t2 = t2
