#wavebuilder.py - The component that allows the user to edit the sine wave
from Tkinter import *
from components import Wave, Graph
import math
import settings
import windowlist
import listupdate

#I wouldn't really run this class as its own thing
#It is a component of a larger project.
class WaveBuilder:
    wav = None
    comp = None

    #window
    t = None
    #graph
    g = None

    f_scale = None
    fvar = 0.3
    a_scale = None
    avar = 0.2
    p_scale = None
    pvar = 0.1

    n_entry = None
    
    def __init__(self, wave, composite_graph):
         #populate variables, then initialize graphics.
         self.wav = wave
         self.comp = composite_graph

         #graphics building
         self.t = Toplevel()
         self.t.title(wave.name)
         self.g = Graph(self.t, width=200,height=200, bg="white")
         self.g.set_wave(wave)
         self.g.pack(side=LEFT)
         self.g.draw()

         f = Frame(self.t)
         f.pack(side=RIGHT)

         f1 = Frame(f)
         f1.pack(side=TOP)
         self.n_entry = Entry(f1, text=str(self.wav.name))
         self.n_entry.insert(0,self.wav.name)
         self.n_entry.pack(side=RIGHT)
         Button(f1, text="Set Name", command=self.update_name).pack(side=LEFT)
         

         #Interesting thing. If you put variables into the scrollbars, then they
         #will follow the maniuplation of other scrollbars with the same variable
         #Even if they are on different windows!
         
         Label(f, text="Amplitude").pack()
         self.a_scale = Scale(f,orient=HORIZONTAL,\
                              command=self.set_amp, from_=settings.getampmin(),\
                              to=settings.getampmax(), resolution=settings.getampstep())
         self.a_scale.set(wave.amp)
         self.a_scale.pack()
         Label(f, text="Frequency(Hz)").pack()
         self.f_scale = Scale(f,orient=HORIZONTAL,\
                              command=self.set_freq, from_=settings.getfreqmin(),\
                              to=settings.getfreqmax(), resolution=settings.getfreqstep())
         self.f_scale.set(wave.freq)
         self.f_scale.pack()
         Label(f, text="Phase Angle(degrees)").pack()
         self.p_scale = Scale(f,orient=HORIZONTAL,\
                              command=self.set_phase, from_=0, to=360)
         self.p_scale.set(wave.freq)
         self.p_scale.pack()

         #I need to add a specific protocol for when the user quits the window
         self.t.protocol("WM_DELETE_WINDOW", self.on_closing)


    def set_amp(self, value):
        self.wav.set_amp(float(value))
        self.update()

    def set_freq(self, value):
        self.wav.set_freq(float(value))
        self.update()

    def set_phase(self,value):
        deg = float(value)
        rads = (deg *2 * math.pi)/360.0
        self.wav.set_phase(rads)
        self.update()
        
    def update(self):
        self.g.draw()
        if(self.comp):
            self.comp.draw()

    def reset(self):
        self.a_scale["from_"] = settings.getampmin()
        self.a_scale["to"] = settings.getampmax()
        self.a_scale["resolution"] = settings.getampstep()

        self.f_scale["from_"] = settings.getfreqmin()
        self.f_scale["to"]=settings.getfreqmax()
        self.f_scale["resolution"]=settings.getfreqstep()

        self.g.setvertical()

        self.update()

    def close(self):
        self.t.destroy()

    def on_closing(self):
        windowlist.delete(self.wav)

    def update_name(self):
        self.wav.set_name(self.n_entry.get())
        
##root = Tk()
##WaveBuilder(Wave(), None)
##root.mainloop()


