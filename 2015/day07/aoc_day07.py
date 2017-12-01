#!/usr/bin/env python

def run_and_print_all(lines):
    """
    >>> run_and_print_all( [\
        "123 -> x",\
        "456 -> y",\
        "x AND y -> d",\
        "x OR y -> e",\
        "x LSHIFT 2 -> f",\
        "y RSHIFT 2 -> g",\
        "NOT x -> h",\
        "NOT y -> i" ] )
    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456
    """
    pass

def main():
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

