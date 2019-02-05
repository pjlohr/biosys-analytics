#!/usr/bin/env python3
"""
Author : pjlohr
Date   : 2019-02-05
Purpose: cat -n
"""

import os
import sys


# --------------------------------------------------
def main():

    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)
    i = 1
    for line in open(file):
        print(' {:2}: {}'.format(i, line), end='')
        i += 1


# --------------------------------------------------
main()

