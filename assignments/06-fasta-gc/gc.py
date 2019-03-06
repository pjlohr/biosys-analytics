#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-02-24
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
        'FASTA', metavar='FASTA', help='Input FASTA files(s)', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Dividing line for percent GC',
        metavar='int',
        type=int,
        default=50)

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
    out = args.outdir
    fastas = args.FASTA
    thresh = args.pct_gc
    num_seq = 0
    num_files = 0

    if not 0 <= thresh <= 100:  # check for good split
        die('--pct_gc \"{}\" must be between 0 and 100'.format(thresh))

    if not os.path.exists(out):  # check if out directory exists, and make one if false
        os.makedirs(out)

    for file in fastas:
        file_path = os.path.join(os.getcwd(), file)
        if not os.path.exists(file_path):
            warn('\"{}\" is not a file'.format(file))
            continue

        low = open(os.path.join(out, str(os.path.basename(file).split('.')[0]) + '_low.fa'), 'w+')
        high = open(os.path.join(out, str(os.path.basename(file).split('.')[0]) + '_high.fa'), 'w+')
        num_files += 1
        fh = open(file_path, "r")
        print('  {}: {}'.format(num_files, os.path.basename(file_path)))

        for record in SeqIO.parse(fh, "fasta"):
            num_seq += 1
            gc = 0
            for x in str(record.seq):  # count GC content in each FASTA file
                if "C" in x:
                    gc += 1
                elif "G" in x:
                    gc += 1
            pct = gc / len(record.seq)
            if pct < thresh/100:
                SeqIO.write(record, low, "fasta")
            elif pct >= thresh/100:
                SeqIO.write(record, high, "fasta")

    print('Done, wrote {} sequences to out dir \"{}\"'.format(num_seq, out))


# --------------------------------------------------
if __name__ == '__main__':
    main()
