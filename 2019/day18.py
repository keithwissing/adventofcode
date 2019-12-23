#!/usr/bin/env python3

from heapq import heappush, heappop
from itertools import product
from string import ascii_lowercase, ascii_uppercase
import adventofcode

testdata2 = [
    '########################',
    '#f.D.E.e.C.b.A.@.a.B.c.#',
    '######################.#',
    '#d.....................#',
    '########################']

testdata3 = [
    '########################',
    '#...............b.C.D.f#',
    '#.######################',
    '#.....@.a.B.c.d.A.e.F.g#',
    '########################']

testdata4 = [
    '#################',
    '#i.G..c...e..H.p#',
    '########.########',
    '#j.A..b...f..D.o#',
    '########@########',
    '#k.E..a...g..B.n#',
    '########.########',
    '#l.F..d...h..C.m#',
    '#################']

testdata5 = [
    '########################',
    '#@..............ac.GI.b#',
    '###d#e#f################',
    '###A#B#C################',
    '###g#h#i################',
    '########################']

def test1(lines):
    """
    >>> test1(testdata2)
    86
    >>> test1(testdata3)
    132
    >>> test1(testdata5)
    81
    >>> test1(testdata4)
    136
    """
    g = Grid(lines)
    return part1(g)

def distances(dist, start, goal, adjf):
    found = None
    heap = []
    for a in adjf(start):
        heappush(heap, (1, a))
    while heap and not found:
        d, pos = heappop(heap)
        if pos not in dist or d < dist[pos]:
            dist[pos] = d
            if len(pos[1]) == goal:
                found = pos
                break
            for a in adjf(pos):
                heappush(heap, (d + 1, a))
    return dist, found

def part1(g):
    start = (g.find('@'), tuple())
    keys = set(g.grid[y][x] for x, y in product(range(g.width), range(g.height)) if g.grid[y][x] in ascii_lowercase)
    dist, found = distances({start: 0}, start, len(keys), g.adjacent)
    pos = dist[found]
    return pos

dataset1 = [
    '#######',
    '#a.#Cd#',
    '##...##',
    '##.@.##',
    '##...##',
    '#cB#Ab#',
    '#######'
]

dataset2 = [
    '###############',
    '#d.ABC.#.....a#',
    '######@#@######',
    '###############',
    '######@#@######',
    '#b.....#.....c#',
    '###############'
]

dataset3 = [
    '#############',
    '#DcBa.#.GhKl#',
    '#.###@#@#I###',
    '#e#d#####j#k#',
    '###C#@#@###J#',
    '#fEbA.#.FgHi#',
    '#############',
]

dataset4 = [
    '#############',
    '#g#f.D#..h#l#',
    '#F###e#E###.#',
    '#dCba@#@BcIJ#',
    '#############',
    '#nK.L@#@G...#',
    '#M###N#H###.#',
    '#o#m..#i#jk.#',
    '#############',
]

def part2(lines):
    """
    >>> part2(dataset1)
    8
    >>> part2(dataset2)
    24

    # >>> part2(dataset3)
    # 32
    # >>> part2(dataset4)
    # 72
    """
    g = Grid(lines)
    cx, cy = g.width//2, g.height//2
    for p in [(cy-1, cx), (cy, cx), (cy+1, cx), (cy, cx-1), (cy, cx+1)]:
        g.grid[p[0]][p[1]] = '#'
    starts = ((cx-1, cy-1), (cx+1, cy-1), (cx-1, cy+1), (cx+1, cy+1))
    keys = frozenset(g.grid[y][x] for x, y in product(range(g.width), range(g.height)) if g.grid[y][x] in ascii_lowercase)
    keys0 = frozenset(g.grid[y][x] for x, y in product(range(cx), range(cy)) if g.grid[y][x] in ascii_lowercase)
    keys1 = frozenset(g.grid[y][x] for x, y in product(range(cx, g.width), range(cy)) if g.grid[y][x] in ascii_lowercase)
    keys2 = frozenset(g.grid[y][x] for x, y in product(range(cx), range(cy, g.height)) if g.grid[y][x] in ascii_lowercase)
    keys3 = frozenset(g.grid[y][x] for x, y in product(range(cx, g.width), range(cy, g.height)) if g.grid[y][x] in ascii_lowercase)
    kqs = [keys0, keys1, keys2, keys3]
    total = 0
    for q in range(4):
        start = (starts[q], keys - kqs[q])
        dist, found = distances({start: 0}, start, len(keys), g.adjacent)
        total += dist[found]
    return total

def adjacent(pos):
    # clockwise, starting up, negative y is up
    for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        yield (pos[0]+d[0], pos[1]+d[1])

class Grid:
    def __init__(self, lines):
        self.grid = [list(l) for l in lines]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.find_cache = {}
        self.doors_cache = {}

    def find(self, c):
        if c not in self.find_cache:
            self.find_cache[c] = None
            for x, y in product(range(self.width), range(self.height)):
                if self.grid[y][x] == c:
                    self.find_cache[c] = (x, y)
        return self.find_cache[c]

    def adjacent(self, state):
        pos, keys = state
        for a in adjacent(pos):
            c = self.get(a)
            if c == '#':
                continue
            if c in ['.', '@']:
                yield (a, keys)
            if c in ascii_lowercase:
                if c in keys:
                    yield (a, keys)
                else:
                    yield (a, tuple(sorted(list(keys) + [c])))
            if c in ascii_uppercase:
                if c.lower() in keys:
                    yield (a, keys)

    def adjacent2(self, state):
        poses, keys = state
        for i, pos in enumerate(poses):
            for a in adjacent(pos):
                c = self.get(a)
                if c == '#':
                    continue
                if c in ['.', '@'] or (c in ascii_lowercase and c in keys) or (c in ascii_uppercase and c.lower() in keys):
                    al = list(poses)
                    al[i] = a
                    yield (tuple(al), keys)
                elif c in ascii_lowercase:
                    al = list(poses)
                    al[i] = a
                    yield (tuple(al), tuple(sorted(list(keys) + [c])))

    def get(self, pos):
        if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            return self.grid[pos[1]][pos[0]]
        return '#'

    def __repr__(self):
        return '\n'.join([''.join(l) for l in self.grid])

def main():
    puzzle_input = adventofcode.read_input(18)
    adventofcode.answer(1, 7430, test1(puzzle_input))
    adventofcode.answer(2, 1864, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
