#!/usr/bin/env python

def is_valid_one(line):
    """
    >>> is_valid_one("aa bb cc dd ee")
    True
    >>> is_valid_one("aa bb cc dd aa")
    False
    >>> is_valid_one("aa bb cc dd aaa")
    True
    """
    words = line.split()
    return max([words.count(x) for x in words]) == 1

def count_valid_passphrases(lines, is_valid):
    checks = [is_valid(x) for x in lines]
    return checks.count(True)

def sort_word(word):
    """
    >>> sort_word("asdfasdf")
    'aaddffss'
    """
    return "".join(sorted([x for x in word]))

def is_valid_two(line):
    """
    >>> is_valid_two("abcde fghij")
    True
    >>> is_valid_two("abcde xyz ecdab")
    False
    >>> is_valid_two("a ab abc abd abf abj")
    True
    >>> is_valid_two("iiii oiii ooii oooi oooo")
    True
    >>> is_valid_two("oiii ioii iioi iiio")
    False
    """
    words = line.split()
    words = [sort_word(x) for x in words]
    return max([words.count(x) for x in words]) == 1

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day04_input.txt")]
    print "Part 1 Answer", count_valid_passphrases(puzzle_input, is_valid_one)
    print "Part 2 Answer", count_valid_passphrases(puzzle_input, is_valid_two)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
