#!/usr/bin/env python

import io
import os
import sys
import simplejson as json
import glob
import codecs
import argparse
from urlparse import urlparse
from collections import Counter
from datetime import datetime


def dump_count_csvs(filename, data):
    with codecs.open(filename, "w", encoding="utf8") as f:
        f.write("url,count\n")
        for k,v in data.items():
            f.write("\"%s\", %d\n" %(k,v))


#
#
# program arguments
#
#
parser = argparse.ArgumentParser(description='url extractor')
parser.add_argument("outfile", help="output filename")
parser.add_argument("infiles", help="input filenames")
parser.add_argument("--encoding", help="input encoding", default="utf8")
args = parser.parse_args()

#
# filelist
#
file_list = sorted(glob.glob(args.infiles))
file_count = len(file_list)

url_cntr = Counter()
domain_cntr = Counter()

num_tweets = 0
last_update = datetime.now()

for filename_index in range(file_count):

        filename = file_list[filename_index]
        print "opening \"%s\" (%d of %d)"%(filename, filename_index+1, file_count)
        with open(filename, "r") as f:
            # get file length
            f.seek(0, os.SEEK_END)
            file_length = f.tell()
            f.seek(0, os.SEEK_SET)


                # tweets are expected on each line
            for rawline in f:

                # check for empty lines
                rawline = rawline.strip()
                if not rawline:
                    continue

                line = codecs.decode(rawline, args.encoding)

                # convert it to json
                try:
                    tweet = None

                    #print "parsing ----"
                    #print line
                    #print "\n"*4
                    tweet = json.loads(line)

                except Exception, e:
                    print "failed to parse json: ", e
                    print line

                # continue if the tweet failed
                if tweet is None:
                    continue

                # see if this is a gnip info message, and skip if it is
                if 'info' in tweet and 'message' in tweet['info']:
                    # print "info tweet", repr(tweet)
                    continue

                if not 'text' in tweet or not 'created_at' in tweet or not 'user' in tweet:
                    print "line is not a recognized tweet..."
                    print "> ", line
                    print "----------"
                    continue

                num_tweets += 1

                try:
                    urls = tweet["entities"]["urls"]
                except KeyError:
                    continue

                if len(urls) == 0:
                    continue

                url_list = [u["expanded_url"] for u in urls]

                url_cntr.update(url_list)

                domain_cntr.update([urlparse(u).netloc for u in url_list])



                time_diff = datetime.now() - last_update
                if time_diff.total_seconds() > 10:
                    last_update = datetime.now()

                    pos = os.lseek(f.fileno(), 0, os.SEEK_CUR)
                    pct_done = (pos *100.0) / float(file_length)

                    print "%6.2f%% done. (%d tweets processed)" % (
                        pct_done,
                        num_tweets
                        )
                #lim += 1
                #if lim > 500:
                #    break

print "checking unique domains..."
uniq_domains = [urlparse(u).netloc for u in url_cntr.keys()]
uniq_domain_urls = Counter(uniq_domains)

dump_count_csvs("urls.csv", url_cntr)
dump_count_csvs("domains.csv", domain_cntr)
dump_count_csvs("unique_domains.csv", domain_cntr)

