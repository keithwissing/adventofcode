#!/usr/bin/env python

import timeit

def look_and_say_super_slow(line):
    """
    >>> look_and_say_super_slow("1")
    '11'
    >>> look_and_say_super_slow("11")
    '21'
    >>> look_and_say_super_slow("21")
    '1211'
    >>> look_and_say_super_slow("1211")
    '111221'
    >>> look_and_say_super_slow("111221")
    '312211'
    """
    # This implementation is laughably slow, but it was fun to see how bad it is.
    out = ""
    while len(line):
        next = line[0]
        clen = len(line)
        line = line.lstrip(next)
        out = out+str(clen-len(line))+next
    return out

def look_and_say(line):
    """
    >>> look_and_say("1")
    '11'
    >>> look_and_say("11")
    '21'
    >>> look_and_say("21")
    '1211'
    >>> look_and_say("1211")
    '111221'
    >>> look_and_say("111221")
    '312211'
    """
    out = []
    p = 0
    while p < len(line):
        n = line[p]
        c = 0
        while p < len(line) and line[p] == n:
            c = c + 1
            p = p + 1
        out.append(str(c))
        out.append(n)
    return "".join(out)

def main2():
    input = "1113122113"
    for count in range(1,51):
        input = look_and_say(input)
        if count in [ 40, 50 ]:
            print count, len(input)

def main():
    time = timeit.timeit(main2, number=1)
    print "Elapsed time", time

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

