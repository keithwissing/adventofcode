#!/usr/bin/env python

def paper(x,y,z):
    s1 = x*y
    s2 = x*z
    s3 = y*z
    o = min(s1,s2,s3)
    return 2*(s1+s2+s3)+o

def print_paper(x,y,z):
    """
    >>> print_paper(2,3,4)
    58
    >>> print_paper(1,1,10)
    43
    """
    print paper(x,y,z)

def ribbon(x,y,z):
    l1 = 2*(x+y+z-max(x,y,z))
    l2 = x*y*z
    return l1+l2

def print_ribbon(x,y,z):
    """
    >>> print_ribbon(2,3,4)
    34
    >>> print_ribbon(1,1,10)
    14
    """
    print ribbon(x,y,z)

def one_line(line, func):
    (x,y,z) = line.split('x')
    x=int(x)
    y=int(y)
    z=int(z)
    return func(x,y,z)

def calculate(input,func):
    total = 0
    for line in input:
        total = total + one_line(line, func)
    print total

def main():
    input = [line.strip() for line in open('input.txt')]
    calculate(input, paper)
    calculate(input, ribbon)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

