#!/usr/bin/env python

def supports_tls(ip):
    """
    >>> supports_tls("abba[mnop]qrst")
    True
    >>> supports_tls("abcd[bddb]xyyx")
    False
    >>> supports_tls("aaaa[qwer]tyui")
    False
    >>> supports_tls("ioxxoj[asdfgh]zxcvbn")
    True
    """
    inside = False
    found = False
    for pos in range(0, len(ip)):
        if ip[pos] == '[':
            inside = True
        elif ip[pos] == ']':
            inside = False
        elif pos > 2:
            if ip[pos] == ip[pos-3] and ip[pos-1] == ip[pos-2] and ip[pos] != ip[pos-1]:
                if inside:
                    return False
                else:
                    found = True
    return found

def supports_sls(ip):
    """
    >>> supports_sls("aba[bab]xyz")
    True
    >>> supports_sls("xyx[xyx]xyx")
    False
    >>> supports_sls("aaa[kek]eke")
    True
    >>> supports_sls("zazbz[bzb]cdb")
    True
    """
    inside = False
    inlist = []
    outlist = []
    for pos in range(0, len(ip)):
        if ip[pos] == '[':
            inside = True
        elif ip[pos] == ']':
            inside = False
        elif pos > 1:
            if ip[pos] == ip[pos-2] and ip[pos] != ip[pos-1] and ip[pos-1] != '[' and ip[pos-1] != ']':
                if inside:
                    inlist.append(ip[pos-2:pos+1])
                else:
                    outlist.append(ip[pos-2:pos+1])
    inlist = [c[1]+c[0]+c[1] for c in inlist]
    both = [x for x in inlist if x in outlist]
    return len(both) > 0

def count_supports_tls(puzzle_input):
    return sum([1 for x in puzzle_input if supports_tls(x)])

def count_supports_sls(puzzle_input):
    return sum([1 for x in puzzle_input if supports_sls(x)])

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day07_input.txt")]
    print "Part 1 Answer", count_supports_tls(puzzle_input)
    print "Part 2 Answer", count_supports_sls(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

