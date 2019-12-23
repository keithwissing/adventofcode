#!/usr/bin/env python3

from heapq import heappush, heappop
from itertools import product
from random import randint, choice
from string import ascii_lowercase, ascii_letters, ascii_uppercase
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

cur_min = 5000000

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
    global cur_min
    g = Grid(lines)
    # print(g.reach(['b']))
    # print(','.join(str(g.find(chr(a))) for a in range(ord('a'), ord('z')+1)))
    # dist = g.distances_from(g.pos)
    # return g.distance_from_to(g.find('@'), g.find('b'))
    cur_min = 5000000
    return part1(g)
    return min_path(g)
    return min_dist(g)
    # # print(g)
    # dist, reach = g.distances()
    # while reach:
    #     kl = ''.join(sorted(list([x for x in reach if x.islower()])))
    #     k = kl[0]
    #     # print(k, kl)
    #     g.move(g.find(k))
    #     # print(f'moved {g.mc}')
    #     dist, reach = g.distances()
    # return g.mc

    # min=136 picked=['h', 'd', 'a', 'b', 'j', 'g', 'n', 'f', 'o', 'c', 'i', 'e', 'p', 'k', 'l', 'm']
    # min=136 picked=['d', 'h', 'a', 'g', 'c', 'i', 'e', 'p', 'b', 'j', 'f', 'o', 'n', 'k', 'm', 'l']
    # min=136 picked=['c', 'e', 'f', 'a', 'k', 'b', 'j', 'g', 'n', 'd', 'l', 'h', 'm', 'o', 'i', 'p']

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
    >>> part2(dataset3)
    32
    >>> part2(dataset4)
    72
    """
    g = Grid(lines)
    cx, cy = g.width//2, g.height//2
    g.grid[cy-1][cx] = '#'
    g.grid[cy][cx] = '#'
    g.grid[cy+1][cx] = '#'
    g.grid[cy][cx-1] = '#'
    g.grid[cy][cx+1] = '#'
    # start = (((cx-1, cy-1), (cx+1, cy-1), (cx-1, cy+1), (cx+1, cy+1)), tuple())
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

def pheappush(heap, state):
    heappush(heap, ((1000-len(state[2]), state[0]), state))

def min_path(g):
    min_d = 150
    min_p = []
    heap = []
    mc = 0
    pos = g.find('@')
    picked = []
    reach = g.reach(picked)
    for n in reach:
        # heappush(heap, (pos, (mc, pos, picked[:], n)))
        pheappush(heap, (mc, pos, picked[:], n))
    while heap:
        _, (mc, pos, picked, k) = heappop(heap)
        if mc < min_d:
            dest = g.find(k)
            mc += g.distance_from_to(pos, dest)
            pos = dest
            picked.append(k)
            reach = g.reach(picked)
            if not reach:
                if mc < min_d:
                    min_d = mc
                    min_p = picked[:]
                    print(f'min={min_d} picked={min_p}', flush=True)
            else:
            # for n in reach:

                n = choice(reach)
                # heappush(heap, (pos, (mc, pos, picked[:], n)))
                pheappush(heap, (mc, pos, picked[:], n))
                n = choice(reach)
                # heappush(heap, (pos, (mc, pos, picked[:], n)))
                pheappush(heap, (mc, pos, picked[:], n))
    # print(f'min={min_d} picked={min_p}')
    return min_d

def min_dist(g, mc=0, pos=None, picked=None, k=None):
    global cur_min
    # print(f'{k}')
    if pos is None:
        pos = g.find('@')
    if picked is None:
        picked = []
    if k is not None:
        dest = g.find(k)
        mc += g.distance_from_to(pos, dest)
        pos = dest
        picked.append(k)
    reach = g.reach(picked)
    while reach and mc < cur_min:
        if len(reach) > 1:
            # print(f'choices are {reach}')
            return min(min_dist(g, mc, pos, picked[:], k) for k in reach)
        else:
            k = reach[0]
            dest = g.find(k)
            mc += g.distance_from_to(pos, dest)
            pos = dest
            picked.append(k)
        reach = g.reach(picked)
    print(f'min={cur_min} mc = {mc}  picked = {picked}')
    if mc < cur_min:
        cur_min = mc
    return mc

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
        self.dist_cache = {}
        self.doors_cache = {}
        self.picked = set()
        self.pos = self.find('@')
        self.mc = 0

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

    def move(self, dest):
        dist = self.distance_from_to(self.pos, dest)
        self.mc += dist
        self.pos = dest
        self.picked.add(self.get(dest))

    def get(self, pos):
        if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            return self.grid[pos[1]][pos[0]]
        return '#'

    def reach(self, keys):
        reach = []
        for t in ascii_lowercase:
            if t not in keys and self.find(t) is not None:
                d = self.doors(t)
                if all(x.lower() in keys for x in d):
                    reach.append(t)
        return reach

    def doors(self, key):
        if key not in self.doors_cache:
            p = self.find(key)
            self.doors_cache[key] = self.doors_to(p)
        return self.doors_cache[key]

    def doors_to(self, pos):
        dist = self.distances_from(self.find('@'))
        doors = []
        for p in path(dist, pos):
            if self.get(p) in ascii_letters:
                doors.append(self.get(p))
        return doors

    def distance_from_to(self, a, b):
        if a not in self.dist_cache:
            self.dist_cache[a] = self.distances_from(a)
        return self.dist_cache[a][b]

    def distances_from(self, pos):
        dist = {pos: 0}
        heap = []
        for a in adjacent(pos):
            if self.get(a) != '#':
                heappush(heap, (1, a))
        while heap:
            nd, pos = heappop(heap)
            if pos not in dist or nd < dist[pos]:
                dist[pos] = nd
                for a in adjacent(pos):
                    if self.get(a) != '#':
                        heappush(heap, (nd+1, a))
        return dist

    def distances(self, pos=None):
        pos = self.pos if pos is None else pos
        dist = {pos: 0}
        reach = set()
        heap = []
        for a in adjacent(pos):
            heappush(heap, a)
        while heap:
            pos = heappop(heap)
            v = self.get(pos)
            if v != '#':
                mad = min(dist[a] for a in adjacent(pos) if a in dist and self.get(a) != '#')
                if pos not in dist or mad + 1 < dist[pos]:
                    dist[pos] = mad + 1
                    if v == '.':
                        for a in adjacent(pos):
                            heappush(heap, a)
                    else:
                        reach.add(v)
        return dist, reach

    def __repr__(self):
        return '\n'.join([''.join(l) for l in self.grid])

def path(dist, pos):
    cd = dist[pos]
    while cd > 0:
        for nc in adjacent(pos):
            if nc in dist and dist[nc] == cd - 1:
                yield nc
                pos = nc
                cd -= 1
                break

def display_dict_as_grid(panel):
    (minX, maxX), (minY, maxY) = [(min(c), max(c)) for c in zip(*panel)]
    for row in range(minY, maxY+1):
        line = [str(panel[(x, row)]) if (x, row) in panel else ' ' for x in range(minX, maxX+1)]
        print(','.join(line))

def main():
    puzzle_input = adventofcode.read_input(18)
    # adventofcode.answer(1, 7430, test1(puzzle_input))
    adventofcode.answer(2, 1864, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
