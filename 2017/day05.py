#!/usr/bin/env python

def escape_one(instr):
    """
    >>> escape_one([0, 3, 0, 1, -3])
    5
    """
    pos = 0
    count = 0
    while pos >= 0 and pos < len(instr):
        instr[pos] += 1
        pos += instr[pos] - 1
        count += 1
    return count

def escape_two(instr):
    """
    >>> escape_two([0, 3, 0, 1, -3])
    10
    """
    pos = 0
    count = 0
    while pos >= 0 and pos < len(instr):
        off = instr[pos]
        instr[pos] += 1 if off < 3 else -1
        pos += off
        count += 1
    return count

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day05_input.txt")]
    print "Part 1 Answer", escape_one([int(x) for x in puzzle_input])
    print "Part 2 Answer", escape_two([int(x) for x in puzzle_input])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
