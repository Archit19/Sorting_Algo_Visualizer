import random
import tkinter as tk
from tkinter import ttk
from bubbleSort import bubble_sort
from quicksort import quick_sort

root = tk.Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg = 'black')

# Variables
selected_algo = tk.StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10

    # Normalizing data
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        # Top Left
        x0 = i * x_width + offset + spacing
        y0 = c_height -height * 340

        # Bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor = 'sw', text = str(data[i]), fill = 'black')
    
    root.update_idletasks()


def Generate():
    global data
    minVal = int(minEntry.get())
    
    maxVal = int(maxEntry.get())

    size = int(sizeEntry.get())


    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    #data = [3, 9, 13, 2, 5]
    drawData(data, ['RoyalBlue1' for x in range(len(data))])

def StartAlgorithm():
    #print("Starting Algorithm .....")
    global data 
    if not data:
        return

    if (algoMenu.get() == "Quick Sort"):
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])
    elif (algoMenu.get() == 'Bubble Sort'):
        bubble_sort(data, drawData, speedScale.get())

# UI frame
UI_frame = tk.Frame(root, width = 600, height = 200, bg = 'grey')
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

canvas = tk.Canvas(root, width = 610, height = 380, bg = 'white')
canvas.grid(row = 1, column = 0, padx = 10, pady  =5)


# UI area
# Row [0]
tk.Label(UI_frame, text='Algorithm', bg='grey').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
algoMenu = ttk.Combobox(UI_frame, textvariable = selected_algo, values = ['Bubble Sort', 'Quick Sort'])
algoMenu.grid(row = 0, column = 1, padx = 5, pady = 0)
algoMenu.current(0)

speedScale = tk.Scale(UI_frame, from_ = 0.1, to = 2.0, length = 200, digits = 2, resolution = 0.2, orient = 'horizontal', label = "Select Speed [s]")
speedScale.grid(row = 0, column = 2, padx = 5, pady = 5)

tk.Button(UI_frame, text = "Start", command = StartAlgorithm, bg = 'red').grid(row = 0, column = 3, padx = 5, pady = 5)


# Row [1]
# tk.Label(UI_frame, text='Size', bg='grey').grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
sizeEntry = tk.Scale(UI_frame, from_ = 3, to = 25, resolution = 1, orient = 'horizontal', label = "Data Size")
sizeEntry.grid(row = 1, column = 0, padx =5, pady = 5)

# tk.Label(UI_frame, text='Min Value', bg='grey').grid(row = 1, column = 2, padx = 5, pady = 5, sticky = 'w')
minEntry = tk.Scale(UI_frame, from_ = 0, to = 10, resolution = 1, orient = 'horizontal', label = "Min Value")
minEntry.grid(row = 1, column = 1, padx =5, pady = 5)

# tk.Label(UI_frame, text='Max value', bg='grey').grid(row = 1, column = 4, padx = 5, pady = 5, sticky = 'w')
maxEntry = tk.Scale(UI_frame, from_ = 10, to = 100, resolution = 1, orient = 'horizontal', label = "Max Value")
maxEntry.grid(row = 1, column = 2, padx =5, pady = 5)

tk.Button(UI_frame, text = "Generate", command = Generate, bg = 'white').grid(row = 1, column = 3, padx = 5, pady = 5)

root.mainloop()