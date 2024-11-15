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
    t1_x = params.t1.location[0] * WINDOW_SIZE[0]
    t1_y = params.t1.location[1] * WINDOW_SIZE[1]
    canvas.create_oval(t1_x-25, t1_y-25, t1_x+25, t1_y+25, fill="black") # create_oval defines a bounding box

    t2_x = params.t2.location[0] * WINDOW_SIZE[0]
    t2_y = params.t2.location[1] * WINDOW_SIZE[1]
    canvas.create_oval(t2_x-25, t2_y-25, t2_x+25, t2_y+25, fill="black") # create_oval defines a bounding box
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
