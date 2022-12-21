# The purpose of this program is to access a pre-specified directory and list it's contents in alphabetical order (unless this is already the case).

import os, pathlib, numpy, shutil # Adjacent to this comment, the os, pathlib and shutil module is imported in order to allow for access to and manipulation of said directory.
# The Numpy module has been used as a replacement/workaround for the removal of the random.shuffle() function in the random module.

CurrDir = os.getcwd() 
print(CurrDir)

NewDir = pathlib.PureWindowsPath(r"C:\Users\PC\Desktop\Text Files") 
ChangeDir = os.chdir(NewDir)

CheckCurrDir = os.getcwd()
print(CheckCurrDir)

ExtContent = os.listdir(NewDir) 
ShuffContent = os.listdir() 

for x in range(len(ExtContent)):
     ShuffObj = numpy.random.randint(0,len(ExtContent)) 
     ShuffContent.append(ExtContent[ShuffObj])

NwPlace = r"C:\Users\PC\Desktop\NewTxtFiles"    
for x in ShuffContent:
    shutil.copy(x,NwPlace)

print(len(ShuffContent))