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
    up = input.count('(')
    down = input.count(')')
    print up - down

def basement(input):
    """
    >>> basement(")")
    1
    >>> basement("()())")
    5
    """
    floor = 0
    pos = 0
    while pos < len(input):
        if input[pos] == '(' : floor = floor + 1
        if input[pos] == ')' : floor = floor - 1
        if floor == -1:
            print pos+1
            break
        pos = pos + 1

def main():
    input = open("input.txt").read()
    find_floor(input)
    basement(input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

