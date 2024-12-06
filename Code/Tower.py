# This class is optionally used for creating tower objects
class Tower():
    def __init__(self, name, location, radius, on, display_added_device=False):
        self.name = name
        self.location = location    # tuple (x,y) where x, y in [0,1]. Canvas is 10x10 miles. x,y are percentages of 10 miles.
        self.radius = radius        # radius in [0,1]. Percentage of 10 miles.
        self.on = on                # T/F
        if display_added_device:
            print("--New tower created--")
            print("Tower name: " + self.name + ".")
            print("Tower location: " + str(self.location) + ".")
            print("Tower radius: " + str(self.radius) + ".")
            print("Tower power status: " + str(int(self.on)) + ".")
        
    # for setting the name of the tower
    def set_name(self, name, display_added_device=False):
        if display_added_device: print(self.name + " updating to " + name + ".")
        self.name = name
        if display_added_device: print("Updated.")

    # turn on or off the tower
    def set_power_status(self, on, display_added_device=False):
        if (self.on != on):
            self.on = on
            if display_added_device: print("Tower " + self.name + "\'s power changed to " + str(int(self.on)) + ".")
        else:
            if display_added_device: print("Tower " + self.name +"\'s power status already set to " + str(int(self.on)) + ".")

    # sets the location of the tower
    def set_location(self, location, display_added_device=False):
        self.location = location
        if display_added_device: print("Tower " + self.name + "\'s location set to " + str(self.location) + ".")

    # sets the radius of the signal of the tower
    def set_radius(self, radius, display_added_device=False):
        self.radius = radius
        if display_added_device: print("Tower " + self.name + "\'s radius set to " + str(self.radius) + ".")

    
