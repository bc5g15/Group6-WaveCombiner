#help.py - The programs inbuilt help

from Tkinter import *

def change():
    f1 = f2

root = Tk()

Button(root, text="cycle", command=change).pack()

f1=Frame(root)

f1.pack()

f2=Frame(root)

Label(f2, text="???").pack()



root.mainloop()
