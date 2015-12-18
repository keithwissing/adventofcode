#!/usr/bin/env python

import itertools
import sys

def ways_to_fill(total, sizes, test):
    """
    >>> ways_to_fill(25, [20, 15, 10, 5, 5], lambda x: True)
    {'count': 4, 'minlen': 2}
    """
    count = 0
    minlen = sys.maxint
    for n in range(1, len(sizes)+1):
        for c in itertools.combinations(sizes, n):
            if sum(c) == total and test(c):
                count += 1
                minlen = min(minlen, len(c))
    return {'count': count, 'minlen': minlen}

def two_parts(total, sizes):
    """
    >>> two_parts(25, [20, 15, 10, 5, 5])
    Part 1 4
    Part 2 3
    """
    result = ways_to_fill(total, sizes, lambda x: True)
    print 'Part 1', result['count']
    part2 = ways_to_fill(total, sizes, lambda x: len(x) == result['minlen'])
    print 'Part 2', part2['count']

def main():
    puzzle_input = [int(line.strip()) for line in open('input.txt')]
    print puzzle_input
    two_parts(150, puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

