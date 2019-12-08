#!/usr/bin/env python3

from collections import Counter
import adventofcode

def part1(image, width, height):
    layers = [image[p:p+width*height] for p in range(0, len(image), width*height)]
    data = {c[0]: c[1]*c[2] for c in [Counter(l) for l in layers]}
    return data[min(data.keys())]

def part2(image, width, height):
    layers = [image[p:p+width*height] for p in range(0, len(image), width*height)]
    pixels = ['#' if next(x for x in l if x != 2) == 1 else ' ' for l in zip(*layers)]
    rows = [''.join(pixels[p:p+width]) for p in range(0, width*height, width)]
    print('\n'.join(rows))
    return 'GJYEA' # result of visual inspetion of the output

def main():
    puzzle_input = adventofcode.read_input(8)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 1742, part1(puzzle_input, 25, 6))
    adventofcode.answer(2, 'GJYEA', part2(puzzle_input, 25, 6))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
