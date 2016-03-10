#settingsview.py

from Tkinter import *
import settings
import validate
import tkMessageBox
#For some reason you can't set StringVars here. So I'm just defining the space
import windowlist

window = None
isOpen = False

comp = None
wavs = None

freqmin=None
freqmax=None
freqstep=None

ampmin=None
ampmax=None
ampstep=None

xscale=None
yscale=None

def on_closing():
    global isOpen
    isOpen = False
    window.destroy()

def btnapply():
    #1st check: All values are numerical
    k = validate.valid_float
    errors = []
    failed = False

    fn = freqmin.get()
    fx = freqmax.get()
    fz = freqstep.get()

    an = ampmin.get()
    ax = ampmax.get()
    az = ampstep.get()

    xs = xscale.get()
    ys = yscale.get()
    
    if k(fn):
        fn = float(fn)
    else:
        failed = True
        errors.append("Frequency Minimum is not a valid float!")

    if k(fx):
        fx = float(fx)
    else:
        failed = True
        errors.append("Frequency Maximum is not a valid float!")

    if k(fz):
        fz=float(fz)
    else:
        failed=True
        errors.append("Frequency Step is not a valid float!")

    if k(an):
        an=float(an)
    else:
        failed=True
        errors.append("Amplitude Minimum is not a valid float!")

    if k(ax):
        ax = float(ax)
    else:
        failed = True
        errors.append("Amplitude Maximum is not a valid float!")

    if k(az):
        az=float(az)
    else:
        failed = True
        errors.append("Amplitude Step is not a valid float!")

    if validate.non_zero_float(xs):
        xs=float(xs)
    else:
        failed=True
        errors.append("X Scale is not a valid float!")

    if validate.non_zero_float(ys):
        ys=float(ys)
    else:
        failed=True
        errors.append("Y Scale is not a valid float!")

    if failed:
        output = ""
        for item in errors:
            output += item + "\n"
        tkMessageBox.showinfo(title="Error",\
                              message="Apply failed for the following reasons:\n" + output)
    else:
        #Check2 - Some specific checks for min,max,step
        j = validate.valid_minmaxstep
        error2 = False
        if not j(fn, fx, fz):
            #Error
            error2 = True
            print "e1"
        if not j(an, ax, az):
            #Error
            error2=True
            print "e2"

        #At this point, all is good!
        if not error2:
            settings.edit(fn, fx, fz, an, ax, az, xs, ys)
            windowlist.update_windows()
            comp.getscale()
            comp.draw()
            
        

def update():
    freqmin.set(str(settings.getfreqmin()))
    freqmax.set(str(settings.getfreqmax()))
    freqstep.set(str(settings.getfreqstep()))

    ampmin.set(str(settings.getampmin()))
    ampmax.set(str(settings.getampmax()))
    ampstep.set(str(settings.getampstep()))

    xscale.set(str(settings.getxscale()))
    yscale.set(str(settings.getyscale()))
    
def start(composite):
    global isOpen
    global comp
    global wavs
    global window
    
    global freqmin
    global freqmax
    global freqstep

    global ampmin
    global ampmax
    global ampstep

    global xscale
    global yscale

    comp = composite
    
    if isOpen:
        pass
    else:
        #Width of 10 for entry boxes
        width=10
        
        isOpen=True
        window = Toplevel()
        window.title("Settings")

        Label(window, text="Frequency(Hz)").pack()
        freqf=Frame(window)
        freqf.pack()

        freqmin=StringVar()
        freqmax=StringVar()
        freqstep=StringVar()

        ampmin=StringVar()
        ampmax=StringVar()
        ampstep=StringVar()

        xscale=StringVar()
        yscale=StringVar()

        Label(freqf, text="Mininmum").grid(row=0, column=0)
        Entry(freqf, textvar=freqmin, width=width).grid(row=1, column=0)
        Label(freqf, text="Maximum").grid(row=0,column=1)
        Entry(freqf, textvar=freqmax,width=width).grid(row=1, column=1)
        Label(freqf, text="Step").grid(row=0, column=2)
        Entry(freqf, textvar=freqstep,width=width).grid(row=1, column=2)

        Label(window, text="Amplitude").pack()
        ampf=Frame(window)
        ampf.pack()

        Label(ampf, text="Minimum").grid(row=0,column=0)
        Entry(ampf, textvar=ampmin, width=width).grid(row=1, column=0)
        Label(ampf, text="Maximum").grid(row=0,column=1)
        Entry(ampf, textvar=ampmax, width=width).grid(row=1,column=1)
        Label(ampf, text="Step").grid(row=0, column=2)
        Entry(ampf, textvar=ampstep, width=width).grid(row=1, column=2)


        scalef = Frame(window)
        scalef.pack()

        Label(scalef, text= "X Scale").grid(row=0, column=0)
        Entry(scalef, textvar=xscale, width=width).grid(row=0, column=1)
        Label(scalef,text="Y Scale").grid(row=1, column=0)
        Entry(scalef, textvar=yscale, width=width).grid(row=1, column=1)

        Button(window, text="Apply", command=btnapply).pack()

        window.protocol("WM_DELETE_WINDOW", on_closing)

        #Update values right at the end.
        update()
        
        
