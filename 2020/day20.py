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
    t, _, l, _ = calc_edge_ids(grid)
    return t not in all_edges and l not in all_edges

def left_is(goal, grid):
    _, _, l, _ = calc_edge_ids(grid)
    return l == goal

def top_is(goal, grid):
    t, _, _, _ = calc_edge_ids(grid)
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

def find_and_orient_pieces(tiles):
    edges = {idn: calc_edge_ids(tile) + calc_edge_ids(flip_h(flip_v(tile))) for idn, tile in tiles.items()}

    corners = get_corner_idns(edges)
    cidn = corners[0] # does not matter which corner piece we start with

    size = int(math.sqrt(len(tiles)))
    pieces = [[None] * size for _ in range(size)]
    ids = [[None] * size for _ in range(size)]

    edges_minus_corner = set(i for k, e in edges.items() if k != cidn for i in e)
    uppper_left = orient(tiles[cidn], lambda g: upper_left(edges_minus_corner, g))

    pieces[0][0] = uppper_left
    ids[0][0] = cidn
    used = set([cidn])

    for col in range(1, size):
        left = calc_edge_ids(pieces[0][col - 1])[3] # right from tile to the left
        tidn = [i for i, e in edges.items() if left in e and i not in used][0]
        grid = orient(tiles[tidn], lambda g, l=left: left_is(l, g))
        pieces[0][col] = grid
        ids[0][col] = tidn
        used.add(tidn)

    for row in range(1, size):
        for col in range(0, size):
            top = calc_edge_ids(pieces[row - 1][col])[1] # bottom from tile above
            tidn = [i for i, e in edges.items() if top in e and i not in used][0]
            grid = orient(tiles[tidn], lambda g, t=top: top_is(t, g))
            pieces[row][col] = grid
            ids[row][col] = tidn
            used.add(tidn)

    return pieces

def image_from_pieces(pieces):
    image = []
    for row in range(0, len(pieces)):
        for r in range(1, 9):
            image.append(''.join([pieces[row][x][r][1:-1] for x in range(0, len(pieces[row]))]))
    return image

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
    >>> part2(t1)
    273
    """
    tiles = parse(lines)
    pieces = find_and_orient_pieces(tiles)
    image = image_from_pieces(pieces)
    image = orient(image, lambda g: find_monsters(g) != 0)
    found = find_monsters(image)
    seas = sum(x.count('#') for x in image)
    msize = sum(x.count('#') for x in monster)
    return seas - found * msize

def main():
    puzzle_input = adventofcode.read_input(20)
    adventofcode.answer(1, 29584525501199, part1(puzzle_input))
    adventofcode.answer(2, 1665, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
