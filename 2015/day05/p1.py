#!/usr/bin/env python

def at_least_3_vowels(line):
    """
    >>> at_least_3_vowels("aei")
    True
    >>> at_least_3_vowels("xazegov")
    True
    >>> at_least_3_vowels("aeiouaeiouaeiou")
    True
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = [line.count(v) for v in vowels]
    return sum(counts) >= 3

def has_double_letter(line):
    """
    >>> has_double_letter("xx")
    True
    >>> has_double_letter("abcdde")
    True
    >>> has_double_letter("aabbccdd")
    True
    """
    last = line[0]
    for pos in range(1, len(line)):
        if last == line[pos]:
            return True
        last = line[pos]
    return False

def has_bad_string(line):
    """
    >>> has_bad_string("abcd")
    True
    >>> has_bad_string("aaccppxx")
    False
    """
    bad = ["ab", "cd", "pq", "xy"]
    counts = [line.count(b) for b in bad]
    return sum(counts) > 0

def is_nice(line):
    """
    >>> is_nice("ugknbfddgicrmopn")
    True
    >>> is_nice("aaa")
    True
    >>> is_nice("jchzalrnumimnmhp")
    False
    >>> is_nice("haegwjzuvuyypxyu")
    False
    >>> is_nice("idvszwmarrgswjxmb")
    False
    """
    nice = at_least_3_vowels(line) and has_double_letter(line) and not has_bad_string(line)
    return nice

def has_double_pair(line):
    """
    >>> has_double_pair("xyxy")
    True
    >>> has_double_pair("aabcdefgaa")
    True
    >>> has_double_pair("aaa")
    False
    """
    for pos in range(0, len(line)-3):
        pair = line[pos:pos+2]
        if line[pos+2:].count(pair) > 0:
            return True
    return False

def has_repeat_with_one(line):
    """
    >>> has_repeat_with_one("xyx")
    True
    >>> has_repeat_with_one("abcdefeghi")
    True
    >>> has_repeat_with_one("aaa")
    True
    """
    for pos in range(0, len(line)-2):
        if line[pos] == line[pos+2]:
            return True
    return False

def is_part2(line):
    """
    >>> is_part2("qjhvhtzxzqqjkmpb")
    True
    >>> is_part2("xxyxx")
    True
    >>> is_part2("uurcxstgmygtbstg")
    False
    >>> is_part2("ieodomkazucvgmuy")
    False
    """
    return has_double_pair(line) and has_repeat_with_one(line)

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    nice = 0
    part2 = 0
    for line in puzzle_input:
        if is_nice(line): nice = nice + 1
        if is_part2(line): part2 = part2 + 1
    print nice
    print part2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

