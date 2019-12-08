#!/usr/bin/env python3

from collections import Counter
import adventofcode

def decode(image, width, height):
    layersize = width * height
    pos = 0
    cz = 500000
    while pos < len(image):
        layer = image[pos:pos+layersize]
        c = Counter(layer)
        zeros = c[0]
        if zeros < cz:
            cz = zeros
            ret = c[1]*c[2]
        pos += layersize
    return ret

def part1(image):
    return decode(image, 25, 6)

def part2(image, width, height):
    layersize = width * height
    layers = []
    pos = 0
    while pos < len(image):
        layers.append(image[pos:pos+layersize])
        pos += layersize
    for y in range(height):
        for x in range(width):
            for l in range(len(layers)):
                p = layers[l][y*width+x]
                if p != 2:
                    print('#' if p == 1 else ' ', end = '')
                    break
        print()
    return 'GJYEA' # result of visual inspetion of the output

def main():
    puzzle_input = adventofcode.read_input(8)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 1742, part1(puzzle_input))
    adventofcode.answer(2, 'GJYEA', part2(puzzle_input, 25, 6))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
