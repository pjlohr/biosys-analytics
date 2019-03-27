#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-03-01
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SwissProt


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
        #nargs='+',
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
    uni_file = args.FILE
    skip = args.skip
    keyword = args.keyword
    out = args.output

    if not os.path.exists(uni_file):  # check if out directory exists, and make one if false
        die('\"{}\" is not a file'.format(uni_file))

    if not os.path.exists(out):  # check if out directory exists, and make one if false
        os.makedirs(out)


# --------------------------------------------------
if __name__ == '__main__':
    main()
