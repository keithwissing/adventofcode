#!/usr/bin/env python

import adventofcode

def part1(puzzle_input):
    """
    >>> part1([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
    138
    """
    (c, m, _) = parse_tree(puzzle_input)
    tree = (c, m)
    return sum_of_meta(tree)

def parse_tree(puzzle):
    nchild = puzzle[0]
    nmeta = puzzle[1]
    children = []
    if nchild == 0:
        return (None, puzzle[2:2+nmeta], nmeta + 2)
    else:
        pos = 2
        for _ in range(nchild):
            (c, m, l) = parse_tree(puzzle[pos:])
            children.append((c, m))
            pos += l
        return (children, puzzle[pos:pos+nmeta], pos+nmeta)

def sum_of_meta(tree):
    (children, meta) = tree
    if children is None:
        return sum(meta)
    return sum([sum_of_meta(x) for x in children]) + sum(meta)

def part2(puzzle_input):
    """
    >>> part2([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
    66
    """
    (c, m, _) = parse_tree(puzzle_input)
    tree = (c, m)
    return value_of_node(tree)

def value_of_node(node):
    (children, meta) = node
    if children is None:
        return sum(meta)
    else:
        total = 0
        for x in meta:
            if x > 0 and x-1 < len(children):
                total += value_of_node(children[x-1])
        return total

def parse_line(line):
    return line

def main():
    puzzle_input = adventofcode.read_input(8)
    puzzle_input = [int(x) for x in puzzle_input.split()]
    adventofcode.answer(1, 37905, part1(puzzle_input))
    adventofcode.answer(2, 33891, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
