#!/usr/bin/env python3
"""
Author : pjlohr
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='---------')

    parser.add_argument(
        '-p',
        '--player',
        help='Player',
        metavar='str',
        type=str)

    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
        metavar='int',
        type=int)

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
def print_state(char_array):
    """print board state"""
    view = [''] * 9

    for i in range(0, 9):
        if char_array[i] == 'X':
            view[i] = 'X'
        elif char_array[i] == 'O':
            view[i] = 'O'
        else:
            view[i] = str(i + 1)
    print('-------------')
    print('{}{}{}'.format('| ', ' | '.join(view[0:3]), ' |'))
    print('-------------')
    print('{}{}{}'.format('| ', ' | '.join(view[3:6]), ' |'))
    print('-------------')
    print('{}{}{}'.format('| ', ' | '.join(view[6:9]), ' |'))
    print('-------------')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    state = list(args.state)
    player = args.player
    cell = args.cell
    set = '.-XO'

    if not any([x in state for x in set]) or len(state) < 9:
        print('Invalid state "{}", must be 9 characters of only -, X, O'.format(args.state))
        sys.exit(1)

    if player and player != 'X' and player != 'O':
        print('Invalid player "{}", must be X or O'.format(player))
        sys.exit(1)

    if cell is not None and not (1 <= cell <= 9):
        print('Invalid cell "{}", must be 1-9'.format(cell))
        sys.exit(1)

    if cell is None and player is None:
        print_state(state)

    elif not all([cell, player]):
        print('Must provide both --player and --cell')
        sys.exit(1)

    elif all([cell, player]):

        if state[cell - 1] == 'O' or state[cell - 1] == 'X':
            print('Cell {} already taken'.format(cell))
            sys.exit(1)

        else:
            state[cell - 1] = player
            print_state(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()