#settings.py - The global settings window
#import windowlist
#import test

freqmin = 0.0
freqmax = 5.0
freqstep = 0.1

ampmin = 0.0
ampmax = 1.0
ampstep = 0.1

xscale = 2
yscale = 4


def defaults_flat():
    global freqmin
    global freqmax
    global freqstep
    global ampmin
    global ampmax
    global ampstep
    global xscale
    global yscale
    
    freqmin = 0.0
    freqmax = 5.0
    freqstep = 0.1

    ampmin = 0.0
    ampmax = 1.0
    ampstep = 0.1

    xscale = 2
    yscale = 4

def edit(newfreqmin, newfreqmax, newfreqstep, newampmin, newampmax, newampstep,\
         newxscale, newyscale):
    global freqmin
    global freqmax
    global freqstep
    global ampmin
    global ampmax
    global ampstep
    global xscale
    global yscale

    freqmin = newfreqmin
    freqmax = newfreqmax
    freqstep = newfreqstep
    ampmin = newampmin
    ampmax = newampmax
    ampstep = newampstep
    xscale = newxscale
    yscale = newyscale

    #Save these settings to an external file

    #Update the components from here?
    #No, settings are updated from the settings window

def getfreqmin():
    return freqmin
def getfreqmax():
    return freqmax
def getfreqstep():
    return freqstep

def getampmin():
    return ampmin
def getampmax():
    return ampmax
def getampstep():
    return ampstep

def getxscale():
    return xscale
def getyscale():
    return yscale
