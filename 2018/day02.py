#!/usr/bin/env python

import itertools
import adventofcode

def contains_exactly(box, target_count):
    """
    >>> contains_exactly("abcdef", 2)
    False
    """
    chars = list(box)
    chars.sort()
    return target_count in [chars.count(x) for x in set(chars)]

def rudimentary_checksum(puzzle_input):
    """
    >>> rudimentary_checksum([ "abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab" ])
    12
    """
    twos = sum([contains_exactly(x, 2) for x in puzzle_input])
    threes = sum([contains_exactly(x, 3) for x in puzzle_input])
    return twos * threes

def common_letters(box1, box2):
    """
    >>> common_letters("fghij", "fguij")
    'fgij'
    """
    return "".join([box1[x] for x in range(len(box1)) if box1[x] == box2[x]])

def common_letters_in_box_ids(puzzle_input):
    """
    >>> common_letters_in_box_ids([ "abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz" ])
    'fgij'
    """
    for x in itertools.combinations(puzzle_input, 2):
        common = common_letters(x[0], x[1])
        if len(common) == len(x[0]) - 1:
            return common

def main():
    puzzle_input = adventofcode.read_input(2)
    adventofcode.answer(1, 5434, rudimentary_checksum(puzzle_input))
    adventofcode.answer(2, 'agimdjvlhedpsyoqfzuknpjwt', common_letters_in_box_ids(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
