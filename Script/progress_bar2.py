import time
from progressbar import *
 
progress =ProgressBar()
for i in progress(range(1000)):
    time.sleep(0.01)