#!/usr/bin/env python3
"""tests for wynnpi.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string

prg = "./wynnpi.py"


# --------------------------------------------------
def test_usage():
    """usage"""
    rv1, out1 = getstatusoutput(prg)
    assert rv1 > 0
    assert re.match("usage", out1, re.IGNORECASE)

    rv2, out2 = getstatusoutput('{} fox.txt'.format(prg))
    assert rv2 > 0
    assert re.match("usage", out2, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input():
    """bad_input"""
    for n in [0, 23]:
        rv, out = getstatusoutput('{} -n {}'.format(prg, n))
        assert out.strip() == '-n Number of terms "{}" must be between 1 and 24, inclusive'.format(n)


# --------------------------------------------------
def test_runs_ok():
    log = '.log'

    for f1, f2, n in [
        ('fox.txt', 'fox.txt', '0'),
        ('american.txt', 'british.txt', '28'),
        ('american.txt', 'american.txt', '0'),
        ('sample1.fa', 'sample2.fa', '6'),
    ]:
        for debug in [True, False]:
            if os.path.isfile(log):
                os.remove(log)

            rv, out = getstatusoutput('{} {} {} {}'.format(
                prg, '-d' if debug else '', f1, f2))

            if debug:
                assert os.path.isfile(log)

            assert rv == 0
            assert out.rstrip() == n

