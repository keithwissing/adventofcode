#!/usr/bin/env python

def find_floor(input):
    """
    >>> find_floor("(())")
    0
    >>> find_floor("()()")
    0
    >>> find_floor("(((")
    3
    >>> find_floor("(()(()(")
    3
    >>> find_floor("))(((((")
    3
    >>> find_floor("())")
    -1
    >>> find_floor("))(")
    -1
    >>> find_floor(")))")
    -3
    >>> find_floor(")())())")
    -3
    """
    pass

def basement(input):
    """
    >>> basement(")")
    1
    >>> basement("()())")
    5
    """
    pass

def main():
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

