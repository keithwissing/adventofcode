#!/usr/bin/env python3

import itertools
import adventofcode

t1 = [
    '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
    '',
    '22 13 17 11  0',
    ' 8  2 23  4 24',
    '21  9 14 16  7',
    ' 6 10  3 18  5',
    ' 1 12 20 15 19',
    '',
    ' 3 15  0  2 22',
    ' 9 18 13 17  5',
    '19  8  7 25 23',
    '20 11 10 24  4',
    '14 21 16 12  6',
    '',
    '14 21 17 24  4',
    '10 16 15  9 19',
    '18  8 23 26 20',
    '22 11 13  6  5',
    ' 2  0 12  3  7',
]

def parse(lines):
    draws = [int(d) for d in lines[0].split(',')]
    boards = []
    for l in range(2, len(lines), 6):
        board = lines[l:l + 5]
        board = [[int(s) for s in l.split()] for l in board]
        boards.append(board)
    return draws, boards

def is_winner(board):
    for l in board:
        if all([c >= 100 for c in l]):
            return True
    for c in range(5):
        if all([l[c] >= 100 for l in board]):
            return True
    return False

def mark_board(board, draw):
    for l, c in itertools.product(range(5), range(5)):
        if board[l][c] == draw:
            board[l][c] += 100

def mark_boards(boards, draw):
    for board in boards:
        mark_board(board, draw)

def score(board):
    return sum([x for l in board for x in l if x < 100])

def part1(lines):
    """
    >>> part1(t1)
    4512
    """
    draws, boards = parse(lines)
    for draw in draws:
        mark_boards(boards, draw)
        for board in boards:
            if is_winner(board):
                return score(board) * draw

def part2(lines):
    """
    >>> part2(t1)
    1924
    """
    draws, boards = parse(lines)
    for draw in draws:
        mark_boards(boards, draw)
        if len(boards) == 1 and is_winner(boards[0]):
            return score(boards[0]) * draw
        boards = [b for b in boards if not is_winner(b)]

def main():
    puzzle_input = adventofcode.read_input(4)
    adventofcode.answer(1, 39984, part1(puzzle_input))
    adventofcode.answer(2, 8468, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
