#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-04-09
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
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='FASTA file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='Overlap',
        metavar='int',
        type=int,
        default=3)

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
def find_kmers(s, k):
    kmers = []
    for i in range(len(s) + 1):
        match = s[i:i + k]
        if len(match) == k:
            kmers.append(match)

    return kmers


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    k = args.overlap
    fasta = args.FILE

    if not os.path.isfile(fasta):
        die('"{}" is not a file'.format(fasta))

    if k <= 0:
        die('-k "{}" must be a positive integer'.format(k))

    fasta_fh = open(fasta, "r")
    begin = {}
    end = {}
    for record in SeqIO.parse(fasta_fh, "fasta"):
        begin[record.id] = str(record.seq[:k])
        end[record.id] = str(record.seq[-k:])

    for eid, ekmer in end.items():
        for bid, bkmer in begin.items():
            if ekmer == bkmer and eid != bid:
                print(eid, bid)


# --------------------------------------------------
if __name__ == '__main__':
    main()
