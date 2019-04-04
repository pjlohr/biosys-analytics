#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-04-04
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find unclustered proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

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
    proteins = args.proteins
    out = args.outfile
    hits = args.cdhit

    pat = re.compile('[|](\d+)[|]')
    if not os.path.isfile(proteins) or not proteins:
        die('--proteins \"{}\" is not a file'.format(proteins))

    if not os.path.isfile(hits) or not hits:
        die('--cdhit \"{}\" is not a file'.format(hits))

    proteins_fh = open(proteins, "r")
    out_fh = open(out, 'w+')
    h = set()
    num_proteins = 0
    num_unclustered = 0

    for line in open(hits, "r"):
        match = pat.search(line)
        if match:
            h.add(match.group(1))

    for record in SeqIO.parse(proteins_fh, "fasta"):
        num_proteins += 1
        if record.id.split('|')[0] not in h:
            num_unclustered += 1
            SeqIO.write(record, out_fh, "fasta")

    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(num_unclustered, num_proteins, out))


# --------------------------------------------------
if __name__ == '__main__':
    main()
