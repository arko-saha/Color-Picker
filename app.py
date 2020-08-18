

# Import modules

from tkinter import *
from tkinter import colorchooser
import clipboard

# Define Function

def color():
    clr = colorchooser.askcolor(title="Select Color")
    label = Label(text=clr[1], width = 30)
    label.pack()
    root.configure(background=clr[1])
    clipboard.copy(clr[1])
    text = clipboard.paste()
    
# Window

root = Tk()

button1 = Button(root, text="Choose Color", command = color)
button1.pack()

root.geometry("300x300")
root.mainloop()
