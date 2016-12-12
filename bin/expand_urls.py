#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import pandas as pd
import numpy as np
import re
import ujson as json
import glob
import bz2
from ezconf import ConfigFile
from datetime import datetime
from multiprocessing import Pool, Process, freeze_support
from functools import partial
import fcntl
import signal
import requests
from urlparse import urlparse


# disable warnings
requests.packages.urllib3.disable_warnings()


UA_STRING = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"



def resolve_url(url_dict):
    url = url_dict.get("url", None) 
    count = url_dict.get("count", "")

    status_code = None
    resolved_url = None
    domain = None

    if url is not None:
        try:
            headers = {
                "user-agent": UA_STRING
            }
            r = requests.head(
                url,
                allow_redirects=True,
                verify=False,
                headers=headers)
            # some places return 400 errors for head
            if r.status_code >= 400 or r.status_code < 500:
                r = requests.get(
                    url,
                    allow_redirects=True,
                    verify=False,
                    headers=headers)
            status_code = r.status_code
            resolved_url = r.url
        except Exception, e:
            status_code = "Exception: ", e
            pass


    if resolved_url is not None:
        re.sub(r"www\.", "", urlparse(resolved_url).netloc).lower()

    return {
        'url': url,
        'status_code': status_code,
        'resolved_url': resolved_url,
        'domain': domain,
        'count': count
    }



def sp_start(rows):
    total = len(rows)
    arr = []
    for i, r in enumerate(rows):
        if i % 50:
            print "%2.2f%% (%d finished)" % ((i*100/total), i)
            arr.append(resolve_url(r))

    return arr


def mp_start(rows):
    total = len(rows)

    # pool
    mpool = Pool(processes=32)


    results = None
    try:
        results = mpool.map(resolve_url, rows)
        
    except KeyboardInterrupt:
        print "Quitting!!!"
        mpool.terminate()
        mpool.join()
    else:
        mpool.close()
        mpool.join()
        mpool = None

    return results




if __name__ == '__main__':
    freeze_support()

    #
    #
    # program arguments
    #
    #
    parser = argparse.ArgumentParser(description='live thread dumper')
    parser.add_argument('input', help='csv input file')
    parser.add_argument('outfile', help='csv outfile')
    parser.add_argument('--procs', default=32, type=int, help='number of processes')
    args = parser.parse_args()



    # read csv
    csv = pd.read_csv(args.input)
    csv = csv.fillna('')


    rows = csv.to_dict(orient='records')

    if args.procs < 2:
        new_rows = sp_start(rows)
    else:
        new_rows = mp_start(rows)


    new_csv = pd.DataFrame.from_records(new_rows)


    new_csv.to_csv(args.outfile, new_rows)


