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
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    num_vowels = 0
    for char in sys.argv[1]:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    if num_vowels != 1:
        print('There are ' + str(num_vowels) + ' vowels in "' + sys.argv[1] + '."')
    else:
        print('There is ' + str(num_vowels) + ' vowel in "' + sys.argv[1] + '."')
# --------------------------------------------------
main()


