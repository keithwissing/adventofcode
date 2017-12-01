#!/usr/bin/env python

import re

def mem_len(line):
    step = line[1:len(line)-1]
    step = step.replace("\\\\", "\\")
    step = step.replace("\\\"", "\"")
    step = re.sub(r"\\x[0-9a-f][0-9a-f]", "_", step)
    #print len(line),len(step),line,step
    return len(step)

def string_size_difference(lines):
    """
    >>> string_size_difference( [\
        '""',\
        '"abc"',\
        '"aaa\\\\"aaa"',\
        '"\\\\x27"' ] )
    12
    """
    tlen = 0
    tmlen = 0
    for line in lines:
        tlen = tlen + len(line)
        tmlen = tmlen + mem_len(line)
    return tlen - tmlen

def code_encode(line):
    step = line
    step = step.replace("\\", "\\\\")
    step = step.replace("\"", "\\\"")
    step = '"'+step+'"'
    #print len(line),len(step),line,step
    return len(step)

def part2(lines):
    """
    >>> part2( [\
        '""',\
        '"abc"',\
        '"aaa\\\\"aaa"',\
        '"\\\\x27"' ] )
    19
    """
    tlen = 0
    tmlen = 0
    for line in lines:
        tlen = tlen + len(line)
        tmlen = tmlen + code_encode(line)
    return tmlen - tlen

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    print string_size_difference(puzzle_input)
    print part2(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

