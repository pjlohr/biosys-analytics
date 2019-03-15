#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-03-01
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR',
        type=str,
        nargs='+',
        default='')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='STR',
        type=str,
        required=True,
        default='')

    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.fa')

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
    swiss = args.FILE
    skip = args.skip
    keyword = args.keyword
    out = args.output
    i = 0;
    if not os.path.exists(swiss):  # check if out directory exists, and make one if false
        die('\"{}\" is not a file'.format(swiss))

    if not os.path.exists(out):  # check if out directory exists, and make one if false
        os.makedirs(out)

    with open(swiss) as swiss_fh:
        for record in SeqIO.parse(swiss_fh, 'swiss'):
            if keyword in [x.lower() for x in record.annotations['keywords']]:
                if not any([I for I in skip if I in [x.lower() for x in record.annotations['taxonomy']]]):
                    i += 1
                    #print(record.annotations['taxonomy'])
    print(i)
    print(skip)

# --------------------------------------------------
if __name__ == '__main__':
    main()
