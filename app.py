from shutil import copy
import os
#with 
#for /L %v in (1,1,100) do fsutil file createnew from%v.txt 10485760
def copyFiles(files,src,dst):
    #copy files
    for file in files:
        file_path = os.path.join(src, file)
        if os.path.isfile(file_path):
            copy(file_path, dst)


    
