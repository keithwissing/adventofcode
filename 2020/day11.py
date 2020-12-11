#!/usr/bin/env python3

import adventofcode

t1 = [
    'L.LL.LL.LL',
    'LLLLLLL.LL',
    'L.L.L..L..',
    'LLLL.LL.LL',
    'L.LL.LL.LL',
    'L.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLLL',
    'L.LLLLLL.L',
    'L.LLLLL.LL',
]

def safe_get(y, x, lines):
    if 0 <= y < len(lines) and 0 <= x < len(lines[0]):
        return lines[y][x]
    return None

def count_adjacent(y, x, lines):
    count = 0
    for yi in range(y - 1, y + 2):
        for xi in range(x - 1, x + 2):
            if x == xi and y == yi:
                continue
            if safe_get(yi, xi, lines) == '#':
                count += 1
    return count

def count_seen(y, x, lines):
    count = 0
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for d in dirs:
        pos = (y, x)
        while True:
            pos = (pos[0] + d[0], pos[1] + d[1])
            peek = safe_get(pos[0], pos[1], lines)
            if peek is None or peek == 'L':
                break
            if peek == '.':
                continue
            if peek == '#':
                count += 1
                break
    return count

def tick(lines, counter, tolerance):
    changed = False
    future = []
    for yi in range(0, len(lines)):
        nl = ''
        for xi in range(0, len(lines[0])):
            cur = lines[yi][xi]
            if cur == 'L' and counter(yi, xi, lines) == 0:
                nl += '#'
                changed = True
            elif cur == '#' and counter(yi, xi, lines) >= tolerance:
                nl += 'L'
                changed = True
            else:
                nl += cur
        future.append(nl)
    return future, changed

def count_occupied(lines):
    tot = 0
    for l in lines:
        tot += l.count('#')
    return tot

def find_occupied_at_stability(seats, counter, tolerance):
    changed = True
    while changed:
        seats, changed = tick(seats, counter, tolerance)
    return count_occupied(seats)

def part1(lines):
    """
    >>> part1(t1)
    37
    """
    return find_occupied_at_stability(lines, count_adjacent, 4)

def part2(lines):
    """
    >>> part2(t1)
    26
    """
    return find_occupied_at_stability(lines, count_seen, 5)

def main():
    puzzle_input = adventofcode.read_input(11)
    adventofcode.answer(1, 2346, part1(puzzle_input))
    adventofcode.answer(2, 2111, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
