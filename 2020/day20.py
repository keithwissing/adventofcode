#!/usr/bin/env python3

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
        tile = lines[pos+1:pos+11]
        tiles[idn] = tile
        pos += 12
    return tiles

def part1(lines):
    """
    >>> part1(t1)
    20899048083289
    """
    tiles = parse(lines)
    edges = {}
    for idn, tile in tiles.items():
        top = int(''.join(['0' if c == '.' else '1' for c in tile[0]]), 2)
        bottom = int(''.join(['0' if c == '.' else '1' for c in tile[9]]), 2)
        left = int(''.join(['0' if r[0] == '.' else '1' for r in tile]), 2)
        right = int(''.join(['0' if r[9] == '.' else '1' for r in tile]), 2)
        top2 = int(''.join(['0' if c == '.' else '1' for c in tile[0]][::-1]), 2)
        bottom2 = int(''.join(['0' if c == '.' else '1' for c in tile[9][::-1]]), 2)
        left2 = int(''.join(['0' if r[0] == '.' else '1' for r in tile])[::-1], 2)
        right2 = int(''.join(['0' if r[9] == '.' else '1' for r in tile])[::-1], 2)
        edges[idn] = [top, bottom, left, right, top2, bottom2, left2, right2]
    tot = 1
    for idn, es in edges.items():
        o = set()
        for k, e in edges.items():
            if k == idn:
                continue
            o.update(e)
        if len(o.intersection(es[:4])) == 2 or len(o.intersection(es[4:])) == 2:
            tot *= idn
    return tot

def main():
    puzzle_input = adventofcode.read_input(20)
    adventofcode.answer(1, 29584525501199, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
