#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-04-02
Purpose: Rock the Casbah
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    password = args[0]
    alt = args[1]
    find = re.compile('.?' + password + '.?')
    match = find.match(alt)
    ok = False

    if password == alt:
        ok = True
    elif password.upper() == alt:
        ok = True
    elif password.capitalize() == alt:
        ok = True
    elif match:
        ok = True

    print('ok' if ok else 'nah')


# --------------------------------------------------
main()
