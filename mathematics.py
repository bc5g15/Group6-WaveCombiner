#Mathematics.py - Mathematics window. Currently Blank
from Tkinter import *

isOpen = False
window = None

fcomp = None
fsing = None
fcomb = None

def compositeWaveData():
    #All data regarding composite wave is presented here
    Label(fcomp, text="Composite Wave Data Goes Here!").pack()

def singleWaveData():
    #Data regarding individual waves is presented here
    Label(fsing, text="Single wave data goes here!").pack()

def combinedWaveData():
    #Data regarding two compared waves is presented here
    Label(fcomb, text="Compared wave data goes here!").pack()

def start():
    global isOpen
    global window

    global fcomp
    global fsing
    global fcomb
    
    if isOpen:
        pass
    else:
        isOpen=True
        window = Toplevel()
        window.title("Mathematical Data")

        fcomp = Frame(window, bd=1, relief = RAISED)
        fcomp.pack(side=LEFT)

        fsing = Frame(window, bd=1, relief = RAISED)
        fsing.pack(side=LEFT)

        fcomb = Frame(window, bd=1, relief = RAISED)
        fcomb.pack(side=LEFT)

        compositeWaveData()
        singleWaveData()
        combinedWaveData()
