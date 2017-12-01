#!/usr/bin/env python

def is_possible(sides):
    return sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]

def count_possible_triangles(puzzle_input):
    """
    >>> count_possible_triangles(["   5  10  25"])
    0
    """
    count = 0
    for row in puzzle_input:
        sides = [int(x) for x in row.split()]
        if is_possible(sides):
            count = count + 1
    return count

def count_by_columns(puzzle_input):
    count = 0
    intInput = [[int(x) for x in row.split()] for row in puzzle_input]
    for col in range(0, 3):
        for row in range(0, len(intInput), 3):
            sides = [intInput[row][col], intInput[row+1][col], intInput[row+2][col]]
            if is_possible(sides):
                count = count + 1
    return count

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day03_input.txt")]
    print "Part 1 Answer", count_possible_triangles(puzzle_input)
    print "Part 2 Answer", count_by_columns(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

