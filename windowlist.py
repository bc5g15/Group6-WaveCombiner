#windowlist.py - Manages the list of open waveforms

wavwindows = {}

def add(wav, window):
    wavwindows[wav] = window

def delete(wav):
    wavwindows[wav].close()
    del wavwindows[wav]

def exists(wav):
    if wav in wavwindows:
        return True
    else:
        return False

def get(wav):
    #Don't use this without validation!
    return wavwindows[wav]

def update_windows():
    for item in wavwindows:
        wavwindows[item].reset()
        
