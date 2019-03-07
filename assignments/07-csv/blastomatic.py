#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-03-06
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import csv
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

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
    out = args.outfile
    ann = args.annotations
    FILE = args.FILE

    if not os.path.exists(out) and out != '':  # check if out directory exists, and make one if false
        os.makedirs(out)

    if not os.path.exists(FILE):
        die('\"{}\" is not a file'.format(FILE))

    if not os.path.exists(ann) and ann != '':
        die('\"{}\" is not a file'.format(ann))

    with open(FILE) as csvfile:
        dict_args = {'delimiter': '\t'}
        names = ['qaccver','saccver','pident','length','mismatch','gapopen','qstart','qend','sstart','sendevalue','bitscore']

        reader = csv.DictReader(csvfile, fieldnames = names, **dict_args)

        for i, row in enumerate(reader, start=1):
            vals = dict(row)
            flds = vals.keys()
            fmt = '{} : {}'
            print('// ****** Record {} ****** //'.format(i))
            n = 0
            for key, val in vals.items():
                n += 1
                show = fmt.format(key, val)
                print(show)

# --------------------------------------------------
if __name__ == '__main__':
    main()
