from tkinter import *
from PIL import Image, ImageTk
from presetDevices import presetDevices
from random import *
from csv import *
from Data import Data
import time
import threading # (optional)

WINDOW_SIZE = [800,610]

# real map bounds of background image
HIGHEST_LATITUDE = 33.979672
LOWEST_LATITUDE = 33.968959
HIGHEST_LONGITUDE = -117.316927
LOWEST_LONGITUDE = -117.333857

# data for program to use
csv_files_to_open = ["Data/parking_srv_to_botanic_grdn.csv", "Data/around_campus.csv", "Data/across_ucr.csv"] # list of files
data = []

pause = False # (optional)

# initializes the file data needed for the program
def initialize(preset_devices, canvas,  mainWindow, data, csv_files_to_open):
    for i in range(len(csv_files_to_open)):
        read_csv_file(csv_files_to_open[i],data[i])
    pass

# triggers when the mouse press event occurs
def mousePressed(preset_devices, event, canvas):
    # what can we do on mouse pressed?
    # should there be buttons?
    # should there be images?
    pass

# draws all items to the canvas
def redraw(preset_devices, canvas,  data):
    try: # Draws the map background
        image = Image.open("Images/ucr_map.png")
        original_width, original_height = image.size
        image = image.resize((int(original_width*.5), int(original_height*.5)))
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image=photo, anchor=NW)
        canvas.image = photo
    except Exception as e:
        error_label = Label(canvas, text=f"Error loading image: {e}", fg="red")
        error_label.pack()
    """
    # temporary --> Draw t1
    t1_x = preset_devices.t1.location[0] * WINDOW_SIZE[0]
    t1_y = preset_devices.t1.location[1] * WINDOW_SIZE[1]
    canvas.create_text(t1_x, t1_y-25, text=preset_devices.t1.name, font=("Arial", 12, "bold"), fill="blue")
    canvas.create_polygon(t1_x+15, t1_y+15, t1_x-15, t1_y+15, t1_x+0, t1_y-15, fill="black") # create_oval defines a bounding box
    canvas.create_oval(t1_x-(WINDOW_SIZE[0]*preset_devices.t1.radius), t1_y-(WINDOW_SIZE[1]*preset_devices.t1.radius), t1_x+(WINDOW_SIZE[0]*preset_devices.t1.radius), t1_y+(WINDOW_SIZE[1]*preset_devices.t1.radius), dash=(4,2)) # create_oval defines a bounding box

    # temporary --> Draw t2
    t2_x = preset_devices.t2.location[0] * WINDOW_SIZE[0]
    t2_y = preset_devices.t2.location[1] * WINDOW_SIZE[1]
    canvas.create_text(t2_x, t2_y-25, text=preset_devices.t2.name, font=("Arial", 12, "bold"), fill="blue")
    canvas.create_polygon(t2_x+15, t2_y+15, t2_x-15, t2_y+15, t2_x+0, t2_y-15, fill="black") # create_oval defines a bounding box
    canvas.create_oval(t2_x-(WINDOW_SIZE[0]*preset_devices.t2.radius), t2_y-(WINDOW_SIZE[1]*preset_devices.t2.radius), t2_x+(WINDOW_SIZE[0]*preset_devices.t2.radius), t2_y+(WINDOW_SIZE[1]*preset_devices.t2.radius), dash=(4,2)) # create_oval defines a bounding box
    canvas.update()

    # temporary --> Draw d1
    d1_x = preset_devices.d1.location[0] * WINDOW_SIZE[0]
    d1_y = preset_devices.d1.location[1] * WINDOW_SIZE[1]
    canvas.create_text(d1_x, d1_y-25, text=preset_devices.d1.name, font=("Arial", 12, "bold"), fill="blue")
    canvas.create_polygon(d1_x+15, d1_y+15, d1_x-15, d1_y+15, d1_x-15, d1_y-15, d1_x+15, d1_y-15, fill="black") # create_oval defines a bounding box
    # canvas.create_oval(d1_x-(WINDOW_SIZE[0]*preset_devices.d1.radius), d1_y-(WINDOW_SIZE[1]*preset_devices.d1.radius), d1_x+(WINDOW_SIZE[0]*preset_devices.d1.radius), d1_y+(WINDOW_SIZE[1]*preset_devices.d1.radius), dash=(4,2)) # create_oval defines a bounding box

    # temporary --> Draw d2
    d2_x = preset_devices.d2.location[0] * WINDOW_SIZE[0]
    d2_y = preset_devices.d2.location[1] * WINDOW_SIZE[1]
    canvas.create_text(d2_x, d2_y-25, text=preset_devices.d2.name, font=("Arial", 12, "bold"), fill="blue")
    canvas.create_polygon(d2_x+15, d2_y+15, d2_x-15, d2_y+15, d2_x-15, d2_y-15, d2_x+15, d2_y-15, fill="black") # create_oval defines a bounding box
    # canvas.create_oval(d2_x-(WINDOW_SIZE[0]*preset_devices.d2.radius), d2_y-(WINDOW_SIZE[1]*preset_devices.d2.radius), d2_x+(WINDOW_SIZE[0]*preset_devices.d2.radius), d2_y+(WINDOW_SIZE[1]*preset_devices.d2.radius), dash=(4,2)) # create_oval defines a bounding box
    """
    for i in range(len(data)):
        animate_path(canvas, data[i])
        # (threads not working)
        #thread = threading.Thread(target=animate_path(canvas, data[i])) # (optional)
        #thread.start() # (optional)
    canvas.update()
    
    pass

def quick_stats(): # (optional)
    pass

def legend(): # (optional)
    pass

def donothing(): # for testing purposes
    print("This does nothing.")

# text for each display pop-up window
def get_display_text(option):
    dict = {"pdf" : 0,
            "txt" : 1,
            "exit" : 2,
            "tower" : 3,
            "device" : 4,
            "stats" : 5,
            "help" : 6,
            "info" : 7,
            "credit" : 8
            }
    index = ["Use this option to save your data onto a PDF file.",
             "Use this option to save your data onto a TXT file.",
             "Are you sure you would like to exit the program?\n\n\nYou will need to save your data manually.\n\nFile>Save raw data as .pdf\nFile>Save raw data as .txt",
             "Use this option to add a tower to your model.",
             "Use this option to add a device to your model.",
             "Use this option to display all model stats.",
             "Use this option for help.",
             "Handover Project\nFall 2024\n\nDescription of program:\nThis program is meant to simulate a modeled \nhandover event in order to help the user gain better \nfoundational knowledge into the analytic data \nbehind a 5G handover.",
             "Project credit:\nJoshua Barsky\nNicko Martinez\nParikshit Kumar\n\nCS260: Seminar\nProfessor Zhaowei Tan\nFall 2024\nUniversity of California, Riverside"
             ]
    return index[dict[option]]

# (optional) Gets the radius that was set by the user, when adding a tower.
def get_radius_value(radius_var, radius_label):
    print(radius_var.get())
    selection = "Radius = " + str(radius_var.get())
    radius_label.config(text = selection)

# adds buttons to each pop-up windows
def add_buttons_if_needed(popup_window, window_type):
    if window_type == "exit":
        exit_button = Button(popup_window, text="exit", command=exit)
        exit_button.pack(side = 'bottom')
        cancel_button = Button(popup_window, text="cancel", command=popup_window.destroy)
        cancel_button.pack(side = 'bottom')
    elif window_type == "tower":
        radius_var = DoubleVar()
        radius_scale = Scale(popup_window, variable = radius_var)
        radius_scale.pack(anchor="w")
        radius_label = Label(popup_window, anchor="w")
        radius_button = Button(popup_window, text="Get radius value", command= lambda: get_radius_value(radius_var, radius_label))
        radius_button.pack(anchor="w")
        radius_label.pack()
    # will also need to add buttons for the rest.
    
# Default skeleton for a pop-up window
def display_popup(title="", size="200x200", window_type=None):
    if title != "":
        popup_window = Tk()
        popup_window.title(title)
        popup_window.geometry(size)
        popup_label = Label(popup_window, text=get_display_text(window_type))
        add_buttons_if_needed(popup_window, window_type)
        popup_label.pack()
        popup_window.mainloop

def read_txt_file(): # (optional)
    # a function if it's decided later on to read data from .txt files.
    # once read, it will load settings to model.
    pass

# Reads data from a csv file
def read_csv_file(csv_file_to_open, data):
    with open(csv_file_to_open,'r') as csvfile: 
        lines = reader(csvfile, delimiter=',')
        count = 0
        for row in lines:
            if count: 
                data.sim.append(row[0]) 
                data.radiotype.append(row[1]) 
                data.radio.append(row[2]) 
                data.mcc.append(row[3]) 
                data.mnc.append(row[4]) 
                data.area.append(row[5]) 
                data.cellid.append(row[6]) 
                data.unit.append(row[7]) 
                data.lat.append(row[8]) 
                data.lon.append(row[9]) 
                data.signal.append(row[10]) 
                data.extra.append(row[11]) 
                data.acc.append(row[12]) 
                data.time.append(row[13]) 
                data.speed.append(row[14]) 
                data.bearing.append(row[15]) 
                data.alt.append(row[16]) 
                data.api.append(row[17]) 
                data.device.append(row[18]) 
            count = 1

# animates the path that was taken, from the data of the csv file
def animate_path(canvas, data): # plots the xy positions
    # starting position ("START")
    pos_A = [float(data.lat[0]), float(data.lon[0])]
    y_raw = HIGHEST_LATITUDE - pos_A[0]
    x_raw = HIGHEST_LONGITUDE - pos_A[1]    
    y_percent = ((y_raw*100)/(HIGHEST_LATITUDE-LOWEST_LATITUDE))/100
    x_percent = ((x_raw*100)/(HIGHEST_LONGITUDE-LOWEST_LONGITUDE))/100
    x = WINDOW_SIZE[0] - x_percent*WINDOW_SIZE[0]
    y = y_percent*WINDOW_SIZE[1]
    canvas.create_polygon(x+15, y+15, x-15, y+15, x-15, y-15, x+15, y-15, fill="green")
    canvas.create_text(x, y, text="START", font=("Arial", 7, "bold"), fill="black")

    global pause # (optional)
    cell_id = 0
    for i in range(len(data.cellid)):
        if cell_id != data.cellid[i]:
            # add handover positions ("5G->5G HO") (purple)
            cell_id = data.cellid[i]
            if (i != 0) and ("5G" in data.radiotype[i]) and ("5G" in data.radiotype[i-1]):
                pos_HO = [float(data.lat[i]), float(data.lon[i])]
                y_raw = HIGHEST_LATITUDE - pos_HO[0]
                x_raw = HIGHEST_LONGITUDE - pos_HO[1]    
                y_percent = ((y_raw*100)/(HIGHEST_LATITUDE-LOWEST_LATITUDE))/100
                x_percent = ((x_raw*100)/(HIGHEST_LONGITUDE-LOWEST_LONGITUDE))/100
                x = WINDOW_SIZE[0] - x_percent*WINDOW_SIZE[0]
                y = y_percent*WINDOW_SIZE[1]
                canvas.create_text(x+55, y, text="5G->5G HO", font=("Arial", 12, "bold"), fill="black")
                canvas.create_polygon(x+5, y+5, x-5, y+5, x-5, y-5, x+5, y-5, fill="purple")
        elif "5G" in data.radiotype[i]:   
            # add 5G radio connection positions on map (blue)
            pos_ANY = [float(data.lat[i]), float(data.lon[i])]
            y_raw = HIGHEST_LATITUDE - pos_ANY[0]
            x_raw = HIGHEST_LONGITUDE - pos_ANY[1]    
            y_percent = ((y_raw*100)/(HIGHEST_LATITUDE-LOWEST_LATITUDE))/100
            x_percent = ((x_raw*100)/(HIGHEST_LONGITUDE-LOWEST_LONGITUDE))/100
            x = WINDOW_SIZE[0] - x_percent*WINDOW_SIZE[0]
            y = y_percent*WINDOW_SIZE[1]
            canvas.create_text(x, y+25, text="", font=("Arial", 12, "bold"), fill="black")
            canvas.create_polygon(x+2, y+2, x-2, y+2, x-2, y-2, x+2, y-2, fill="blue")
        else:
            # add all other radio connection positions to map (orange)
            pos_ANY = [float(data.lat[i]), float(data.lon[i])]
            y_raw = HIGHEST_LATITUDE - pos_ANY[0]
            x_raw = HIGHEST_LONGITUDE - pos_ANY[1]    
            y_percent = ((y_raw*100)/(HIGHEST_LATITUDE-LOWEST_LATITUDE))/100
            x_percent = ((x_raw*100)/(HIGHEST_LONGITUDE-LOWEST_LONGITUDE))/100
            x = WINDOW_SIZE[0] - x_percent*WINDOW_SIZE[0]
            y = y_percent*WINDOW_SIZE[1]
            canvas.create_text(x, y+25, text="", font=("Arial", 12, "bold"), fill="black")
            canvas.create_polygon(x+2, y+2, x-2, y+2, x-2, y-2, x+2, y-2, fill="orange")
        canvas.update()
        time.sleep(.1)

    # ending position ("FINISH")
    pos_B = [float(data.lat[len(data.lat)-1]), float(data.lon[len(data.lon)-1])]
    y_raw = HIGHEST_LATITUDE - pos_B[0]
    x_raw = HIGHEST_LONGITUDE - pos_B[1]    
    y_percent = ((y_raw*100)/(HIGHEST_LATITUDE-LOWEST_LATITUDE))/100
    x_percent = ((x_raw*100)/(HIGHEST_LONGITUDE-LOWEST_LONGITUDE))/100
    x = WINDOW_SIZE[0] - x_percent*WINDOW_SIZE[0]
    y = y_percent*WINDOW_SIZE[1]
    canvas.create_polygon(x+15, y+15, x-15, y+15, x-15, y-15, x+15, y-15, fill="red")
    canvas.create_text(x, y, text="FINISH", font=("Arial", 6, "bold"), fill="black")

    canvas.update()
    time.sleep(.5)

# creates the menu bar at the top of the window
def createMenuBar(mainWindow):
    menubar = Menu(mainWindow)
    # file
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Save raw data as .pdf", command=lambda: display_popup("Save as PDF", "300x300", "pdf")) # save data as pdf
    filemenu.add_command(label="Save raw data as .txt", command=lambda: display_popup("Save as TEXT", "300x300", "txt")) # save data as .txt
    filemenu.add_separator()
    filemenu.add_command(label="Exit (does not save)", command=lambda: display_popup("Exit?", "300x200", "exit"))       # exit the program
    menubar.add_cascade(label="File", menu=filemenu)
    # add
    addmenu = Menu(menubar, tearoff=0)
    addmenu.add_command(label="Add tower", command=lambda: display_popup("Add a tower", "300x300", "tower")) # A window to pop up for user entry of tower
    addmenu.add_command(label="Add device", command=lambda: display_popup("Add a device", "300x300", "device")) # A window to pop up for user entry of device
    menubar.add_cascade(label="Add", menu=addmenu)
    # play
    playmenu = Menu(menubar, tearoff=0)
    playmenu.add_command(label="Play", command=lambda: play_animation()) # play the scene
    playmenu.add_command(label="Pause", command=lambda: pause_animation()) # pause the scene
    playmenu.add_command(label="Restart", command=lambda: donothing) # restart the scene
    playmenu.add_separator()
    playmenu.add_command(label="Set play speed", command=lambda: donothing) # sets speed of scene
    menubar.add_cascade(label="Play", menu=playmenu)
    # stats
    statsmenu = Menu(menubar, tearoff=0)
    statsmenu.add_command(label="Show stats window", command=lambda: display_popup("Stats", "300x300", "stats")) # this will display a window with a drop down menu.
    statsmenu.add_command(label="Display/hide quick stats", command=lambda: donothing)
    statsmenu.add_command(label="Display/hide legend", command=lambda: donothing)
    menubar.add_cascade(label="Stats", menu=statsmenu)
    # help
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=lambda: display_popup("Help", "300x300", "help"))
    helpmenu.add_command(label="More info", command=lambda: display_popup("More info", "300x300", "info"))
    helpmenu.add_separator()
    helpmenu.add_command(label="CS260 Team Credit", command=lambda: display_popup("Credit", "400x300", "credit")) # displays window with team members and roles.
    menubar.add_cascade(label="Help", menu=helpmenu)

    mainWindow.config(menu=menubar)

def pause_animation(): # (optional)
    global pause
    pause = True

def play_animation(): # (optional)
    global play
    play = False


# runs the program
def run(w = WINDOW_SIZE[0], h = WINDOW_SIZE[1]):

    preset_devices = presetDevices() # (optional)
    
    # creates the window
    mainWindow = Tk()
    mainWindow.title("5G Handover Model")
    canvas = Canvas(mainWindow, width = w, height = h)
    canvas.pack()
    createMenuBar(mainWindow)
    for i in range(len(csv_files_to_open)):
        data.append(Data())
    initialize(preset_devices, canvas, mainWindow, data, csv_files_to_open)

    # wrapper for redraw
    def redrawWrapper(preset_devices, canvas, data):
        canvas.delete(ALL)
        redraw(preset_devices, canvas, data)
        canvas.update()

    # wrapper for moused pressed
    def mousePressWrapper(preset_devices, event, canvas):
        mousePressed(preset_devices, event, canvas)
        redrawWrapper(preset_devices, canvas,  data)

    # binds the mouse pressed event to the mouse
    mainWindow.bind("<Button-1>", lambda event: mousePressWrapper(preset_devices, event, canvas))

    redrawWrapper(preset_devices, canvas,  data)

    mainWindow.mainloop()

run() # call to run()
