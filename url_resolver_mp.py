#!/usr/bin/env python
#

import sys
import io
import os 
from multiprocessing import Pool, freeze_support
from functools import partial
from datetime import datetime
import argparse
import requests
import csv
import codecs
import pandas as pd

# disable warnings
requests.packages.urllib3.disable_warnings()


UA_STRING = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"


class StatusUpdater(object):

    def __init__(self, update_time = 5, count = 0, current_val = 0, total_val = 0, total_added = 0):
        self.update_time = update_time
        self.last_display_time = datetime.now()
        self.count = count
        self.current_val = current_val
        self.total_val = total_val
        self.total_added = 0
        self.total_files = 0
        self.current_file = 0

    def update(self, force=False):
        # update progress display if necessary
        cur_time = datetime.now()
        time_since_last_update = cur_time - self.last_display_time
        if force or time_since_last_update.total_seconds() > self.update_time:
            self.last_display_time = cur_time
            progress = self.current_val * 100.0 / self.total_val
            print "File %d / %d - parsed %d tweets (%2.2f%% finished). %d added."%(self.current_file+1, self.total_files, self.count, progress, self.total_added)



def resolve_url(url_dict):
    url = url_dict.get("url", None) 
    count = url_dict.get("count", "")
    count = count.strip() if count is not None else None
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
            return (url, r.status_code, r.url, count)
        except:
            return (url, None, None, count)
    return (None, None, None, count)



#
#
# program arguments
#
#
parser = argparse.ArgumentParser(description="url resolver")
parser.add_argument("input", help="input csv file with a url column")
parser.add_argument("output", help="name of output file")
parser.add_argument("-l", "--limit", help="limit", type=int, default=0)

args = parser.parse_args()


if __name__ == "__main__":
    freeze_support()

    with open(args.input, "r") as infile:
        with codecs.open(args.output, "w", encoding="utf8") as outfile:
                        
            # get file length
            infile.seek(0, os.SEEK_END)
            file_length = infile.tell()
            infile.seek(0, os.SEEK_SET)

            # pool
            mp = Pool(processes=32)
            su = StatusUpdater()
            # update status_updater
            su.total_val = file_length

            dr = UnicodeDictReader(infile)

            for r in mp.imap_unordered(resolve_url, dr, chunksize=16):
                line = "\"%s\",%s,\"%s\",%s\n" % (
                    r[0],
                    r[1],
                    r[2],
                    r[3])
                outfile.write(line)
                su.current_val = os.lseek(
                    infile.fileno(),
                    0,
                    os.SEEK_CUR)
                su.update()
