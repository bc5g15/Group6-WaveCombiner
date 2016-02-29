#wavebuilder.py - The component that allows the user to edit the sine wave
from Tkinter import *
from components import Wave, Graph
import math


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

         #Interesting thing. If you put variables into the scrollbars, then they
         #will follow the maniuplation of other scrollbars with the same variable
         #Even if they are on different windows!
         
         Label(f, text="Amplitude").pack()
         self.a_scale = Scale(f,orient=HORIZONTAL,\
                              command=self.set_amp, from_=0, to=1, resolution=0.1)
         self.a_scale.set(wave.amp)
         self.a_scale.pack()
         Label(f, text="Frequency(Hz)").pack()
         self.f_scale = Scale(f,orient=HORIZONTAL,\
                              command=self.set_freq, from_=0, to=5, resolution=0.1)
         self.f_scale.set(wave.freq)
         self.f_scale.pack()
         Label(f, text="Phase Angle(degrees)").pack()
         self.p_scale = Scale(f,orient=HORIZONTAL,\
                              command=self.set_phase, from_=0, to=360)
         self.p_scale.set(wave.freq)
         self.p_scale.pack()


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
        
##root = Tk()
##WaveBuilder(Wave(), None)
##root.mainloop()

