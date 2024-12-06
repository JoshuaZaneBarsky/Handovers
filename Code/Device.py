# This class is optionally used for creating device objects
class Device():
    def __init__(self, name, location, radius, on, display_added_device = False):
        self.name = name
        self.location = location    # list [x,y] where x, y in [0,1]. Canvas is 10x10 miles. x,y are percentages of 10 miles.
        self.radius = radius        # radius in [0,1]. Percentage of 10 miles.
        self.on = on                # T/F
        if display_added_device:
            print("--New device created--")
            print("Device name: " + self.name + ".")
            print("Device location: " + str(self.location) + ".")
            print("Device radius: " + str(self.radius) + ".")
            print("Device power status: " + str(int(self.on)) + ".")
        
    # sets the name of the device
    def set_name(self, name, display_added_device=False):
        if display_added_device: print(self.name + " updating to " + name + ".")
        self.name = name
        if display_added_device: print("Updated.")

    # turns on or off the device
    def set_power_status(self, on, display_added_device=False):
        if (self.on != on):
            self.on = on
            if display_added_device: print("Device " + self.name + "\'s power changed to " + str(int(self.on)) + ".")
        else:
            if display_added_device: print("Device " + self.name +"\'s power status already set to " + str(int(self.on)) + ".")

    # sets the location of the device
    def set_location(self, location, display_added_device=False):
        self.location = location
        if display_added_device: print("Device " + self.name + "\'s location set to " + str(self.location) + ".")

    # sets the signal radius of the device
    def set_radius(self, radius, display_added_device=False):
        self.radius = radius
        if display_added_device: print("Device " + self.name + "\'s radius set to " + str(self.radius) + ".")
        
