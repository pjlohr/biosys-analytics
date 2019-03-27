#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-02-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'DIR', metavar='DIR', help='Directory', nargs='+')

    parser.add_argument(
        '-w',
        '--width',
        help='Width',
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
    width = args.width
    directories = args.DIR

    for dir in directories:
        d = {}
        if not os.path.isdir(dir):
            warn('\"{}\" is not a directory'.format(dir))
            continue
        else:
            for file in os.listdir(dir):
                file_path = os.path.join(os.getcwd(), dir, file)
                fh = open(file_path, "r")
                line = fh.readline().strip()
                d[file] = line

        print(dir)
        for k, v in sorted(d.items(), key=lambda x: x[1]):
            print('{} {} {}'.format(v, '.' * (width - len(v) - len(k)) if len(v) <= width else '', k))

        # sort dictionary
        # print dir name
        # print formatted sorted dict


# --------------------------------------------------
if __name__ == '__main__':
    main()
