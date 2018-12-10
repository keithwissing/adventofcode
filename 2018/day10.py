#!/usr/bin/env python

import adventofcode

def part1(puzzle_input):
    lsize = csize = field_size(puzzle_input)
    count = 0
    while csize[0] <= lsize[0]:
        lsize = csize
        puzzle_input = iterate(puzzle_input)
        csize = field_size(puzzle_input)
        count += 1
    puzzle_input = backwards(puzzle_input)
    show_field(puzzle_input)
    print 'Wait in seconds:', count - 1

def field_size(points):
    xmax = max([x[0] for x in points])
    ymax = max([x[1] for x in points])
    xmin = min([x[0] for x in points])
    ymin = min([x[1] for x in points])
    return (xmax-xmin, ymax-ymin)

def iterate(puzzle_input):
    return [(x[0]+x[2], x[1]+x[3], x[2], x[3]) for x in puzzle_input]

def backwards(puzzle_input):
    return [(x[0]-x[2], x[1]-x[3], x[2], x[3]) for x in puzzle_input]

def show_field(points):
    xmax = max([x[0] for x in points])
    ymax = max([x[1] for x in points])
    xmin = min([x[0] for x in points])
    ymin = min([x[1] for x in points])
    grid = [[' ' for x in range(xmax-xmin+1)] for y in range(ymax-ymin+1)]
    for point in points:
        grid[point[1]-ymin][point[0]-xmin] = '#'
    for line in grid:
        print ''.join(line)

def parse_line(line):
    parts = line.replace('<', ' ').replace('>', ' ').replace(',', ' ').split()
    return map(int, parts[1:3] + parts[4:])

def main():
    puzzle_input = adventofcode.read_input(10)
    puzzle_input = map(parse_line, puzzle_input)
    part1(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
