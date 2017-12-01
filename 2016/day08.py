#!/usr/bin/env python

import re

def rotate(l, n):
    return l[-n:] + l[:-n]

class Display(object):
    def __init__(self, columns, rows):
        self.board = [[0 for x in range(0,columns)] for x in range(0,rows)]

    def get_count(self):
        return sum([sum(r) for r in self.board])

    def rect(self, a, b):
        for x in range(0,a):
            for y in range(0,b):
                self.board[y][x] = 1

    def rotate_row(self, a, b):
        self.board[a] = rotate(self.board[a], b)

    def rotate_column(self, a, b):
        col = [x[a] for x in self.board]
        col = rotate(col, b)
        for x in range(0,len(col)):
            self.board[x][a] = col[x]

    def dump(self):
        for row in self.board:
            print ''.join(['#' if x>0 else ' ' for x in row])

def run_display(columns, rows, puzzle_input):
    display = Display(columns, rows)

    pattern = re.compile(r"(rect|column|row) .*?(\d+).+?(\d+)")

    for row in puzzle_input:
        match = pattern.search(row)
        (c,a,b) = (match.group(1), int(match.group(2)), int(match.group(3)))
        if c == 'rect':
            display.rect(a,b)
        if c == 'row':
            display.rotate_row(a,b)
        if c == 'column':
            display.rotate_column(a,b)
    return display

def part1(columns, rows, puzzle_input):
    """
    >>> part1(7, 3, ["rect 3x2", "rotate column x=1 by 1", "irotate row y=0 by 4", "rotate column x=1 by 1"])
    6
    """
    return run_display(columns, rows, puzzle_input).get_count()

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day08_input.txt")]
    print "Part 1 Answer", part1(50, 6, puzzle_input)
    print "Part 2 Answer"
    run_display(50, 6, puzzle_input).dump()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

