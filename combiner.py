#combiner.py - Test bed for building the application
from Tkinter import *
from components import Wave, Graph
from wavebuilder import WaveBuilder

waveno = 1

#function - Update the wavelistbox
def update_list():
    #Clear and repopulate the list
    wavlistbox.delete(0, END)
    for item in wavlst:
        wavlistbox.insert(END, item.name)

#Build a new wave and add it to the list
def new():
    global waveno
    newwave = Wave(name="wave"+str(waveno))
    waveno += 1
    wavlst.append(newwave)
    update_list()
    WaveBuilder(newwave, comp)

def edit():
    #opens the waveform for editing in the external window.
    #returns a tuple for some reason, we only want the first bit
    index = int(wavlistbox.curselection()[0])
    print index
    #If not null
    WaveBuilder(wavlst[index], comp)

def remove():
    index = wavlistbox.curselection()[0]
    wavlst.pop(index)
    update_list()
    comp.draw()

#Graph, populate the wave form properly

#This list has some debug values, delete these later
wavlst = [Wave(name="Default1"), Wave(freq=2, name="Default2")]

#The root window holds the composite graph and the 
root = Tk()

#left bit maintains the composite graph
left1 = Frame(root)
left1.pack(side=LEFT)

#composite graph goes in the left side
#Might want to shuffle this around later to fit more widgets in.
comp = Graph(left1, width = 500, height=500, bg="white")
comp.set_wave_list(wavlst)
comp.recenter()
comp.pack()
comp.draw()

#Scale widget designed to manipulate the graph
#Container
left2 = Frame(left1)
left2.pack()

Scale(left2, label="X Scale", from_=1, to=50, \
      command=comp.scalex).pack(side=LEFT)
Scale(left2,  label="Y Scale", from_=1, to=50, \
      command=comp.scaley).pack(side=LEFT)
Scale(left2,  label="Navigate X", from_=-500, to=500,\
      command=comp.scrollx).pack(side=LEFT)
Scale(left2, label="Navigate Y", from_=-500, to=500,\
      command=comp.scrolly).pack(side=LEFT)

#The Wave List structure goes on the right.
right1 = Frame(root)
right1.pack(side=RIGHT)

wavlistbox = Listbox(right1, height=10)
wavlistbox.pack(side=TOP)

#3 Buttons - New, Edit, Delete
#Might need to refer them in different variables, however it might be enough to just pack them
Button(right1, text="New", command=new).pack()
Button(right1, text="Edit", command=edit).pack()
Button(right1, text="Remove", command=remove).pack()

update_list()

root.mainloop()

