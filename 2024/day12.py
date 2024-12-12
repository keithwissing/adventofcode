#!/usr/bin/env python3
from collections import defaultdict

import adventofcode

t1 = [
    'AAAA',
    'BBCD',
    'BBCC',
    'EEEC',
]

t2 = [
    'OOOOO',
    'OXOXO',
    'OOOOO',
    'OXOXO',
    'OOOOO',
]

t3 = [
    'RRRRIICCFF',
    'RRRRIICCCF',
    'VVRRRCCFFF',
    'VVRCCCJFFF',
    'VVVVCJJCFE',
    'VVIVCCJJEE',
    'VVIIICJJEE',
    'MIIIIIJJEE',
    'MIIISIJEEE',
    'MMMISSJEEE',
]

def find_region(grid):
    pos, crop = next(iter(grid.items()))
    perimeter = 0
    plots = {pos}
    outside = set()
    q = [pos]
    while q:
        pos = q.pop()
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            neighbor = (pos[0] + d[0], pos[1] + d[1])
            if grid[neighbor] != crop:
                perimeter += 1
                outside.add((neighbor, d))
            else:
                if neighbor not in plots:
                    plots.add(neighbor)
                    q.append(neighbor)

    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        outside -= set(((p[0] + d[0], p[1] + d[1]), a) for p, a in outside)

    return crop, plots, perimeter, len(outside)

def find_all_regions(lines):
    width, height = len(lines[0]), len(lines)
    grid = defaultdict(lambda: '', {(x, y): lines[y][x] for x in range(width) for y in range(height)})

    while grid:
        crop, plots, perimeter, sides = find_region(grid)
        grid = defaultdict(lambda: '', {k: v for k, v in grid.items() if k not in plots and v})
        yield crop, plots, perimeter, sides

def part1(lines):
    """
    # >>> part1(t1)
    # 140
    #
    # >>> part1(t2)
    # 772
    #
    # >>> part1(t3)
    # 1930
    """

    return sum(len(plots) * perimeter for _, plots, perimeter, _ in find_all_regions(lines))

def part2(lines):
    """
    >>> part2(t1)
    80

    >>> part2(t2)
    436

    >>> part2(t3)
    1206
    """
    return sum(len(plots) * sides for _, plots, _, sides in find_all_regions(lines))

def main():
    puzzle_input = adventofcode.read_input(12)
    adventofcode.answer(1, 1477924, part1(puzzle_input))
    adventofcode.answer(2, 841934, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
