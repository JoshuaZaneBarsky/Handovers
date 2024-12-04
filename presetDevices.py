# File for seting up custom devices

from Tower import Tower
from Device import Device

class presetDevices():
    # Initial set up for modeling scenario
    def __init__(self):
        print("Instantiating Optional Tower and Device Objects..")
        t1 = Tower("West Tower", (.25,.50), .3, True)
        t2 = Tower("East Tower", (.75, .50), .3, True)

        d1 = Device("Bob", [.20, .25], .1, True)
        d2 = Device("Alice", [.80,.75], .1, True)
        print("Done.")
        
        self.d1 = d1
        self.d2 = d2
        self.t1 = t1
        self.t2 = t2
