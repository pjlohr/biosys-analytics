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

    capPass = password[0].upper() + password[1:]

    ok = (password == alt) or (password.upper() == alt) or (
        capPass == alt) or re.match('.?' + password + '.?', alt)

    print('ok' if ok else 'nah')


# --------------------------------------------------
main()
