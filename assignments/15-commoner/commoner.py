#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-04-19
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
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE',
        help='Input files',
        type=argparse.FileType('r', encoding='UTF-8'),
        nargs=2)

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

    parser.add_argument(
        '-t', '--table', help='Table output', action='store_true')
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
    min = args.min_len
    files = args.FILE
    hamm = args.hamming_distance
    logfile = args.logfile
    table = args.table

    file1 = args.FILE[0]
    file2 = args.FILE[1]

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    logging.debug('file1 = {}, file2 = {}'.format(file1, file2))

    words1 = []
    words2 = []

    for line in file1:
        words1 += line.split()
    for line in file2:
        words2 += line.split()

    tup = list(zip(words1, words2))
    matches = {}
    for str1, str2 in tup:
        d = dist(str1, str2)
        if (len(str1) and len(str2)) >= min:
            if d <= hamm:
                matches[(str1, str2)] = d
    matches = sorted([(x[0], x[1]) for x in matches.items()])

    for words, count in matches:
        print(words, count)
# --------------------------------------------------
if __name__ == '__main__':
    main()
