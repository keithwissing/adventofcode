#!/usr/bin/env python

def part1(steps):
    """
    >>> part1(3)
    638
    """
    buffer = [0]
    pos = 0
    for next in xrange(1, 2018):
        pos = (pos + steps) % len(buffer)
        buffer = buffer[:pos+1] + [next] + buffer[pos+1:]
        pos += 1
    return buffer[(pos+1)%len(buffer)]

def part2(steps):
    return part2var(steps, 50000000)

def part2var(steps, iterations):
    """
    >>> part2var(3, 1)
    1
    >>> part2var(3, 8)
    5
    >>> part2var(3, 9)
    9
    """
    afterz = 0
    pos = 0
    blen = 1
    for next in xrange(1, iterations+1):
        pos = (pos + steps) % blen
        if pos == 0:
            afterz = next
        blen += 1
        pos += 1
    return afterz

def main():
    puzzle_input = open("day17_input.txt").read().rstrip()
    steps = int(puzzle_input)
    a1 = part1(steps)
    print "Part 1 Answer", a1
    assert a1 == 1547
    a2 = part2(steps)
    print "Part 2 Answer", a2
    assert a2 == 31154878

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
