#splash.py - Splash Screen Placeholder.
from Tkinter import *

def start():
    window = Toplevel()
    Label(window, text="Splash Screen Goes Here!").pack()
    window.lift()
