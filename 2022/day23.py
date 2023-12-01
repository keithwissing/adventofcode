#!/usr/bin/env python3

import adventofcode

t1 = [
    '....#..',
    '..###.#',
    '#...#.#',
    '.#...##',
    '#.###..',
    '##.#.##',
    '.#..#..',
]

t2 = [
    '.....',
    '..##.',
    '..#..',
    '.....',
    '..##.',
    '.....',
]

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

class Map:
    def __init__(self, lines):
        self.data = set()
        for y, line in enumerate(lines):
            self.data.update({(x, y) for x, v in enumerate(line) if v != '.'})

    def check_size(self):
        min_x = min(x for x, y in self.data)
        max_x = max(x for x, y in self.data)
        min_y = min(y for x, y in self.data)
        max_y = max(y for x, y in self.data)
        return min_x, max_x, min_y, max_y

    def blanks(self):
        min_x, max_x, min_y, max_y = self.check_size()
        return (max_x - min_x + 1) * (max_y - min_y + 1) - len(self.data)

    def print(self):
        min_x, max_x, min_y, max_y = self.check_size()
        print(min_x, max_x, min_y, max_y)
        for y in range(min_y, max_y + 1):
            print(''.join('#' if (x, y) in self.data else '.' for x in range(min_x, max_x + 1)))
        print()

def adjacent(pos):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy != 0 or dx != 0:
                yield add(pos, (dx, dy))

def in_dir(pos, direction):
    if direction == 'N':
        for x in range(-1, 2):
            yield add(pos, (x, -1))
    if direction == 'S':
        for x in range(-1, 2):
            yield add(pos, (x, 1))
    if direction == 'W':
        for y in range(-1, 2):
            yield add(pos, (-1, y))
    if direction == 'E':
        for y in range(-1, 2):
            yield add(pos, (1, y))

def move_direction(pos, direction):
    delta = {'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}[direction]
    return add(pos, delta)

def nobody_around(grove, pos):
    return not any(t in grove.data for t in adjacent(pos))

def nobody_there(grove, pos, direction):
    return not any(t in grove.data for t in in_dir(pos, direction))

def proposals(grove, directions):
    props = {}
    for elf in grove.data:
        if nobody_around(grove, elf):
            props[elf] = elf
        else:
            for d in directions:
                if nobody_there(grove, elf, d):
                    props[elf] = move_direction(elf, d)
                    break
            if elf not in props:
                props[elf] = elf
    return props

def move(props):
    grove = Map([])
    for k, v in props.items():
        count = sum(1 for t in props.values() if t == v)
        grove.data.add(v if count == 1 else k)
    return grove

def part1(lines):
    """
    >>> part1(t1)
    110
    """
    grove = Map(lines)
    directions = ['N', 'S', 'W', 'E']
    for _ in range(10):
        props = proposals(grove, directions)
        grove = move(props)
        directions = directions[1:] + directions[:1]
    return grove.blanks()

def part2(lines):
    """
    >>> part2(t1)
    20
    """
    grove = Map(lines)
    directions = ['N', 'S', 'W', 'E']
    for r in range(2000):
        lg = grove
        props = proposals(grove, directions)
        grove = move(props)
        directions = directions[1:] + directions[:1]
        if lg.data == grove.data:
            return r + 1

def main():
    puzzle_input = adventofcode.read_input(23)
    adventofcode.answer(1, 3762, part1(puzzle_input))
    adventofcode.answer(2, 997, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
