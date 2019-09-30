from shutil import copy
import os
#with 
#for /L %v in (1,1,100) do fsutil file createnew from%v.txt 10485760
def copyFiles():
    directory = os.path.dirname(os.path.realpath(__file__))
    src= os.path.join(directory, "src")
    dst= os.path.join(directory, "dst")

    files = os.listdir(src)
    print(dst)
    for file in files:
        file_path = os.path.join(src, file)
        if os.path.isfile(file_path):
            copy(file_path, dst)
            
copyFiles()