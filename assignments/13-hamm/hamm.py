#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-04-09
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='File inputs', nargs=2)

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true', default=False)

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
def dist(str1, str2):
    result1 = ''
    result2 = ''

    maxlen = len(str2) if len(str1) < len(str2) else len(str1)
    delta = 0
    for i in range(maxlen):
        letter1 = str1[i:i + 1]
        letter2 = str2[i:i + 1]
        if letter1 != letter2:
            delta += 1

    logging.debug('s1 = {}, s2 = {}, d = {}'.format(str1, str2, delta))
    return delta


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    file1 = args.FILE[0]
    file2 = args.FILE[1]

    logging.debug('file1 = {}, file2 = {}'.format(file1, file2))

    if not os.path.isfile(file1):
        die('\"{}\" is not a file'.format(file1))

    if not os.path.isfile(file2):
        die('\"{}\" is not a file'.format(file2))

    words1 = []
    words2 = []

    for line in open(file1, "r"):
        words1 += line.split()
    for line in open(file2, "r"):
        words2 += line.split()

    print(sum(map(dist, words1, words2)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
