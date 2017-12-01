#!/usr/bin/env python

import hashlib

def hash_the_string(puzzle_input):
    m = hashlib.md5()
    m.update(puzzle_input)
    return m.hexdigest()

def zeros(puzzle_input):
    h = hash_the_string(puzzle_input)
    return len(h) - len(h.lstrip('0'))

def mine(key, nz, hint=1):
    """
    >>> mine("abcdef",5,600000)
    609043
    """
    count = hint
    while True:
        test = key+str(count)
        if zeros(test) >= nz:
            break
        count = count + 1
    print count

def main():
    mine("yzbqklnj", 5)
    mine("yzbqklnj", 6)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

