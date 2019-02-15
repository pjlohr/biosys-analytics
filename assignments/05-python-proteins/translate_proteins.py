#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-02-12
Purpose: Rock the Casbah
"""

import argparse
import sys
import os.path

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'DNA', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='str',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='FILE',
        type=argparse.FileType('w'),
        default='out.txt')

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
    table = args.codons
    string = args.DNA
    output = args.outfile
    d = {}

    if os.path.exists(table):
        with open(table, 'r') as table:
            for line in table:
                col = line.split()
                d[col[0]] = col[1]

            k = 3
            n = len(string) - k + 1

            for i in range(0, n, k):
                codon = string[i:i + k].upper()
                if codon in d:
                    output.write(d[codon])
                else:
                    output.write('-')

            print('Output written to "{}"'.format(output.name))
    # Do Stuff with file
    else:
        die("--codons \"{}\" is not a file".format(table))



# --------------------------------------------------
if __name__ == '__main__':
    main()
