#!/usr/bin/env python3
from collections import defaultdict
from itertools import product

import adventofcode

t1 = [
    '########',
    '#..O.O.#',
    '##@.O..#',
    '#...O..#',
    '#.#.O..#',
    '#...O..#',
    '#......#',
    '########',
    '',
    '<^^>>>vv<v>>v<<',
]

t2 = [
    '##########',
    '#..O..O.O#',
    '#......O.#',
    '#.OO..O.O#',
    '#..O@..O.#',
    '#O#..O...#',
    '#O..O..O.#',
    '#.OO.O.OO#',
    '#....O...#',
    '##########',
    '',
    '<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^',
    'vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v',
    '><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<',
    '<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^',
    '^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><',
    '^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^',
    '>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^',
    '<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>',
    '^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>',
    'v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^',
]

t3 = [
    '#######',
    '#...#.#',
    '#.....#',
    '#..OO@#',
    '#..O..#',
    '#.....#',
    '#######',
    '',
    '<vv<<^^<<^^',
]

def parse(lines):
    blank = lines.index('')
    grid = defaultdict(lambda: '#', {(x, y): v for y, row in enumerate(lines[:blank]) for x, v in enumerate(row)})
    moves = ''.join(lines[blank:])
    return grid, moves

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def display(grid):
    mx = max(x for x, y in grid.keys())
    my = max(y for x, y in grid.keys())
    for y in range(my + 1):
        print(''.join(grid[(x, y)] for x in range(mx + 1)))

def run(grid, moves):
    deltas = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    robot = next(k for k, v in grid.items() if v == '@')
    for m in moves:
        d = deltas[m]
        pos = add(robot, d)
        while (n := grid[pos]) != '#':
            if n == '.':
                grid[pos] = 'O'
                grid[robot] = '.'
                robot = add(robot, d)
                grid[robot] = '@'
                break
            pos = add(pos, d)
    return grid

def score(grid):
    mx = max(x for x, y in grid.keys())
    my = max(y for x, y in grid.keys())
    total = 0
    for x, y in product(range(mx), range(my)):
        if grid[(x, y)] in 'O[':
            total += 100 * y + x
    return total

def part1(lines):
    """
    >>> part1(t1)
    2028

    >>> part1(t2)
    10092
    """
    grid, moves = parse(lines)
    grid = run(grid, moves)
    return score(grid)

def parse2(lines):
    blank = lines.index('')
    top, bottom = lines[:blank], lines[blank:]

    t = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
    top = [''.join(t[c] for c in line) for line in top]
    grid = defaultdict(lambda: '#', {(x, y): v for y, row in enumerate(top) for x, v in enumerate(row)})

    moves = ''.join(bottom)
    return grid, moves

def run2(grid, moves):
    deltas = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    robot = next(k for k, v in grid.items() if v == '@')
    for i, m in enumerate(moves):
        d = deltas[m]
        pos = {robot}
        pushed = {robot}
        while True:
            np = {add(v, d) for v in pos}
            nv = set(grid[v] for v in np)
            if '#' in nv:
                break
            if nv == set('.'):
                f = {v: grid[v] for v in pushed}
                for v in pushed:
                    grid[v] = '.'
                for v in pushed:
                    grid[add(v, d)] = f[v]
                robot = add(robot, d)
                break
            np = {v for v in np if grid[v] != '.'}
            if d[1] != 0:
                for x, y in list(np):
                    if grid[(x, y)] == '[':
                        np.add((x + 1, y))
                    if grid[(x, y)] == ']':
                        np.add((x - 1, y))
            pushed.update(np)
            pos = np

    return grid

def part2(lines):
    """
    >>> part2(t3)
    618

    >>> part2(t2)
    9021
    """
    grid, moves = parse2(lines)
    grid = run2(grid, moves)
    return score(grid)

def main():
    puzzle_input = adventofcode.read_input(15)
    adventofcode.answer(1, 1509074, part1(puzzle_input))
    adventofcode.answer(2, 1521453, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
