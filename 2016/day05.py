#!/usr/bin/env python

import hashlib
#m = hashlib.md5()
#m.update("000005fab4534d05api_key9a0554259914a86fb9e7eb014e4e5d52permswrite")
#print m.hexdigest()

def calculate_passcode(puzzle_input):
    """
    #>>> calculate_passcode('abc')
    #'18f47a30'
    """
    index = 0
    passcode = ''
    while len(passcode) < 8:
        h = hashlib.md5(puzzle_input+str(index)).hexdigest()
        if h[:5] == "00000":
            passcode = passcode + h[5]
            print passcode
        index = index + 1
    return passcode

def second_passcode(puzzle_input):
    index = 0
    passcode = "________"
    while passcode.count('_') > 0:
        h = hashlib.md5(puzzle_input+str(index)).hexdigest()
        if h[:5] == "00000":
            pos = int(h[5], 16)
            if pos < len(passcode) and passcode[pos] == '_':
                blah = list(passcode)
                blah[pos] = h[6]
                passcode = ''.join(blah)
            print passcode
        index = index + 1
    return passcode

def main():
    puzzle_input = "ffykfhsq"
    print "Part 1 Answer", calculate_passcode(puzzle_input)
    print "Part 2 Answer", second_passcode(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

