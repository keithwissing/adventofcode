#!/usr/bin/env python

def calibrate(reps, start):
    """
    >>> len(calibrate([ 'H => HO', 'H => OH', 'O => HH' ], 'HOH'))
    4
    """
    out = set()
    for rep in reps:
        f, t = rep.split(' => ')
        pos = 0
        while pos >= 0:
            pos = start.find(f, pos)
            if pos >= 0:
                out.add(''.join([start[0:pos], t, start[pos+len(f):]]))
                pos += 1
    return out

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    start = puzzle_input.pop()
    print start
    blank = puzzle_input.pop()
    print 'blank', blank
    print len(calibrate(puzzle_input, start))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

