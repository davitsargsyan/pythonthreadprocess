from concurrent.futures import ThreadPoolExecutor
import timeit
from shutil import copy
import os
from app import copyFiles


directory = os.path.dirname(os.path.realpath(__file__))
src= os.path.join(directory, "src")
dst= os.path.join(directory, "dst")
files = os.listdir(src)

start=timeit.default_timer()
executor = ThreadPoolExecutor(3)

future = executor.submit(copyFiles(files[0:32],src,dst))
future2 = executor.submit(copyFiles(files[33:65],src,dst))
future3 = executor.submit(copyFiles(files[66:99],src,dst))

duration = timeit.default_timer()-start
print(duration)