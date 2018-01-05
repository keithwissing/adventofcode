#!/usr/bin/env python

import adventofcode

def part1(steps):
    """
    >>> part1(3)
    638
    """
    buffer = [0]
    pos = 0
    for next in xrange(1, 2018):
        pos = (pos + steps) % len(buffer)
        buffer = buffer[:pos+1] + [next] + buffer[pos+1:]
        pos += 1
    return buffer[(pos+1)%len(buffer)]

def part2(steps):
    return part2var(steps, 50000000)

def part2var(steps, iterations):
    """
    >>> part2var(3, 1)
    1
    >>> part2var(3, 8)
    5
    >>> part2var(3, 9)
    9
    """
    afterz = 0
    pos = 0
    blen = 1
    for next in xrange(1, iterations+1):
        pos = (pos + steps) % blen
        if pos == 0:
            afterz = next
        blen += 1
        pos += 1
    return afterz

def main():
    puzzle_input = adventofcode.read_input(17)
    steps = int(puzzle_input)
    adventofcode.answer(1, 1547, part1(steps))
    adventofcode.answer(2, 31154878, part2(steps))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
