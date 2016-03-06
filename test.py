#combiner.py - Test bed for building the application
from Tkinter import *
from components import Wave, Graph
from wavebuilder import WaveBuilder
import settings
import windowlist
import settingsview

waveno = 1

#wavwindows = {}



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
    a=WaveBuilder(newwave, comp)
    windowlist.add(newwave, a)
    

def edit():
    #opens the waveform for editing in the external window.
    #returns a tuple for some reason, we only want the first bit
    if not wavlistbox.curselection() == ():
        index = int(wavlistbox.curselection()[0])
        #print index
        wav = wavlst[index]
        
        #check if the window is already open
        if windowlist.exists(wav):
            #Will it be enough to just focus on the window?
            windowlist.get(wav).t.lift()
        else:
            a=WaveBuilder(wavlst[index], comp)
            windowlist.add(wav, a)

def remove():
    #Make sure something is highlighted!
    if not wavlistbox.curselection() ==():
        index = wavlistbox.curselection()[0]
        wav=wavlst.pop(index)
        #If the window is open, close it
        if windowlist.exists(wav):
            windowlist.delete(wav)
        update_list()
        comp.draw()

#There are a lot of functions in this list, this feels like very bad
#programming practice

#Recenters the graph, just by setting the X/Y Nav scales
def recenter():
    xnav.set(0)
    ynav.set(0)

def update_graph():
    comp.getscale()
    comp.draw()

#All incomplete menu items link here
def TODO():
    print "NOT IMPLEMENTED"

def opensettings():
    settingsview.start(comp)

#So many menuitem functions!
#It may be a good idea to implement them in a seperate file

#Graph, populate the wave form properly

#This list has some debug values, delete these later
wavlst = [Wave(name="Default1"), Wave(freq=2, name="Default2")]

#The root window holds the composite graph and the list of waves
root = Tk()

#Add the menubar and cascade menus
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=TODO)
filemenu.add_command(label="Save...", command=TODO)
filemenu.add_command(label="Load...", command=TODO)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=TODO)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Settings...", command=opensettings)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Documentation...", command=TODO)
helpmenu.add_command(label="About...", command=TODO)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#left bit maintains the composite graph
left1 = Frame(root)
left1.pack(side=LEFT)

#composite graph goes in the left side
#Might want to shuffle this around later to fit more widgets in.
comp = Graph(left1, width = 500, height=500, bg="white")
comp.set_wave_list(wavlst)

comp.pack()
comp.recenter()
comp.getscale()
comp.draw()



#Scale widget designed to manipulate the graph
#Container
left2 = Frame(left1)
left2.pack()

#Recenter button, no real reason, just thought it might be a nice feature
Button(left2, text="Recenter", command=recenter).pack(side=RIGHT)

#This sort of thing should go in the settings window
##Scale(left2, label="X Scale", from_=1, to=50, \
##      command=comp.scalex).pack(side=LEFT)
##Scale(left2,  label="Y Scale", from_=1, to=50, \
##      command=comp.scaley).pack(side=LEFT)


xnav=Scale(left2,  label="Navigate X", from_=-500, to=500,\
      command=comp.scrollx)
xnav.pack(side=LEFT)
ynav=Scale(left2, label="Navigate Y", from_=-500, to=500,\
      command=comp.scrolly)
ynav.pack(side=LEFT)

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
