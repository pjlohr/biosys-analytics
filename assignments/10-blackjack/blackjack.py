#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
import random
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    parser.add_argument(
        '-p', '--player_hits', help='Player hits', action='store_true')

    parser.add_argument(
        '-d', '--dealer_hits', help='Dealer hits', action='store_true')

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
def create_deck():
    """create deck of cards"""
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♥', '♠', '♣', '♦']
    prod = list(product(suits, cards))
    deck = []
    values = {}

    for tup in prod:
        deck.append(''.join(tup))
    for card in deck:
        face = list(card)[1]
        if face.isdigit():
            values[card] = int(re.findall(r'\d+', card)[0])
        elif face == 'A':
            values[card] = 1
        else:
            values[card] = 10

    return {'deck': deck, 'values': values}


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seed = args.seed
    player_hits = args.player_hits
    dealer_hits = args.dealer_hits

    if seed is not None:
        random.seed(seed)

    var = create_deck()
    deck = var['deck']
    values = var['values']

    deck.sort()
    random.shuffle(deck)

    player = []
    dealer = []

    player.append(deck.pop())
    dealer.append(deck.pop())
    player.append(deck.pop())
    dealer.append(deck.pop())

    player_sum = values[player[0]] + values[player[1]]
    dealer_sum = values[dealer[0]] + values[dealer[1]]

    if player_hits:
        player.append(deck.pop())
        player_sum += values[player[2]]

    if dealer_hits:
        dealer.append(deck.pop())
        dealer_sum += values[dealer[2]]

    print('D [{:>2}]: {} {}{}'.format(dealer_sum, dealer[0], dealer[1], ' ' + dealer[2] if dealer_hits else ''))
    print('P [{:>2}]: {} {}{}'.format(player_sum, player[0], player[1], ' ' + player[2] if player_hits else ''))

    if player_sum > 21:
        print('Player busts! You lose, loser!')
        sys.exit(0)
    elif dealer_sum > 21:
        print('Dealer busts.')
        sys.exit(0)
    elif player_sum == 21:
        print('Player wins. You probably cheated.')
        sys.exit(0)
    elif dealer_sum == 21:
        print('Dealer wins!')
        sys.exit(0)

    if dealer_sum < 18:
        print('Dealer should hit.')

    if player_sum < 18:
        print('Player should hit.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
