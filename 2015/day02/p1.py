#!/usr/bin/env python

def paper(x, y, z):
    """
    >>> paper(2,3,4)
    58
    >>> paper(1,1,10)
    43
    """
    s1 = x*y
    s2 = x*z
    s3 = y*z
    o = min(s1, s2, s3)
    return 2*(s1+s2+s3)+o

def ribbon(x, y, z):
    """
    >>> ribbon(2,3,4)
    34
    >>> ribbon(1,1,10)
    14
    """
    l1 = 2*(x+y+z-max(x, y, z))
    l2 = x*y*z
    return l1+l2

def one_line(line, func):
    (x, y, z) = line.split('x')
    x = int(x)
    y = int(y)
    z = int(z)
    return func(x, y, z)

def calculate(puzzle_input, func):
    total = 0
    for line in puzzle_input:
        total = total + one_line(line, func)
    print total

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    calculate(puzzle_input, paper)
    calculate(puzzle_input, ribbon)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

