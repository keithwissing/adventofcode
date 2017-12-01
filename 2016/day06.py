#!/usr/bin/env python

import string

def error_correct(puzzle_input, rev):
    """
    >>> error_correct(["eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa", "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"], True)
    'easter'
    >>> error_correct(["eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa", "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"], False)
    'advent'
    """
    message = ''
    for pos in range(0, len(puzzle_input[0])):
        column = ''.join([x[pos] for x in puzzle_input])
        counts = [column.count(x) for x in string.lowercase]
        pairs = [(i,j) for i,j in zip(counts, string.lowercase)]
        pairs.sort(reverse=rev)
        pairs = [(i,j) for i,j in pairs if i > 0]
        message = message + pairs[0][1]
    return message

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day06_input.txt")]
    print "Part 1 Answer", error_correct(puzzle_input, True)
    print "Part 2 Answer", error_correct(puzzle_input, False)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

