#!/usr/bin/env python

import adventofcode

def interations_to_loop(banks):
    """
    >>> interations_to_loop([0, 2, 7, 0])
    5
    """
    count, _ = find_loop(banks)
    return count

def size_of_loop(banks):
    """
    >>> size_of_loop([0, 2, 7, 0])
    4
    """
    _, banks = find_loop(banks)
    count, _ = find_loop(banks)
    return count

def find_loop(banks):
    count = 0
    seen = { str(banks) : 1}
    while True:
        count += 1
        banks = reallocate(banks)
        if seen.get(str(banks)) == 1:
            break
        seen[str(banks)] = 1
    return count, banks

def reallocate(banks):
    """
    >>> reallocate([0, 2, 7, 0])
    [2, 4, 1, 2]
    >>> reallocate([2, 4, 1, 2])
    [3, 1, 2, 3]
    >>> reallocate([3, 1, 2, 3])
    [0, 2, 3, 4]
    >>> reallocate([0, 2, 3, 4])
    [1, 3, 4, 1]
    >>> reallocate([1, 3, 4, 1])
    [2, 4, 1, 2]
    """
    n = len(banks)
    m = max(banks)
    pos = banks.index(m)
    banks[pos] = 0
    while m > 0:
        pos = (pos + 1) % n
        banks[pos] += 1
        m -= 1
    return banks

def main():
    puzzle_input = adventofcode.read_input(6)
    puzzle_input = [int(x) for x in puzzle_input.split()]
    adventofcode.answer(1, 6681, interations_to_loop(puzzle_input))
    adventofcode.answer(2, 2392, size_of_loop(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
