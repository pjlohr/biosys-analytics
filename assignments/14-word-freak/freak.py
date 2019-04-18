#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-04-18
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print word frequencies',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE',
        help='File input(s)',
        type=argparse.FileType('r', encoding='UTF-8'),
        nargs='+')

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)

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
    sort = args.sort
    min = args.min
    files = args.FILE
    d = defaultdict(int)

    words = []
    for file in files:
        for line in file:
            words += line.split()

    for word in words:
        strip = re.sub('[^a-zA-Z0-9]', '', word).lower()
        if len(strip) > 0:
            d[strip] += 1
    if sort == 'frequency':
        pairs = sorted([(x[1], x[0]) for x in d.items()])
        pairs = list(map(lambda s: (s[1], s[0]), pairs))
    else:
        pairs = sorted([(x[0], x[1]) for x in d.items()])

    for word, count in pairs:
        if int(count) >= min:
            print('{:20} {}'.format(word, count))


# --------------------------------------------------
if __name__ == '__main__':
    main()
