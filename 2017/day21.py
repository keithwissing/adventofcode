#!/usr/bin/env python

import math
import adventofcode

start_image = [".#.", "..#", "###"]

def parse_line(line):
    """
    >>> parse_line("../.. => .../.../###")
    [['..', '..'], ['...', '...', '###']]
    """
    side = line.split(" => ")
    return [a.split("/") for a in side]

def remove_collitions(lines):
    positions = [p.pos for p in lines]
    ponts = set(positions)
    for point in ponts:
        if positions.count(point) > 1:
            lines = [x for x in lines if x.pos != point]
    return lines

def break_into_subimages(image):
    subimages = []
    subsize = 2 if len(image[0]) % 2 == 0 else 3
    for row in range(0, len(image), subsize):
        for col in range(0, len(image), subsize):
            subimage = [[image[srow][scol] for scol in range(col, col+subsize)] for srow in range(row, row+subsize)]
            subimages.append(subimage)
    return subimages

def rebuild_image(subimages):
    size = int(math.sqrt(len(subimages)))
    image = []
    for blah in range(0, len(subimages), size):
        for blip in range(0, len(subimages[0])):
            row = [si[blip] for si in subimages[blah:blah+size]]
            flat_list = [item for sublist in row for item in sublist]
            image.append(flat_list)
    return image

def rotate(subimage):
    return [[x for x in row] for row in zip(*subimage[::-1])]

def flip(subimage):
    return subimage[::-1]

def subimage_matches(rule, subimage):
    if len(rule) != len(subimage):
        return False
    erule = [[char for char in row] for row in rule]
    if erule == subimage:
        return True
    for _ in range(3):
        erule = rotate(erule)
        if erule == subimage:
            return True
    erule = flip(erule)
    if erule == subimage:
        return True
    for _ in range(3):
        erule = rotate(erule)
        if erule == subimage:
            return True
    return False

def subimage_replacement(subimage, rules):
    for rule in rules:
        if subimage_matches(rule[0], subimage):
            replacement = rule[1]
    return replacement

def iterate(image, rules):
    subimages = break_into_subimages(image)
    for idx, subimage in enumerate(subimages):
        subimages[idx] = subimage_replacement(subimage, rules)
    return rebuild_image(subimages)

def count_on(image):
    return sum([1 if x == '#' else 0 for row in image for x in row])

def test1(lines):
    """
    >>> test1(["../.# => ##./#../...", ".#./..#/### => #..#/..../..../#..#"])
    12
    """
    rules = [parse_line(line) for line in lines]
    image = start_image[:]
    after1 = iterate(image, rules)
    after2 = iterate(after1, rules)
    return count_on(after2)

def test2(image):
    """
    >>> test2(start_image)
    [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
    """
    subs = break_into_subimages(image)
    full = rebuild_image(subs)
    return full

def part1(rules):
    image = start_image[:]
    for _ in range(5):
        image = iterate(image, rules)
    return count_on(image)

def part2(rules):
    image = start_image[:]
    for _ in range(18):
        image = iterate(image, rules)
    return count_on(image)

def main():
    lines = adventofcode.read_input(21)
    rules = [parse_line(line) for line in lines]
    adventofcode.answer(1, 125, part1(rules))
    adventofcode.answer(2, 1782917, part2(rules))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
