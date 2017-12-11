#!/usr/bin/env python

def part1(puzzle_input):
    """
    >>> part1("ne,ne,ne")
    3
    >>> part1("ne,ne,sw,sw")
    0
    >>> part1("ne,ne,s,s")
    2
    >>> part1("se,sw,se,sw,sw")
    3
    """
    data = puzzle_input.split(",")
    return final_hex_distance(data)

def final_hex_distance(data):
    """
    I ended up referring to https://www.redblobgames.com/grids/hexagons/ to come up with this.
    """
    north = data.count("n") - data.count("s")
    northeast = data.count("ne") - data.count("sw")
    southeast = data.count("se") - data.count("nw")
    q = 0 + northeast + southeast
    r = -north - northeast
    return (abs(q) + abs(q + r) + abs(r)) / 2

def part2(puzzle_input):
    """
    >>> part2("ne,ne,sw,sw")
    2
    """
    data = puzzle_input.split(",")
    far = 0
    for x in range(len(data)):
        step = data[0:x+1]
        far = max(far, final_hex_distance(step))
    return far

def main():
    puzzle_input = open("day11_input.txt").read().rstrip()
    print "Part 1 Answer", part1(puzzle_input)
    print "Part 2 Answer", part2(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
