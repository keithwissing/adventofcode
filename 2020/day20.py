#!/usr/bin/env python3

import itertools
import math
import adventofcode

t1 = [
    'Tile 2311:',
    '..##.#..#.',
    '##..#.....',
    '#...##..#.',
    '####.#...#',
    '##.##.###.',
    '##...#.###',
    '.#.#.#..##',
    '..#....#..',
    '###...#.#.',
    '..###..###',
    '',
    'Tile 1951:',
    '#.##...##.',
    '#.####...#',
    '.....#..##',
    '#...######',
    '.##.#....#',
    '.###.#####',
    '###.##.##.',
    '.###....#.',
    '..#.#..#.#',
    '#...##.#..',
    '',
    'Tile 1171:',
    '####...##.',
    '#..##.#..#',
    '##.#..#.#.',
    '.###.####.',
    '..###.####',
    '.##....##.',
    '.#...####.',
    '#.##.####.',
    '####..#...',
    '.....##...',
    '',
    'Tile 1427:',
    '###.##.#..',
    '.#..#.##..',
    '.#.##.#..#',
    '#.#.#.##.#',
    '....#...##',
    '...##..##.',
    '...#.#####',
    '.#.####.#.',
    '..#..###.#',
    '..##.#..#.',
    '',
    'Tile 1489:',
    '##.#.#....',
    '..##...#..',
    '.##..##...',
    '..#...#...',
    '#####...#.',
    '#..#.#.#.#',
    '...#.#.#..',
    '##.#...##.',
    '..##.##.##',
    '###.##.#..',
    '',
    'Tile 2473:',
    '#....####.',
    '#..#.##...',
    '#.##..#...',
    '######.#.#',
    '.#...#.#.#',
    '.#########',
    '.###.#..#.',
    '########.#',
    '##...##.#.',
    '..###.#.#.',
    '',
    'Tile 2971:',
    '..#.#....#',
    '#...###...',
    '#.#.###...',
    '##.##..#..',
    '.#####..##',
    '.#..####.#',
    '#..#.#..#.',
    '..####.###',
    '..#.#.###.',
    '...#.#.#.#',
    '',
    'Tile 2729:',
    '...#.#.#.#',
    '####.#....',
    '..#.#.....',
    '....#..#.#',
    '.##..##.#.',
    '.#.####...',
    '####.#.#..',
    '##.####...',
    '##..#.##..',
    '#.##...##.',
    '',
    'Tile 3079:',
    '#.#.#####.',
    '.#..######',
    '..#.......',
    '######....',
    '####.#..#.',
    '.#...#.##.',
    '#.#####.##',
    '..#.###...',
    '..#.......',
    '..#.###...',
]

def parse(lines):
    tiles = {}
    pos = 0
    while pos < len(lines):
        idn = int(lines[pos][5:9])
        tile = lines[pos + 1:pos + 11]
        tiles[idn] = tile
        pos += 12
    return tiles

def get_corner_idns(edges):
    ret = []
    for idn, es in edges.items():
        o = set()
        for k, e in edges.items():
            if k == idn:
                continue
            o.update(e)
        if len(o.intersection(es[:4])) == 2 or len(o.intersection(es[4:])) == 2:
            ret.append(idn)
    return ret

def flip_v(grid):
    return grid[::-1]

def flip_h(grid):
    return [l[::-1] for l in grid]

def rotate(grid):
    ret = []
    for x in range(len(grid) - 1, -1, -1):
        ret.append(''.join([r[x] for r in grid]))
    return ret

def printg(grid):
    print('\n'.join(grid))

def calc_edge_ids(grid):
    top = int(''.join(['0' if c == '.' else '1' for c in grid[0]]), 2)
    bottom = int(''.join(['0' if c == '.' else '1' for c in grid[9]]), 2)
    left = int(''.join(['0' if r[0] == '.' else '1' for r in grid]), 2)
    right = int(''.join(['0' if r[9] == '.' else '1' for r in grid]), 2)
    return [top, bottom, left, right]

def part1(lines):
    """
    >>> part1(t1)
    20899048083289
    """
    tiles = parse(lines)
    edges = {}
    for idn, tile in tiles.items():
        edges[idn] = calc_edge_ids(tile) + calc_edge_ids(flip_h(flip_v(tile)))
    corners = get_corner_idns(edges)
    return corners[0] * corners[1] * corners[2] * corners[3]

def upper_left(all_edges, grid):
    t, b, l, r = calc_edge_ids(grid)
    return t not in all_edges and l not in all_edges

def left_is(goal, grid):
    t, b, l, r = calc_edge_ids(grid)
    return l == goal

def top_is(goal, grid):
    t, b, l, r = calc_edge_ids(grid)
    return t == goal

def orient(grid, match_func):
    for _ in range(4):
        if match_func(grid):
            return grid
        grid = rotate(grid)
    grid = flip_v(grid)
    for _ in range(4):
        if match_func(grid):
            return grid
        grid = rotate(grid)
    raise 'Did not find orientation match'

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ', ]

def find_monsters(image):
    count = 0
    for row in range(0, len(image) - len(monster)):
        for col in range(0, len(image[0]) - len(monster[0])):
            found = True
            for y, x in itertools.product(range(len(monster)), range(len(monster[0]))):
                if monster[y][x] == '#' and image[row + y][col + x] != '#':
                    found = False
            if found:
                count += 1
    return count

def part2(lines):
    """
    # >>> part2(t1)
    # 273
    """
    tiles = parse(lines)
    edges = {}
    for idn, tile in tiles.items():
        edges[idn] = calc_edge_ids(tile) + calc_edge_ids(flip_h(flip_v(tile)))

    corners = get_corner_idns(edges)
    cidn = corners[0]

    for idn, es in edges.items():
        o = set()
        for k, e in edges.items():
            if k == cidn:
                continue
            o.update(e)
    # print('aaa ', ' '.join([str(x) if x in o else 'x' for x in edges[cidn]]))

    size = int(math.sqrt(len(tiles)))
    pieces = [[None] * size for _ in range(size)]
    ids = [[None] * size for _ in range(size)]

    used = set([cidn])

    ul = orient(tiles[cidn], lambda g: upper_left(o, g))
    pieces[0][0] = ul
    ids[0][0] = cidn
    for col in range(1, size):
        left = calc_edge_ids(pieces[0][col - 1])[3]
        tidn = [i for i, e in edges.items() if left in e and i not in used][0]
        grid = tiles[tidn]
        grid = orient(grid, lambda g, l=left: left_is(l, g))
        pieces[0][col] = grid
        ids[0][col] = tidn
        used.add(tidn)

    for row in range(1, size):
        for col in range(0, size):
            top = calc_edge_ids(pieces[row - 1][col])[1]
            tidn = [i for i, e in edges.items() if top in e and i not in used][0]
            grid = tiles[tidn]
            grid = orient(grid, lambda g, t=top: top_is(t, g))
            pieces[row][col] = grid
            ids[row][col] = tidn
            used.add(tidn)

    # print(len(used), len(tiles))

    # for row in range(0, size):
    #     for r in range(0, 10):
    #         print(' '.join([pieces[row][x][r] for x in range(0, size)]))
    #     print()

    # print(ids)

    image = []
    for row in range(0, size):
        for r in range(1, 9):
            image.append(''.join([pieces[row][x][r][1:-1] for x in range(0, size)]))

    # print('\n'.join(image))

    image = orient(image, lambda g: find_monsters(g) != 0)

    found = find_monsters(image)
    seas = sum(1 for y,x in itertools.product(range(len(image)), range(len(image[0]))) if image[y][x] == '#')
    msize = sum(1 for y,x in itertools.product(range(len(monster)), range(len(monster[0]))) if monster[y][x] == '#')
    a = seas - found * msize
    # print(found, a)
    return a

def main():
    puzzle_input = adventofcode.read_input(20)
    adventofcode.answer(1, 29584525501199, part1(puzzle_input))
    adventofcode.answer(2, 1665, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
