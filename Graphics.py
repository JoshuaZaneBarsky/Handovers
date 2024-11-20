from tkinter import *
from PIL import Image, ImageTk # For displaying images
from Parameters import Parameters
from random import *

WINDOW_SIZE = [800,800]


def initialize(params, canvas, model, mainWindow):
    pass

def mousePressed(params, event, canvas, model):
    pass
 
def redraw(params, canvas, model):
    # temporary --> Draw t1
    t1_x = params.t1.location[0] * WINDOW_SIZE[0]
    t1_y = params.t1.location[1] * WINDOW_SIZE[1]
    canvas.create_text(t1_x, t1_y-25, text=params.t1.name, font=("Arial", 12, "bold"), fill="blue")
    canvas.create_polygon(t1_x+15, t1_y+15, t1_x-15, t1_y+15, t1_x+0, t1_y-15, fill="black") # create_oval defines a bounding box
    canvas.create_oval(t1_x-(WINDOW_SIZE[0]*params.t1.radius), t1_y-(WINDOW_SIZE[1]*params.t1.radius), t1_x+(WINDOW_SIZE[0]*params.t1.radius), t1_y+(WINDOW_SIZE[1]*params.t1.radius), dash=(4,2)) # create_oval defines a bounding box

    # temporary --> Draw t2
    t2_x = params.t2.location[0] * WINDOW_SIZE[0]
    t2_y = params.t2.location[1] * WINDOW_SIZE[1]
    canvas.create_text(t2_x, t2_y-25, text=params.t2.name, font=("Arial", 12, "bold"), fill="blue")
    canvas.create_polygon(t2_x+15, t2_y+15, t2_x-15, t2_y+15, t2_x+0, t2_y-15, fill="black") # create_oval defines a bounding box
    canvas.create_oval(t2_x-(WINDOW_SIZE[0]*params.t2.radius), t2_y-(WINDOW_SIZE[1]*params.t2.radius), t2_x+(WINDOW_SIZE[0]*params.t2.radius), t2_y+(WINDOW_SIZE[1]*params.t2.radius), dash=(4,2)) # create_oval defines a bounding box
    canvas.update()

    # temporary --> Draw d1
    d1_x = params.d1.location[0] * WINDOW_SIZE[0]
    d1_y = params.d1.location[1] * WINDOW_SIZE[1]
    canvas.create_text(d1_x, d1_y-25, text=params.d1.name, font=("Arial", 12, "bold"), fill="blue")
    canvas.create_polygon(d1_x+15, d1_y+15, d1_x-15, d1_y+15, d1_x-15, d1_y-15, d1_x+15, d1_y-15, fill="black") # create_oval defines a bounding box
    # canvas.create_oval(d1_x-(WINDOW_SIZE[0]*params.d1.radius), d1_y-(WINDOW_SIZE[1]*params.d1.radius), d1_x+(WINDOW_SIZE[0]*params.d1.radius), d1_y+(WINDOW_SIZE[1]*params.d1.radius), dash=(4,2)) # create_oval defines a bounding box

    # temporary --> Draw d2
    d2_x = params.d2.location[0] * WINDOW_SIZE[0]
    d2_y = params.d2.location[1] * WINDOW_SIZE[1]
    canvas.create_text(d2_x, d2_y-25, text=params.d2.name, font=("Arial", 12, "bold"), fill="blue")
    canvas.create_polygon(d2_x+15, d2_y+15, d2_x-15, d2_y+15, d2_x-15, d2_y-15, d2_x+15, d2_y-15, fill="black") # create_oval defines a bounding box
    # canvas.create_oval(d2_x-(WINDOW_SIZE[0]*params.d2.radius), d2_y-(WINDOW_SIZE[1]*params.d2.radius), d2_x+(WINDOW_SIZE[0]*params.d2.radius), d2_y+(WINDOW_SIZE[1]*params.d2.radius), dash=(4,2)) # create_oval defines a bounding box
    canvas.update()


    pass



def run(width = 800, height = 800):
    class Struct(): pass
    model = Struct()
    model.width = width
    model.height = height

    params = Parameters()
    
    mainWindow = Tk()
    canvas = Canvas(mainWindow, width = model.width, height = model.height)
    canvas.pack()

    initialize(params, canvas, model, mainWindow)


    def redrawWrapper(params, canvas, model):
        canvas.delete(ALL)
        redraw(params, canvas, model)
        canvas.update()

    def mousePressWrapper(params, event, canvas, model):
        mousePressed(params, event, canvas, model)
        redrawWrapper(params, canvas, model)

    mainWindow.bind("<Button-1>", lambda event: mousePressWrapper(params, event, canvas, model))

    redrawWrapper(params, canvas, model)

    mainWindow.mainloop()

run() 
