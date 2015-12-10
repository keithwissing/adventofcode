#!/usr/bin/env python

def find_floor(puzzle_input):
    """
    >>> find_floor("(())")
    0
    >>> find_floor("()()")
    0
    >>> find_floor("(((")
    3
    >>> find_floor("(()(()(")
    3
    >>> find_floor("))(((((")
    3
    >>> find_floor("())")
    -1
    >>> find_floor("))(")
    -1
    >>> find_floor(")))")
    -3
    >>> find_floor(")())())")
    -3
    """
    up = puzzle_input.count('(')
    down = puzzle_input.count(')')
    print up - down

def basement(puzzle_input):
    """
    >>> basement(")")
    1
    >>> basement("()())")
    5
    """
    floor = 0
    pos = 0
    while pos < len(puzzle_input):
        if puzzle_input[pos] == '(': floor = floor + 1
        if puzzle_input[pos] == ')': floor = floor - 1
        if floor == -1:
            print pos+1
            break
        pos = pos + 1

def main():
    puzzle_input = open("input.txt").read()
    find_floor(puzzle_input)
    basement(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

