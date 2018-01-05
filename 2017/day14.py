#!/usr/bin/env python

import adventofcode
import day10

def generate_hex_grid(puzzle_input):
    return [day10.part2("%s-%d" % (puzzle_input, row)) for row in range(128)]

def hextobin(hexstring):
    """
    >>> hextobin("2")
    '0010'
    """
    return "".join(["{0:04b}".format(int(x, 16)) for x in hexstring])

def generate_bin_grid(puzzle_input):
    return [hextobin(x) for x in generate_hex_grid(puzzle_input)]

def part1(bingrid):
    return sum(row.count("1") for row in bingrid)

def remove_region(used, col, row):
    """
    >>> remove_region({(1,1):1, (1,2):1}, 1, 1)
    """
    todo = [(col, row)]
    while todo:
        pos = todo.pop()
        (col, row) = pos
        if pos in used:
            del used[pos]
            for check in [(col-1, row), (col+1, row), (col, row-1), (col, row+1)]:
                if used.get(check, 0) == 1:
                    todo.append(check)

def part2(bingrid):
    return count_regions_in_bingrid(bingrid)

def count_regions_in_bingrid(bingrid):
    """
    >>> count_regions_in_bingrid(['1100', '0011'])
    2
    """
    used = {(x, y): 1
            for x in range(len(bingrid[0]))
            for y in range(len(bingrid))
            if bingrid[y][x] == '1'}
    regions = 0
    while used:
        regions += 1
        pos = used.keys()[0]
        (col, row) = pos
        remove_region(used, col, row)
    return regions

def main():
    puzzle_input = adventofcode.read_input(14)
    bingrid = generate_bin_grid(puzzle_input)
    adventofcode.answer(1, 8226, part1(bingrid))
    adventofcode.answer(2, 1128, part2(bingrid))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
