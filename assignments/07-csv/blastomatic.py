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
        sys.stdout = open(out, 'w')

    if not os.path.isfile(FILE):
        die('\"{}\" is not a file'.format(FILE))

    if not os.path.isfile(ann) and ann != '':
        die('\"{}\" is not a file'.format(ann))
    matches = []
    with open(FILE, newline='') as csvfile:
        print('seq_id\tpident\tgenus\tspecies')
        blastreader = csv.reader(csvfile, delimiter='\t')
        for brow in blastreader: # Loop through rows of blast file
            with open(ann, newline='') as annfile:
                annreader = csv.reader(annfile)
                for arow in annreader:   #loop through rows of annotation file
                    if brow[1] == arow[0]:
                        print('{}\t{}\t{}\t{}'.format(brow[1], brow[2], arow[6] if arow[6] != '' else 'NA', arow[7] if arow[7] != '' else 'NA'))
                        matches.append(brow[1])

            if brow[1] not in matches:
                warn('cannot find seq \"{}\" in lookup'.format(brow[1]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
