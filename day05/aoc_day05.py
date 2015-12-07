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
    pass

def has_double_letter(line):
    """
    >>> has_double_letter("xx")
    True
    >>> has_double_letter("abcdde")
    True
    >>> has_double_letter("aabbccdd")
    True
    """
    pass

def has_bad_string(line):
    """
    >>> has_bad_string("abcd")
    True
    >>> has_bad_string("aaccppxx")
    False
    """
    pass

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
    pass

def has_double_pair(line):
    """
    >>> has_double_pair("xyxy")
    True
    >>> has_double_pair("aabcdefgaa")
    True
    >>> has_double_pair("aaa")
    False
    """
    pass

def has_repeat_with_one(line):
    """
    >>> has_repeat_with_one("xyx")
    True
    >>> has_repeat_with_one("abcdefeghi")
    True
    >>> has_repeat_with_one("aaa")
    True
    """
    pass

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
    pass

def main():
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

