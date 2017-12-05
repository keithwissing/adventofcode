#!/usr/bin/env python

def checksum_by_row(puzzle_input):
    """
    >>> checksum_by_row(["5\\t1\\t9\\t5", "7\\t5\\t3", "2\\t4\\t6\\t8"])
    18
    """
    result = 0
    for row in puzzle_input:
        p = [int(x) for x in row.split("\t")]
        result += max(p) - min(p)
    return result

def only_divisible(puzzle_input):
    """
    >>> only_divisible(["5\\t9\\t2\\t8", "9\\t4\\t7\\t3", "3\\t8\\t6\\t5"])
    9
    """
    result = 0
    for row in puzzle_input:
        p = [int(x) for x in row.split("\t")]
        p.sort()
        p.reverse()
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if p[i]/p[j] == float(p[i])/p[j]:
                    result += p[i]/p[j]
    return result

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day02_input.txt")]
    print "Part 1 Answer", checksum_by_row(puzzle_input)
    print "Part 2 Answer", only_divisible(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

