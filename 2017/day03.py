#!/usr/bin/env python

import math
import itertools

def move_steps(puzzle_input):
    """
    >>> move_steps(1)
    0
    >>> move_steps(12)
    3
    >>> move_steps(23)
    2
    >>> move_steps(1024)
    31
    """
    puzzle_input = int(puzzle_input)
    if puzzle_input == 1:
        return 0
    l = int(math.floor(math.sqrt(puzzle_input-1)))
    l = l + l % 2 + 1
    d = l**2 - puzzle_input
    return l/2 + abs((d % (l-1)) - l/2)

def move_steps_2(puzzle_input):
    """
    >>> move_steps_2(1)
    0
    >>> move_steps_2(12)
    3
    >>> move_steps_2(23)
    2
    >>> move_steps_2(1024)
    31
    """
    puzzle_input = int(puzzle_input)
    pos = (0, 0)
    for _ in range(puzzle_input - 1):
        pos = spiral_next_pos(pos)
    (x, y) = pos
    return abs(x) + abs(y)

def list_of_spiral_coordinates(count):
    """
    >>> list_of_spiral_coordinates(26)
    [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (2, -1), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (-1, 2), (-2, 2), (-2, 1), (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2), (3, -2)]
    """
    pos = (0, 0)
    result = [pos]
    for _ in range(count - 1):
        pos = spiral_next_pos(pos)
        result.append(pos)
    return result

def spiral_next_pos(pos):
    (x, y) = pos
    return spiral_next(x, y)

def spiral_next(x, y):
    """
    >>> spiral_next(0, 0)
    (1, 0)
    >>> spiral_next(2, 1)
    (2, 2)
    >>> spiral_next(1, 1)
    (0, 1)
    >>> spiral_next(0, 1)
    (-1, 1)
    >>> spiral_next(0, 1)
    (-1, 1)
    >>> spiral_next(-1, 1)
    (-1, 0)
    """
    if x >= 0 and x == -y:
        x += 1
    elif x > 0 and x > -y and y < x: # right moving up
        y += 1
    elif y > 0 and x > -y: # top moving left
        x += -1
    elif x < 0 and y > x: # left moving down
        y += -1
    elif y < 0 and x < -y: # bottom moving right
        x += 1
    return (x, y)

def part2(puzzle_input):
    """
    >>> part2(700)
    747
    """
    puzzle_input = int(puzzle_input)
    known = {(0, 0): 1}
    pos = (0, 0)
    nv = 1
    while nv < puzzle_input:
        pos = spiral_next_pos(pos)
        nv = value(known, pos)
        known[pos] = nv
    return nv

def value(known, pos):
    """
    >>> value({}, (0,0))
    0
    """
    (x, y) = pos
    return sum([known.get((dx, dy), 0) for (dx, dy) in itertools.product(range(x-1, x+2), range(y-1, y+2))])

def main():
    puzzle_input = open("day03_input.txt").read().rstrip()
    print "Part 1 Answer", move_steps(puzzle_input)
    print "Part 1 Answer", move_steps_2(puzzle_input)
    print "Part 2 Answer", part2(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
