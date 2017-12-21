#!/usr/bin/env python

import re

def total_score(line):
    """
    >>> total_score("{}")
    1
    >>> total_score("{{{}}}")
    6
    >>> total_score("{{},{}}")
    5
    >>> total_score("{{{},{},{{}}}}")
    16
    >>> total_score("{<a>,<a>,<a>,<a>}")
    1
    >>> total_score("{{<ab>},{<ab>},{<ab>},{<ab>}}")
    9
    >>> total_score("{{<!!>},{<!!>},{<!!>},{<!!>}}")
    9
    >>> total_score("{{<a!>},{<a!>},{<a!>},{<ab>}}")
    3
    """
    cleaner = remove_garbage(remove_cancels(line))
    clean = cleaner.replace(",", "")
    total = 0
    deep = 0
    for x in clean:
        if x == "{":
            deep += 1
            total += deep
        else:
            deep -= 1
    return total

def count_garbage(line):
    """
    >>> count_garbage("<>")
    0
    >>> count_garbage("<random characters>")
    17
    >>> count_garbage("<<<<>")
    3
    """
    non = remove_cancels(line)
    cleaner = remove_garbage2(non)
    return len(non) - len(cleaner)

def remove_cancels(line):
    """
    >>> remove_cancels("ab!cde!fgh")
    'abdegh'
    """
    return re.sub("!.", "", line)

def remove_garbage(line):
    return re.sub("<.*?>", "", line)

def remove_garbage2(line):
    return re.sub("<.*?>", "<>", line)

def main():
    puzzle_input = open("day09_input.txt").read().rstrip()
    print "Part 1 Answer", total_score(puzzle_input)
    print "Part 2 Answer", count_garbage(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
