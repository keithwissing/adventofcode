#!/usr/bin/env python3
from heapq import heapify, nlargest

import adventofcode

t1 = [
    '162,817,812',
    '57,618,57',
    '906,360,560',
    '592,479,940',
    '352,342,300',
    '466,668,158',
    '542,29,236',
    '431,825,988',
    '739,650,466',
    '52,470,668',
    '216,146,977',
    '819,987,18',
    '117,168,530',
    '805,96,715',
    '346,949,466',
    '970,615,88',
    '941,993,340',
    '862,61,35',
    '984,92,344',
    '425,690,689',
]

def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

def distances(boxes):
    ds = []
    for ai, a in enumerate(boxes):
        for b in boxes[ai + 1:]:
            d = distance(a, b)
            ds.append((d, a, b))
    return sorted(ds)

def make_connections(lines, connections):
    boxes = tuple(tuple(int(x) for x in l.split(',')) for l in lines)
    ds = distances(boxes)
    circuits = [[a] for a in boxes]

    def cn(a):
        for i, c in enumerate(circuits):
            if a in c:
                return i
        return -1

    count = 0
    while (connections == -1 and len(circuits) > 1) or count < connections:
        _, a, b = ds.pop(0)
        ca = cn(a)
        cb = cn(b)
        if ca != cb:
            circuits[ca].extend(circuits[cb])
            del circuits[cb]
        count += 1
    return circuits, a, b

def part1(lines, connections):
    """
    >>> part1(t1, 10)
    40
    """
    circuits, _, _ = make_connections(lines, connections)
    q = list(len(c) for c in circuits)
    heapify(q)
    a, b, c = nlargest(3, q)
    return a * b * c

def part2(lines):
    """
    >>> part2(t1)
    25272
    """
    _, a, b = make_connections(lines, -1)
    return a[0] * b[0]

def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 81536, part1(puzzle_input, 1000))
    adventofcode.answer(2, 7017750530, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
