#saveload.py - Saving and loading object data
import pickle
import hashlib
import tkMessageBox

def save(data, filename):
    f = open(filename, "w")
    #Stringify data
    s = pickle.dumps(data)
    
    #create hash code
    hsh = hashlib.md5()
    hsh.update(s)
    code = hsh.digest()

    #write file, with hash header
    f.write(code+"\n")
    f.write(s)
    f.close()

def load(filename):
    f = open(filename, "r")

    #get the hash code
    code = f.readline()

    #get the rest of the data
    data = f.read()

    #try to recreate the hash
    hsh = hashlib.md5()
    hsh.update(data)
    check = hsh.digest() + "\n"

    if check==code:
        #hashes match, we're good.
        output = pickle.loads(data)
        return output
    else:
        #hashes don't match, file is corrupt
        print check
        print code
        tkMessageBox.showinfo(title="Error Loading", message="File invalid or corrupt! \n Cannot load file!")
        return False
    
