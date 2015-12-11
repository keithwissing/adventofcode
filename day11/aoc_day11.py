#!/usr/bin/env python

def increment(password):
    """
    >>> increment("xx")
    'xy'
    >>> increment("xy")
    'xz'
    >>> increment("xz")
    'ya'
    >>> increment("ya")
    'yb'
    """
    pass

def has_increasing_straight(password):
    """
    >>> has_increasing_straight("abc")
    True
    >>> has_increasing_straight("xyz")
    True
    >>> has_increasing_straight("abd")
    False
    """
    pass

def has_no_bad_letters(password):
    """
    >>> has_no_bad_letters("abcdefg")
    True
    >>> has_no_bad_letters("nope")
    False
    """
    pass

def has_two_pair(password):
    """
    >>> has_two_pair("aabcd")
    False
    >>> has_two_pair("aabcdd")
    True
    >>> has_two_pair("aaabcd")
    False
    """
    pass

def is_good_password(password):
    """
    >>> is_good_password("hijklmmn")
    False
    >>> is_good_password("abbceffg")
    False
    >>> is_good_password("abbcegjk")
    False
    """
    pass

def find_next_password(password):
    """
    >>> find_next_password("abcdefgh")
    'abcdffaa'
    >>> find_next_password("ghijklmn")
    'ghjaabcc'
    """
    pass

def main():
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

