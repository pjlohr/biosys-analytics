#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import random
from itertools import product
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='\"War\" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

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


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seed = args.seed

    if seed is not None:
        random.seed(seed)

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♥', '♠', '♣', '♦']
    prod = list(product(suits, cards))
    deck = []
    values = {}
    result = ''
    final = ''

    for tup in prod:
        deck.append(''.join(tup))
    for card in deck:
        face = list(card)[1]
        if face.isdigit():
            values[card] = int(re.findall(r'\d+', card)[0])
        elif face == 'J':
            values[card] = 11
        elif face == 'Q':
            values[card] = 12
        elif face == 'K':
            values[card] = 13
        elif face == 'A':
            values[card] = 14

    deck.sort()
    random.shuffle(deck)
    p1wins = 0
    p2wins = 0

    while len(deck) > 1:
        p1 = deck.pop()
        p2 = deck.pop()
        if values[p1] > values[p2]:
            result = 'P1'
            p1wins += 1
        elif values[p1] < values[p2]:
            result = 'P2'
            p2wins += 1
        elif values[p1] == values[p2]:
            result = 'WAR!'

        print('{:>3} {:>3} {}'.format(p1, p2, result))
    if p1wins > p2wins:
        final = 'Player 1 wins'
    elif p2wins > p1wins:
        final = 'Player 2 wins'
    elif p1wins == p2wins:
        final = 'DRAW'
    print('P1 {} P2 {}: {}'.format(p1wins, p2wins, final))


# --------------------------------------------------
if __name__ == '__main__':
    main()
