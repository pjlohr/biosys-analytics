#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-03-26
Purpose: Rock the Casbah
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'DATE', metavar='str', help='Date string')

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
    date = args.DATE

    date_re = re.compile('(?P<year>\d{4})'
                         '[/.-]?'
                         '(?P<month>\d{2})'
                         '(?:[/.-]?(?P<day>\d{2}))?')

    dates = open('eg_dates.txt', 'r')
    # dates = ['12/06']
    for line in dates:
        match = date_re.match(line)
        if match:
            print('{}-{}-{}'.format(match.group('year'),
                                    match.group('month'),
                                    match.group('day') if match.group('day') is not None else '01'))
        else:
            print('No match')


# --------------------------------------------------
if __name__ == '__main__':
    main()
