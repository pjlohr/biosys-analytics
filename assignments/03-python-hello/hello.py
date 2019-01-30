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

    if len(args) < 1:
        print('Usage: {} NAME [NAME2 ...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    if len(args) < 3:
        names = ' and '.join(args)
        print('Hello to the ' + str(len(args)) + ' of you: ' + names + '!')

    else:
        names = ', '.join(sys.argv[1:-1])
        print('Hello to the ' + str(len(args)) + ' of you: ' + names + ', and ' + sys.argv[-1] + '!')

# --------------------------------------------------
main()



