#validate.py - All of the validation logic. Mainly for the settings window

def valid_float(value):
    try:
        float(value)
        return True
    except:
        return False

def valid_minmaxstep(amin, amax, step):
    #At this point, we assume the values are floats

    #A step of 0 is never valid
    if step == 0:
        return False

    #Min and max should never be equal
    if amin==amax:
        return False

    #If the step is greater than the difference between the min and max, that is bad
    if abs(amax - amin) <step:
        return False

    #if we made it this far, then the value is probably good.
    return True

def non_zero_float(value):
    try:
        k=float(value)
        if k==0:
            return False
        else:
            return True
    except:
        return False
