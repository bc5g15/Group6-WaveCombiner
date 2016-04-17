#splash.py - Splash Screen Placeholder.
from Tkinter import *

def start(stuff):
    window = Toplevel()
    a = Label(window, image=stuff)
    a.pack(side="top", fill="both", expand="yes")
    Button(window, text="Close", command=window.destroy).pack()
    window.lift()
