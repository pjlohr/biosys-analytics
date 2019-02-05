#!/usr/bin/env python3
"""
Author : pjlohr
Date   : 2019-02-05
Purpose: head
"""

import os
import sys


# --------------------------------------------------
def main():

    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)
    
    if len(args) == 1:
        numlines = 3
    else:
        numlines = int(sys.argv[2])

    if not numlines >= 1:
        print('lines ({}) must be a positive number'.format(numlines))
        sys.exit(1)

    i = 1
    for line in open(file):
        print('{}'.format(line), end='')
        if i == numlines:
            break
        i += 1
# --------------------------------------------------
main()
