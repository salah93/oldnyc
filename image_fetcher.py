#!/usr/bin/python
#
# Fetch full images from the library for a random subset of records.

from argparse import ArgumentParser
import random

import fetcher
import record

if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument("-n", "--num", dest="num",
                    default=100, type=int,
                    help="How many images to fetch.")
  parser.add_argument("", "--seed", dest="seed", type=int, default=12345,
                    help="Random number seed.")
  parser.add_argument("-c", "--output_dir", dest="cache_dir", default="images",
                    help="Images destination dir")
  parser.add_argument("-s", "--secs", dest="secs", type=int, default=5,
                    help="Number of seconds to wait between fetches.")

  args = parser.parse_args()

  rs = record.AllRecords()
  rand = random.Random(args.seed)
  rand.shuffle(rs)
  f = fetcher.Fetcher(args.cache_dir, args.secs)
  for i, r in enumerate(rs[:args.num]):
    print("%03d Fetching %s" % (i, r.photo_url))
    f.Fetch(r.photo_url)
