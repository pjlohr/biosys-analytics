#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-04-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import logging
import re
import io
from tabulate import tabulate as tbl


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE',
        help='Input files',
        type=argparse.FileType('r', encoding='UTF-8'),
        nargs=2)

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

    parser.add_argument(
        '-t', '--table', help='Table output', action='store_true')
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
def dist(str1, str2):
    maxlen = len(str2) if len(str1) < len(str2) else len(str1)
    delta = 0
    for i in range(maxlen):
        letter1 = str1[i:i + 1]
        letter2 = str2[i:i + 1]
        if letter1 != letter2:
            delta += 1

    logging.debug('s1 = {}, s2 = {}, d = {}'.format(str1, str2, delta))
    return delta


# --------------------------------------------------
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n


# --------------------------------------------------
def uniq_words(file, min_len):
    words = set()

    for line in file:
        for word in line.split():
            word = re.sub('[^a-zA-Z0-9]', '', word).lower()
            if len(word) >= min_len:
                words.add(word)

    return words


# --------------------------------------------------
def test_uniq_words():
    """Test uniq_words"""

    s1 = '?foo, "bar", FOO: $fa,'
    s2 = '%Apple.; -Pear. ;bANAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == {'foo', 'bar', 'fa'}

    assert uniq_words(io.StringIO(s1), 3) == {'foo', 'bar'}

    assert uniq_words(io.StringIO(s2), 0) == {'apple', 'pear', 'banana'}

    assert uniq_words(io.StringIO(s2), 4) == {'apple', 'pear', 'banana'}

    assert uniq_words(io.StringIO(s2), 5) == {'apple', 'banana'}


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    min_len = args.min_len
    files = args.FILE
    hamm = args.hamming_distance
    logfile = args.logfile
    table = args.table

    logging.basicConfig(
        filename=logfile,
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    file1 = files[0]
    file2 = files[1]

    logging.debug('file1 = {}, file2 = {}'.format(file1, file2))

    if hamm < 0:
        die('--distance "{}" must be > 0'.format(hamm))

    words1 = sorted(uniq_words(file1, min_len))
    words2 = sorted(uniq_words(file2, min_len))
    matches = {}
    for str1 in words1:
        for str2 in words2:
            d = dist(str1, str2)
            if d <= hamm:
                matches[(str1, str2)] = d

    if len(matches) > 0:
        t = []
        for pairs, count in matches.items():
            col1 = pairs[0]
            col2 = pairs[1]
            col3 = count
            column = col1, col2, col3
            t.append(column)

        if table:
            print(tbl(t, headers=['word1', 'word2', 'distance'], tablefmt='psql'))
        else:
            print('{}\t{}\t{}'.format('word1', 'word2', 'distance'))
            for row in t:
                print('{}\t{}\t{}'.format(row[0], row[1], row[2]))

    else:
        print('No words in common.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
