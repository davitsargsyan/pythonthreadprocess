from concurrent.futures import ProcessPoolExecutor
import time
from shutil import copy
import os
from app import copyFiles

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    src= os.path.join(directory, "src")
    dst= os.path.join(directory, "dst")
    files = os.listdir(src)
    
    start=timeit.default_timer()
    executor = ProcessPoolExecutor(3)
    future = executor.submit(copyFiles,(files[0:32],src,dst))
    future2 = executor.submit(copyFiles,(files[0:32],src,dst))
    future3 = executor.submit(copyFiles,(files[0:32],src,dst))

    duration = timeit.default_timer()-start
    print(duration)

if __name__ == '__main__':
    main()