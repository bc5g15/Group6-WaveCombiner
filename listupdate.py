#listupdate.py - A massive cheat to access the update_list function

#This is an incredibly cheaty way to pass this function around, but really
#seems to be the best way.

myfunction = ""

def setme(function):
    global myfunction
    myfunction = function

def call():
    try:
        myfunction()
    except:
        print "Incorrect Function"
