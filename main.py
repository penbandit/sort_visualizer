from random import random
from tkinter import *
from tkinter import ttk
import random

#Importing colors from colors.py
from colors import *

# Creating a basic window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)

# Sort algorithm selector
algorithm_Name = StringVar()
algo_List = ['Bubble Sort', 'Merge Sort']

# Sort speed selector
speed_Name = StringVar()
speed_List = ['Fast', 'Medium', 'Slow']

# Empty data set to generate numebrs to sort
data = []

# Function to draw data on the canvas
def drawData(data, colorarray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 300
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarray[i])

    window.update_idletasks()

# Function to generate array with random data
def generate():
    global data

    data = []
    for i in range(0, 1000):
        random_value = random.randint(1, 1500)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])

# Function to set sorting speed
def set_Speed():
    if speed_Menu.get() == 'Slow':
        return 0.3
    elif speed_Menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

# Function to select algorithm and start sorting
def sort():
    pass

# UI
UI_frame = Frame(window, width = 900, height = 300, bg = WHITE)
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

# Menu to select sorting algorithm
l1 = Label(UI_frame, text = "Algorithm:  ", bg = WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_Menu = ttk.Combobox(UI_frame, textvariable=algorithm_Name, values=algo_List)
algo_Menu.grid(row=0, column=1, padx=5, pady=5)
algo_Menu.current(0)

# Menu to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed:  ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_Menu = ttk.Combobox(UI_frame, textvariable=speed_Name, values=speed_List)
speed_Menu.grid(row=1, column=1, padx=5, pady=5)
speed_Menu.current(0)

# Sort Button
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

# Button to generate the array
b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

# Canvas
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()