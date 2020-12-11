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
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(1 for d in dirs if safe_get(y + d[0], x + d[1], lines) == '#')

def see_occupied(pos, delta, lines):
    while True:
        pos = (pos[0] + delta[0], pos[1] + delta[1])
        peek = safe_get(pos[0], pos[1], lines)
        if peek == '.':
            continue
        if peek is None or peek == 'L':
            return False
        if peek == '#':
            return True

def count_seen(y, x, lines):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(1 for d in dirs if see_occupied((y, x), d, lines))

def apply(y, x, seats, counter, tolerance):
    cur = seats[y][x]
    if cur == 'L' and counter(y, x, seats) == 0:
        return '#'
    if cur == '#' and counter(y, x, seats) >= tolerance:
        return 'L'
    return cur

def tick(seats, counter, tolerance):
    future = []
    for y, cur in enumerate(seats):
        nl = ''.join(apply(y, x, seats, counter, tolerance) for x in range(0, len(cur)))
        future.append(nl)
    changed = seats != future
    return future, changed

def count_occupied(lines):
    return sum(l.count('#') for l in lines)

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
