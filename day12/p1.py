#!/usr/bin/env python

import json
import re
import timeit

def sum_of_all_numbers(string):
    """
    >>> sum_of_all_numbers('[1,2,3]')
    6
    >>> sum_of_all_numbers('{"a":2,"b":4}')
    6
    >>> sum_of_all_numbers('[[[3]]]')
    3
    >>> sum_of_all_numbers('{"a":{"b":4},"c":-1}')
    3
    >>> sum_of_all_numbers('{"a":[-1,1]}')
    0
    >>> sum_of_all_numbers('[-1,{"a":1}]')
    0
    >>> sum_of_all_numbers('[]')
    0
    >>> sum_of_all_numbers('{}')
    0
    """
    return sum([int(x) if x else 0 for x in re.split(r'[^-\d]+', string)])

def sum_object(obj):
    if type(obj) is int:
        return obj
    if type(obj) is list:
        return sum(sum_object(x) for x in obj)
    if type(obj) is dict:
        if 'red' in obj.values():
            return 0
        return sum(sum_object(x) for x in obj.values())
    if type(obj) is str:
        return 0
    if type(obj) is unicode:
        return 0
    print type(obj)
    return 0

def sum_without_red(string):
    """
    >>> sum_without_red('[1,2,3]')
    6
    >>> sum_without_red('[1,{"c":"red","b":2},3]')
    4
    >>> sum_without_red('{"d":"red","e":[1,2,3,4],"f":5}')
    0
    >>> sum_without_red('[1,"red",5]')
    6
    """
    de = json.loads(string)
    return sum_object(de)

def main2():
    puzzle_input = open("input.txt").read()
    print sum_of_all_numbers(puzzle_input)
    print sum_without_red(puzzle_input)

def main():
    print 'Hello'
    time = timeit.timeit(main2, number=1)
    print "Elapsed time", time

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

