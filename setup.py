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
    pass

# Function to generate array with random data
def generate():
    pass

# Function to set sorting speed
def set_Speed():
    pass

# Function to select algorithm and start sorting
def sort():
    pass

### User Interface Here ###