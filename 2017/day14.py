#!/usr/bin/env python

import day10

def generate_hex_grid(puzzle_input):
    """
    >> generate_hex_grid("flqrgnkx")
    """
    grid = []
    for row in range(128):
        grid.append(day10.part2("%s-%d" % (puzzle_input, row)))
    return grid

def hextobin(hexstring):
    """
    This is disgusting, but it was fast to write
    >>> hextobin("2")
    '0010'
    """
    return "".join(["{0:04b}".format(int(x, 16)) for x in hexstring])

def generate_bin_grid(puzzle_input):
    hexgrid = generate_hex_grid(puzzle_input)
    return [hextobin(x) for x in hexgrid]

def part1(puzzle_input):
    hexgrid = generate_hex_grid(puzzle_input)
    used = 0
    for row in hexgrid:
        bin = hextobin(row)
        used += bin.count("1")
    return used

def remove_region(used, row, col):
    """
    >>> remove_region({(1,1):1, (1,2):1}, 1, 1)
    """
    todo = [(col, row)]
    while len(todo) > 0:
        pos = todo.pop()
        (col, row) = pos
        if pos in used:
            del used[pos]
            for check in [(col-1, row), (col+1, row), (col, row-1), (col, row+1)]:
                if used.get(check, 0) == 1:
                    todo.append(check)

def part2(puzzle_input):
    bingrid = generate_bin_grid(puzzle_input)
    return count_regions_in_bingrid(bingrid)

def count_regions_in_bingrid(bingrid):
    """
    >>> count_regions_in_bingrid(['1100', '0011'])
    2
    """
    used = {(x, y): 1 for x in range(len(bingrid[0])) for y in range(len(bingrid)) if bingrid[y][x] == '1'}
    regions = 0
    while len(used) > 0:
        regions += 1
        pos = used.keys()[0]
        (col, row) = pos
        remove_region(used, row, col)
    return regions

def main():
    puzzle_input = open("day14_input.txt").read().rstrip()
    print "Part 1 Answer", part1(puzzle_input)
    print "Part 2 Answer", part2(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
