#!/usr/bin/env python3
"""tests for hamm.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string
import hamm

prg = "./hamm.py"


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
    bad_int = [0, 23]
    rv, out = getstatusoutput('{} {} {}'.format(prg, 'fox.txt', bad_file))
    assert rv > 0
    assert out == '"{}" is not a file'.format(bad_file)


# --------------------------------------------------
def test_dist():
    """dist ok"""
    tests = [('foo', 'boo', '1'), ('foo', 'faa', '2'), ('foo', 'foobar', '3'),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              '9'), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', '10')]

    for s1, s2, n in tests:
        d = hamm.dist(s1, s2)
        assert d == int(n)

