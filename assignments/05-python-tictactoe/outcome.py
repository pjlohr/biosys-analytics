#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-02-14
Purpose: Rock the Casbah
"""

import os
import sys
import re


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def find_board(char_array):
    """determines state in terms of -, X, O"""
    view = [''] * 9

    for i in range(0, 9):
        if char_array[i] == 'X':
            view[i] = 'X'
        elif char_array[i] == 'O':
            view[i] = 'O'
        else:
            view[i] = str(i + 1)

    return view


# --------------------------------------------------
def print_state(char_array):
    """print board state"""
    view = char_array
    print('-------------')
    print('{}{}{}'.format('| ', ' | '.join(view[0:3]), ' |'))
    print('-------------')
    print('{}{}{}'.format('| ', ' | '.join(view[3:6]), ' |'))
    print('-------------')
    print('{}{}{}'.format('| ', ' | '.join(view[6:9]), ' |'))
    print('-------------')


# --------------------------------------------------
def check(board):
    # check if previous move caused a win on vertical line

    for x in range(0, 3):
        for y in range(0, 3):
            # check if previous move caused a win on vertical line
            if grid(0, y, board) == grid(1, y, board) == grid(2, y, board):
                print('{} has won'.format(grid(x, y, board)))
                return True

            # check if previous move caused a win on horizontal line
            if grid(x, 0, board) == grid(x, 1, board) == grid(x, 2, board):
                print('{} has won'.format(grid(x, y, board)))
                return True

            # check if previous move was on the main diagonal and caused a win
            if x == y and grid(0, 0, board) == grid(1, 1, board) == grid(2, 2, board):
                print('{} has won'.format(grid(x, y, board)))
                return True

            # check if previous move was on the secondary diagonal and caused a win
            if x + y == 2 and grid(0, 2, board) == grid(1, 1, board) == grid(2, 0, board):
                print('{} has won'.format(grid(x, y, board)))
                return True

    print('No winner')
    return False


# --------------------------------------------------
def grid(row, col, array):
    """Take in row/column position of array, return Axy"""
    return array[3 * row + col]


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) < 1:
        die('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))

    state = list(sys.argv[1])

    if not re.search('^[.XO]{9}$', ''.join(state)):
        die('State "{}" must be 9 characters of only ., X, O'.format(''.join(state)))

    board = find_board(state)  # returns character array of number, X, O
    check(board)

# --------------------------------------------------
if __name__ == '__main__':
    main()
