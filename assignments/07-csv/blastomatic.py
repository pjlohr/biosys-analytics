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
    results = {}
    if not os.path.isfile(out) and out != '':  # check if out directory exists, and make one if false
        open(out, 'w')

    if not os.path.isfile(FILE):
        die('\"{}\" is not a file'.format(FILE))

    if not os.path.isfile(ann) and ann != '':
        die('\"{}\" is not a file'.format(ann))

    with open(FILE) as csvfile, open(ann) as annfile:
        dict_args = {'delimiter': '\t'}
        blastnames = ['qaccver','saccver','pident','length','mismatch','gapopen','qstart','qend','sstart','sendevalue','bitscore']
        blastreader = csv.DictReader(csvfile, fieldnames = blastnames, **dict_args)
        annreader = csv.DictReader(annfile, **dict_args)

        for i, brow in enumerate(blastreader, start=1):
            for j, arow in enumerate(annreader, start=1):
                blastvals = dict(brow)
                annvals = dict(arow)

                for bkey, bval in blastvals.items():
                    for akey, aval in annvals.items():
                        print(akey)

# --------------------------------------------------
if __name__ == '__main__':
    main()
