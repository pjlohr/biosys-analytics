#!/usr/bin/env python3
"""
Author : pjlohr
Date   : 2019-01-29
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():

    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    size = int(sys.argv[1])

    if 2 <= size <= 9:
        for i in range(1, size ** 2 + 1):
            print('{:3}{}'.format(i, '\n' if i%size == 0 else ''), end='')

    else:
        print('NUM (' + str(size) + ') must be between 1 and 9')
        sys.exit(1)

# --------------------------------------------------
main()
