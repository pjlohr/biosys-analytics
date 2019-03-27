#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-03-12
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        type=int,
        default=10)

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
    num_bottles = args.num_bottles

    if num_bottles < 1:
        die('Number of bottles must be greater than 1')

    for i in range(num_bottles, 0, -1):
        line1 = '{} {} of beer on the wall,\n'.format(i, 'bottle' if i == 1 else 'bottles')
        line2 = '{} {} of beer,\n'.format(i, 'bottle' if i == 1 else 'bottles')
        line3 = 'Take one down, pass it around,\n'
        line4 = '{} {} of beer on the wall!{}'.format(i - 1, 'bottle' if i-1 == 1 else 'bottles', '' if i-1 == 0 else '\n')
        print('{}{}{}{}'.format(line1, line2, line3, line4))


# --------------------------------------------------
if __name__ == '__main__':
    main()
