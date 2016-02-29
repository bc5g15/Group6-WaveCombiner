#components.py - The Wave and Graph classes. Designed to be imported.
from Tkinter import *
import math

class Wave:
    amp = 0
    freq = 0
    phase = 0
    name = ""

    def __init__(self,name="default", amp=1, freq=1, phase=0):
        self.amp = amp
        self.freq = freq
        self.phase = phase
        self.name= name

    def y(self, x):
        y = self.amp * math.sin((x * 2 *math.pi * self.freq) + self.phase)
        return y

    def set_amp(self, value):
        self.amp = value
    def set_freq(self, value):
        self.freq=value
    def set_phase(self, value):
        self.phase = value


class Graph(Canvas):
    wave = None
    scaleX = 2
    scaleY =4
    viewX = 0
    viewY = 0

    wavlst= []

    def set_wave(self, wav):
        self.wavlst = [wav]
        self.recenter()

    def set_wave_list(self, wavelist):
        self.wavlst = wavelist

    def recenter(self):
        self.viewX = float(self["width"]) / 2
        self.viewY = float(self["height"])/2

    def scrollx(self, value):
        k = float(value)
        self.viewX = k + float(self["width"])/2
        self.draw()

    def scrolly(self, value):
        self.viewY = float(self["height"])/2 + float(value)
        self.draw()

    def scalex(self, value):
        self.scaleX=float(value)
        self.draw()

    def scaley(self, value):
        self.scaleY=float(value)
        self.draw()

    
    def draw(self):
        buf = 10
        #clean the slate, and do some basic housekeeping
        self.delete(ALL)
        height = float(self["height"])
        width = float(self["width"])
        vx = self.viewX
        vy = self.viewY
        
        xratio = width/(self.scaleX)
        yratio = height/(self.scaleY)

        #Axis lines, if they can be seen
        self.create_line(0, height-vy, width, height-vy, fill="blue")
        self.create_line(vx, 0, vx, height, fill="red")

        oldx = 0
        oldy = vy
        for x in range(int(width)):
            #k = k/xratio
            #k = x-vx
            k = (x-vx)/xratio

            #Creating gridlines. This is still in the works
            if (k%1==0) and (x!=vx):
                self.create_line(x, 0, x, height, fill="grey")
            
            y = 0
            for item in self.wavlst:
                y += item.y(k)
                
            #y = self.wave.y(k)
            y *= yratio
            #clean up that damn y signal
            y += vy
            y = height - y
            
            self.create_line(oldx, oldy, x, y, fill="black")
            oldx = x
            oldy = y
