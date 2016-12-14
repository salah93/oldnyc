#!/usr/bin/python
#
# Determine the sizes of a bunch of images.
#
# Usage:
# ./extract-sizes.py '*.jpg' > sizes.txt
#
# Produces a CSV file with three columns:
# file-basename-no-extension,width,height

import re
import subprocess
import sys
from glob import glob
from os.path import splitext, basename


def get_size(patterns):
    dimensions = []
    for pattern in patterns:
        for path in glob(pattern):
            size_str = subprocess.check_output(['identify', path])
            m = re.search(r' (\d+)x(\d+) ', size_str)
            try:
                width, height = [int(x) for x in m.groups()]
                assert width > 0
                assert height > 0
            except:
                return dimensions
            base, _ = splitext(basename(path))
            dimensions.append('%s,%d,%d' % (base, width, height))
    return dimensions


if __name__ == '__main__':
    dimensions = get_size(sys.argv[1:])
    print(dimensions)
