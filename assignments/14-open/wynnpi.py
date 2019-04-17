#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-04-16
Purpose: Demonstrate Wynn Epsilon Convergence Acceleration of the Gregory-Leibniz series
"""

import argparse
import sys
import numpy as np


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Wynn Epsilon',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--numterms',
        help='Number of series terms',
        metavar='INT',
        type=int,
        default=10)

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


def wynnepsilon(sn, r):
    """Perform Wynn Epsilon Convergence Algorithm"""

    n = 2 * int(r) + 1
    E = np.zeros(shape=(n+1, n+1))

    for i in range(0, n):
        E[i + 1, 1] = sn[i]



    # for i in range(2, n):
    #     for j in range(2, i):
    #         E[i, j] = E[i - 1, j - 2] + 1 / (E[i, j - 1] - E[i - 1, j - 1])
    # print(E)
    # Er = E(:, 2: 2:n + 1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    N = args.numterms
    Psum = []
    sum = 0
    for k in range(0, N):
        term = 4 * np.power(-1, k) / (2 * k + 1)
        sum += term
        Psum.append(sum)

    wynnepsilon(Psum, (N - 1) / 2)


# --------------------------------------------------
if __name__ == '__main__':
    main()
