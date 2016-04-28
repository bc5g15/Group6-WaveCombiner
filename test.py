#test.py - Entry point for the application
from Tkinter import *
from components import Wave, Graph
from wavebuilder import WaveBuilder
import settings
import windowlist
import settingsview
import mathematics
import splash

import tkFileDialog
import saveload

import listupdate
waveno = 1

filename = ""

fextension=".wavcom"

#wavwindows = {}



#function - Update the wavelistbox
def update_list():
    #Clear and repopulate the list
    wavlistbox.delete(0, END)
    for item in wavlst:
        wavlistbox.insert(END, item.name)

listupdate.setme(update_list)

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
        index = int(wavlistbox.curselection()[0])
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

#Will call saveas if a filename is not declared.
#Otherwise just do it automatically.
def save():
    if filename=="":
        saveas()
    else:
        saveload.save(wavlst, filename)

def saveas():
    global filename

    #Need to determine what our file extension is.
    filename = tkFileDialog.asksaveasfilename(defaultextension=fextension,\
                                              filetypes=(("Wave Combiner files",fextension),\
                                                         ("All Files", "*")))

    if filename == "":
        return
    
    saveload.save(wavlst, filename)
    root.title("Wave Combiner - " + filename)

def saveimageas():
    filename = tkFileDialog.asksaveasfilename(defaultextension=fextension,\
                                              filetypes=(("Bitmap",".bmp"),\
                                                         ("Jpeg",".jpg"),\
                                                         ("Png",".png"),\
                                                         ("All Files", "*")))
    
    if filename=="":
        return
    else:
        comp.draw_image(filename)

#Here is where things get crazy
def load():
    global filename
    global wavlst
    #Still need to decide on an extension!
    filename = tkFileDialog.askopenfilename(defaultextension=fextension,\
                                            filetypes=(("Wave Combiner files",fextension),\
                                                       ("All Files", "*")))

    if filename=="":
        return
    
    data = saveload.load(filename)
    if data:
        
        root.title("Wave Combiner - " + filename)
        wavlst = data
        comp.set_wave_list(wavlst)
        windowlist.clear()
        update_list()
        comp.draw()
    else:
        print "Invalid Data!"
        
def new_file():
    #nothing too hard, just reset the program to a default state
    global wavlst
    global filename
    global waveno
    waveno = 1
    wavlst = [Wave(name="Default1"), Wave(freq=2, name="Default2")]
    comp.set_wave_list(wavlst)
    windowlist.clear()
    root.title("Wave Combiner")
    update_list()
    comp.draw()
    filename = ""

def load_splash():
    splash.start(img)

#Graph, populate the wave form properly

#This list has some debug values, should we leave these in?
wavlst = [Wave(name="Default1"), Wave(freq=2, name="Default2", draw=True)]

#The root window holds the composite graph and the list of waves
root = Tk()

img = PhotoImage(file="fin.gif")
#Add the menubar and cascade menus
menubar = Menu(root)
root.title("Wave Combiner")

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open...", command=load)
filemenu.add_command(label="Save...", command=save)
filemenu.add_command(label="Save As...", command=saveas)
filemenu.add_command(label="Save Image As...", command=saveimageas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Settings...", command=opensettings)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
#helpmenu.add_command(label="Documentation...", command=TODO)
helpmenu.add_command(label="About...", command=load_splash)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#left bit maintains the composite graph
left1 = Frame(root)
left1.pack(side=LEFT)

fgraph = Frame(left1, relief=SUNKEN, bd=1)
fgraph.pack(side=TOP)

#composite graph goes in the left side
#Might want to shuffle this around later to fit more widgets in.
comp = Graph(fgraph, width = 500, height=500, bg="white")
comp.set_wave_list(wavlst)

comp.grid(column=1, row=0)
comp.recenter()
comp.getscale()
comp.draw()



#Scale widget designed to manipulate the graph
#Container
left2 = Frame(left1)
left2.pack(side=BOTTOM)

#Recenter button, no real reason, just thought it might be a nice feature
Button(left2, text="Recenter", command=recenter).pack(side=LEFT)

#Maths window button should go somewhere here. Possibly needs to be better organised.
#Button(left2, text="Mathematics", command=mathematics.start).pack(side=RIGHT)

#This sort of thing should go in the settings window
##Scale(left2, label="X Scale", from_=1, to=50, \
##      command=comp.scalex).pack(side=LEFT)
##Scale(left2,  label="Y Scale", from_=1, to=50, \
##      command=comp.scaley).pack(side=LEFT)


xnav=Scale(fgraph,  label="Navigate X", from_=-500, to=500,\
      command=comp.scrollx, orient=HORIZONTAL, length=500)
xnav.grid(column=1, row=1)
ynav=Scale(fgraph, label="Navigate Y", from_=500, to=-500,\
      command=comp.scrolly, resolution=1, length=500)
ynav.grid(column=0, row=0)

#The Wave List structure goes on the right.
right1 = Frame(root)
right1.pack(side=RIGHT)

Label(right1, text="Wave List").pack()

scroll = Scrollbar(right1)
scroll.pack(side=RIGHT, fill=Y)

wavlistbox = Listbox(right1, height=10)
wavlistbox.pack(side=TOP)

scroll.config(command=wavlistbox.yview)

#3 Buttons - New, Edit, Delete
#Might need to refer them in different variables, however it might be enough to just pack them
Button(right1, text="New", command=new).pack()
Button(right1, text="Edit", command=edit).pack()
Button(right1, text="Remove", command=remove).pack()

update_list()

#Load up that splashscreen
root.after(100, load_splash)

root.mainloop()



