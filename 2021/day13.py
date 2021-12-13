#!/usr/bin/env python3

import adventofcode

t1 = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5',
]

def parse(lines):
    dots = []
    folds = []
    for line in lines:
        if ',' in line:
            p = [int(x) for x in line.split(',')]
            dots.append((p[0], p[1]))
        if line.startswith('fold'):
            p = line.replace('=', ' ').split()
            folds.append((p[2], int(p[3])))
    return dots, folds

def fold(dots, fold):
    nd = set()
    for dot in dots:
        if fold[0] == 'x':
            if dot[0] >= fold[1]:
                x = dot[0]
                x = fold[1] - (x - fold[1])
                nd.add((x, dot[1]))
            else:
                nd.add(dot)
        if fold[0] == 'y':
            if dot[1] >= fold[1]:
                y = dot[1]
                y = fold[1] - (y - fold[1])
                nd.add((dot[0], y))
            else:
                nd.add(dot)
    return nd

def display(dots, w, h):
    for y in range(h):
        print(''.join(['#' if (x, y) in dots else '.' for x in range(w)]))

def part1(lines):
    """
    >>> part1(t1)
    17
    """
    dots, folds = parse(lines)
    dots = set(dots)
    dots = fold(dots, folds[0])
    return len(dots)

def part2(lines):
    dots, folds = parse(lines)
    dots = set(dots)
    for f in folds:
        dots = fold(dots, f)
    display(dots, 40, 6)
    return 'CJCKBAPB'

def main():
    puzzle_input = adventofcode.read_input(13)
    adventofcode.answer(1, 638, part1(puzzle_input))
    adventofcode.answer(2, 'CJCKBAPB', part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
