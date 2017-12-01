#!/usr/bin/env python
import string

def get_decompressed_length(puzzle_input):
    """
    >>> get_decompressed_length("ADVENT")
    6
    >>> get_decompressed_length("A(1x5)BC")
    7
    >>> get_decompressed_length("(3x3)XYZ")
    9
    >>> get_decompressed_length("A(2x2)BCD(2x2)EFG")
    11
    >>> get_decompressed_length("(6x1)(1x3)A")
    6
    >>> get_decompressed_length("X(8x2)(3x3)ABCY")
    18
    """
    dl = 0
    pos = 0
    while pos < len(puzzle_input):
        if puzzle_input[pos] == '(':
            end = string.index(puzzle_input, ')', pos)
            parts = [int(x) for x in puzzle_input[pos+1:end].split('x')]
            dl = dl + parts[0] * parts[1]
            pos = end + parts[0]
        else:
            dl = dl + 1
        pos = pos + 1
    return dl

def version2(puzzle_input):
    """
    >>> version2("(3x3)XYZ")
    9
    >>> version2("X(8x2)(3x3)ABCY")
    20
    >>> version2("(27x12)(20x12)(13x14)(7x10)(1x12)A")
    241920
    >>> version2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")
    445
    """
    dl = 0
    pos = 0
    while pos < len(puzzle_input):
        if puzzle_input[pos] == '(':
            end = string.index(puzzle_input, ')', pos)
            parts = [int(x) for x in puzzle_input[pos+1:end].split('x')]
            sub = puzzle_input[end+1:end+1+parts[0]]
            exp = version2(sub)
            dl = dl + parts[1] * exp
            pos = end + parts[0]
        else:
            dl = dl + 1
        pos = pos + 1
    return dl

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day09_input.txt")]
    print "Part 1 Answer", get_decompressed_length(puzzle_input[0])
    print "Part 2 Answer", version2(puzzle_input[0])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

