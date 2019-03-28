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

    short = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
    long = ('January February March April May June July August '
            'September October November December').split()

    d_short = dict(map(reversed, enumerate(short, 1)))
    d_long = dict(map(reversed, enumerate(long, 1)))

    if not date.strip().isdigit():
        date_re = re.compile('(?P<first>.+?)'
                             '[,/-]'
                             '[ ]?(?P<second>\d+)'
                             '(?:[-]?(?P<third>\d{1,2}))?')
    else:
        date_re = re.compile('(?P<first>\d{4})'
                             '(?P<second>\d{2})'
                             '(?P<third>\d{2})')

    match = date_re.match(date)
    if match:
        first = match.group('first')
        second = int(match.group('second'))
        third = match.group('third')
        third = int(third) if third is not None else None

        if not first.isdigit():  # month as string
            first = d_short[first] if len(first) <= 3 else d_long[first]
            first, second = second, first  # swap

        elif first.isdigit() and len(first) <= 2:  # handle cases like 2/14
            third = None
            first = int(first)
            second = second + 2000  # bad way of formatting
            first, second = second, first  # swap

        print('{}-{:02d}-{:02d}'.format(first, second, third if third is not None else 1))

    else:
        print('No match')


# --------------------------------------------------
if __name__ == '__main__':
    main()
