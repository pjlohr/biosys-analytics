#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
import os
from statistics import mean

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Average all the numbers in a document',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='Input file(s)', nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    FILES = args.FILE

    pat = re.compile(r"[+-]?\d+(?:\.\d+)?")

    for file in FILES:
        if not os.path.isfile(file):
            warn('\"{}\" is not a file'.format(file))
            continue
        base = os.path.basename(file)
        numbers = open(file).read()

        match = list(map(float, pat.findall(numbers)))

        if match:
            avg = mean(match)
            print('{:10.02f}: {}'.format(avg, base))
        else:
            print('{:10.02f}: {}'.format(0.00, base))


# --------------------------------------------------
if __name__ == '__main__':
    main()
