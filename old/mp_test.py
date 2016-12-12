#!/usr/bin/env python
#

import sys
import io
from multiprocessing import Pool, freeze_support, Queue
from functools import partial
from time import sleep
from datetime import datetime

def do_square(x):
    #sleep(2)
    return x*x



results = []

if __name__ == "__main__":
    freeze_support()

    # pool
    first = datetime.now()
    mp = Pool(processes=2)
    for x in range(200000):
        mp.apply_async(do_square, args=(x), callback=results.append)

    dur = datetime.now() - first
    print "took %f secs" % (dur.total_seconds())

    print results
