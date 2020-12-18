from tkinter import *
import random
import time
from insertion import insertion_sort
from selection import selection_sort
from bubble import bubble_sort
from shell import shell_sort
from quick import quick_sort
#from merge import merge_sort

data = []
colourArray = []

c_width = 600
c_height = 380
root = Tk()
root.maxsize(1200, 800)
root.config(bg = 'black')
root.title('Sorting Algorithm Visualizer')

top_frame = Frame(root, width = 800, height = 200, bg = 'azure3', highlightthickness=2, highlightbackground="#111")
top_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

c = Canvas(root, width = 800, height = 380, bg = 'white', highlightthickness=2, highlightbackground="#111")
c.grid(row = 1, column = 0, padx = 5, pady = 5)

def drawData(data, colourArray):

    y_stretch = 5 # highest y = max_value * y_stretch
    y_gap = 100 # gap between lower canvas and x-axis
    x_stretch = 15 # space between every bar item
    x_width = 800 / (len(data) + 1) # width of every item 
    x_gap = 30 #gap between left canvas and y-axis
    c.delete('all')
    normalizedData = [i / max(data) for i in data]
    for x, y in enumerate(normalizedData):
    # create rectangle coordinates for each bar
        x0 = x * x_width + x_gap + x_stretch
        y0 = c_height - y * 340
        x1 = (x + 1) * x_width + x_gap - y_stretch
        y1 = c_height
        c.create_rectangle(x0, y0, x1, y1, fill = colourArray[x])

        # place y-value above each bar
        c.create_text(x0 + 2, y0, anchor = SW, text = str(data[x]))
    root.update_idletasks()

def generate():

    global data
    data = []

    try:
        size = int(sizeNum.get())
    except:
        size = 10

    try:
        minValue = int(MIN.get())
    except:
        minValue = 1
    
    try: 
        maxValue = int(maxValue.get())
    except:
        maxValue = 50

    for i in range(size):
        data.append(random.randint(minValue, maxValue))

    drawData(data, ['red' for x in range(len(data))])

def start():

    global data
    selection = variable.get()

    if selection == "Insertion Sort":
        insertion_sort(data, drawData, speed.get())
    
    if selection == "Selection Sort":
        selection_sort(data, drawData, speed.get())

    if selection == "Bubble Sort":
        bubble_sort(data, drawData, speed.get())

    if selection == "Shell Sort":
        shell_sort(data, drawData, speed.get())
    
    if selection == "Quick Sort":
        quick_sort(data, 0, len(data) - 1, drawData, speed.get())
    
    # if selection == "Merge Sort":
    #     merge_sort(data, 0, len(data) - 1, drawData, speed.get())
    # drawData(data, ['green' for x in range(len(data))])

l = Label(top_frame, text = "Algorithm: ", bg = 'bisque3', padx = 10, pady = 5)
l.grid(row = 0, column = 0, padx = 2, sticky = W)

Options = ["Insertion Sort", "Selection Sort", "Bubble Sort", "Shell Sort", "Quick Sort"]
variable = StringVar()
variable.set(Options[0])

user = OptionMenu(top_frame, variable, *Options)
user.grid(row = 0, column = 1, padx = 2, pady = 5)
user.configure(background = 'bisque2', font = ('calibri', 12, 'bold'))
user["menu"].configure(bg = 'bisque2', font = ('calibri', 10, 'bold'))

generate = Button(top_frame, text = "Generate", command = generate, font = ('calibri', 12, 'bold'), background = 'bisque2', padx = 20)
generate.grid(row = 0, column = 4, padx = 2, pady = 10)

start = Button(top_frame, text = "Start", command = start, font = ('calibri', 12, 'bold'), background = 'bisque2', padx = 20)
start.grid(row = 0, column = 5, padx = 5, pady = 10)

length = Label(top_frame, text = "Number of Elements: ", bg = 'bisque3', padx = 10, pady = 5)
length.grid(row = 0, column = 2, padx = 2, pady = 5, sticky = W)

sizeNum = Entry(top_frame, bd = 5, justify = CENTER, font = ('calibri', 12))
sizeNum.grid(row = 0, column = 3, padx = 2, pady = 5)

MIN = Label(top_frame, text = "Minimum value: ", bg = 'bisque3', padx = 5, pady = 5)
MIN.grid(row = 1, column = 0, padx = 2, pady = 5, sticky = W)

minNum = Entry(top_frame, bd = 3, justify = CENTER, font = ('calibri', 12))
minNum.grid(row = 1, column = 1, padx = 2, pady = 5)

MAX = Label(top_frame, text = "Maximum value: ", bg = 'bisque3', padx = 5, pady = 5)
MAX.grid(row = 1, column = 2, padx = 2, pady = 5, sticky = W)

maxNum = Entry(top_frame, bd = 3, justify = CENTER, font = ('calibri', 12))
maxNum.grid(row = 1, column = 3, padx = 2, pady = 5)

speed = Scale(top_frame, label = "Speed [s]", font = ('calibri', 10, 'bold'), from_= 0.1, to= 2.0, resolution = 0.2, length = 200, digits = 2, orient = HORIZONTAL, background = 'bisque2')
speed.grid(row = 1, column = 4, padx = 2, pady = 5)

green = Label(top_frame, bg = 'green', padx = 10, pady = 5)
green.grid(row = 2, column = 0, padx = 2, pady = 5, sticky = W)

gs = Label(top_frame, text = 'Actively sorting', padx = 10, pady = 5)
gs.grid(row = 2, column = 1, padx = 2, pady = 5, sticky = W)

red = Label(top_frame, bg = 'red', padx = 10, pady = 5)
red.grid(row = 3, column = 0, padx = 2, pady = 5, sticky = W)

rs = Label(top_frame, text = 'Not sorted yet', padx = 10, pady = 5)
rs.grid(row = 3, column = 1, padx = 2, pady = 5, sticky = W)

root.mainloop()
