#!/usr/bin/env python

def minimum_moves(puzzle_input):
    pass

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day10_input.txt")]
    print "Part 1 Answer", minimum_moves(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

