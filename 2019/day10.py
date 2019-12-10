#!/usr/bin/env python3

from itertools import product, cycle
import math
import adventofcode

testgrid = ['.#..##.###...#######', '##.############..##.', '.#.######.########.#', '.###.#######.####.#.', '#####.##.#.##.###.##', '..#####..#.#########', '####################', '#.####....###.#.#.##', '##.#################', '#####.##.###..####..', '..######..##.#######', '####.##.####...##..#', '.#####..#.######.###', '##...#.##########...', '#.##########.#######', '.####.#.###.###.#.##', '....##.##.###..#####', '.#.#.###########.###', '#.#.#.#####.####.###', '###.##.####.##.#..##']

def test1(grid):
    """
    >>> test1(['.#..#', '.....', '#####', '....#', '...##'])
    (8, (3, 4))
    >>> test1(['......#.#.', '#..#.#....', '..#######.', '.#.#.###..', '.#..#.....', '..#....#.#', '#..#....#.', '.##.#..###', '##...#..#.', '.#....####'])
    (33, (5, 8))
    >>> test1(['#.#...#.#.', '.###....#.', '.#....#...', '##.#.#.#.#', '....#.#.#.', '.##..###.#', '..#...##..', '..##....##', '......#...', '.####.###.'])
    (35, (1, 2))
    >>> test1(['.#..#..###', '####.###.#', '....###.#.', '..###.##.#', '##.##.#.#.', '....###..#', '..#.#..#.#', '#..#.#.###', '.##...##.#', '.....#.#..'])
    (41, (6, 3))
    >>> test1(testgrid)
    (210, (11, 13))
    """
    gs = len(grid)
    mvis = 0
    for x, y in product(range(0, gs), range(0, gs)):
        if at(grid, (x, y)) == '#':
            vis = visible_from(grid, (x, y))
            if vis > mvis:
                mvis = vis
                mpos = (x, y)
    return (mvis, mpos)

# def compute_gcd(a, b):
#     """
#     >>> compute_gcd(4, 6)
#     2
#     """
#     while b:
#         a, b = b, a % b
#     return a

# def total_astroids(grid):
#     return sum(sum(1 for x in row if x == '#') for row in grid)

# sign = lambda x: math.copysign(1, x)

# def path(x1, y1, x2, y2):
#     """
#     # >>> list(path(0, 0, 5, 5))
#     # >>> list(path(5, 5, 0, 0))
#     # >>> list(path(1, 0, 3, 4))
#     """
#     if x1 > x2:
#         x1, x2 = (x2, x1)
#     if y1 > y2:
#         y1, y2 = (y2, y1)
#     dx, dy = x2 - x1, y2 - y1
#     gcd = compute_gcd(dx, dy)
#     for t in range(1, gcd):
#         yield (x1 + t * dx // gcd, y1 + t * dy // gcd)

# def blocked(grid, x, y, tx, ty):
#     """
#     # >>> blocked(['.#..#', '.....', '#####', '....#', '...##'], 3, 4, 1, 0)
#     # True
#     >>> blocked(['.#..#', '.....', '#####', '....#', '...##'], 1, 0, 4, 3)
#     True
#     >>> blocked(['.#..#', '.....', '#####', '....#', '...##'], 4, 3, 1, 0)
#     True
#     """
#     for bx, by in path(x, y, tx, ty):
#         if at(grid, (bx, by)) == '#':
#             return True
#     return False

# def visible_from_o(grid, pos):
#     """
#     >>> visible_from(['.#..#', '.....', '#####', '....#', '...##'], (1, 0))
#     7
#     >>> visible_from(['.#..#', '.....', '#####', '....#', '...##'], (3, 4))
#     8
#     """
#     gs = len(grid)
#     (x, y) = pos
#     cblocked = 0
#     for tx, ty in product(range(0, gs), range(0, gs)):
#         if at(grid, (tx, ty)) != '#' or (tx, ty) == pos:
#             continue
#         if blocked(grid, x, y, tx, ty):
#             cblocked += 1
#     return total_astroids(grid) - cblocked - 1

def visible_from(grid, pos):
    gs = len(grid)
    (x, y) = pos
    vals = set()
    for tx, ty in product(range(0, gs), range(0, gs)):
        if at(grid, (tx, ty)) != '#' or (tx, ty) == pos:
            continue
        vals.add(math.atan2(ty-y, tx-x))
    return len(vals)

def distance(x, y, tx, ty):
    return math.sqrt((x-tx)*(x-tx) + (y-ty)*(y-ty))

def oangle(x, y, tx, ty):
    """
    >>> oangle(10, 10, 10, 5)
    0.0
    >>> oangle(10, 10, 20, 10)
    1.5707963267948966
    >>> oangle(10, 10, 10, 15)
    3.141592653589793
    >>> oangle(10, 10, 0, 10)
    -1.5707963267948966
    """
    return math.atan2(tx-x, y-ty)

def part2(grid, pos):
    """
    >>> part2(testgrid, (11,13))
    802
    """
    (x, y) = pos
    gs = len(grid)
    vals = {}
    for tx, ty in product(range(0, gs), range(0, gs)):
        if at(grid, (tx, ty)) != '#' or (tx, ty) == pos:
            continue
        angle = oangle(x, y, tx, ty)
        if angle not in vals:
            vals[angle] = []
        vals[angle].append((distance(x, y, tx, ty), (tx, ty)))
    zapped = 0
    angles = sorted([k for k in vals])
    started = False
    for angle in cycle(angles):
        if angle == 0:
            started = True
        if not started:
            continue
        if angle in vals and vals[angle]:
            l = vals[angle]
            md = min(x for x, _ in l)
            mem = list(filter(lambda x: x[0] == md, l))
            vals[angle] = list(filter(lambda x: x[0] != md, l))
            zapped += 1
            # print(f'{zapped} {angle} {mem}')
            if zapped == 200:
                return mem[0][1][0]*100+mem[0][1][1]

def at(grid, pos):
    (x, y) = pos
    return grid[y][x]

def part1(grid):
    vis, station = test1(grid)
    print(f'station at {station}')
    return vis

def main():
    puzzle_input = adventofcode.read_input(10)
    adventofcode.answer(1, 329, part1(puzzle_input))
    adventofcode.answer(2, 512, part2(puzzle_input, (25, 31)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
