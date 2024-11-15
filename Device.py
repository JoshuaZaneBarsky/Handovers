class Device():
    def __init__(self, name, location, radius, on):
        self.name = name
        self.location = location    # list [x,y] where x, y in [0,1]. Canvas is 10x10 miles. x,y are percentages of 10 miles.
        self.radius = radius        # radius in [0,1]. Percentage of 10 miles.
        self.on = on                # T/F
        print("--New device created--")
        print("Device name: " + self.name + ".")
        print("Device location: " + str(self.location) + ".")
        print("Device radius: " + str(self.radius) + ".")
        print("Device power status: " + str(int(self.on)) + ".")
        

    def set_name(self, name):
        print(self.name + " updating to " + name + ".")
        self.name = name
        print("Updated.")

    def set_power_status(self, on):
        if (self.on != on):
            self.on = on
            print("Device " + self.name + "\'s power changed to " + str(int(self.on)) + ".")
        else:
            print("Device " + self.name +"\'s power status already set to " + str(int(self.on)) + ".")

    def set_location(self, location):
        self.location = location
        print("Device " + self.name + "\'s location set to " + str(self.location) + ".")

    def set_radius(self, radius):
        self.radius = radius
        print("Device " + self.name + "\'s radius set to " + str(self.radius) + ".")
        
