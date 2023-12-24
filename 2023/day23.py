#!/usr/bin/env python3
from collections import defaultdict
from heapq import heappop, heappush
from itertools import product
from sys import maxsize

import matplotlib.pyplot as plt
import networkx as nx

import adventofcode

t1 = [
    '#.#####################',
    '#.......#########...###',
    '#######.#########.#.###',
    '###.....#.>.>.###.#.###',
    '###v#####.#v#.###.#.###',
    '###.>...#.#.#.....#...#',
    '###v###.#.#.#########.#',
    '###...#.#.#.......#...#',
    '#####.#.#.#######.#.###',
    '#.....#.#.#.......#...#',
    '#.#####.#.#.#########v#',
    '#.#...#...#...###...>.#',
    '#.#.#v#######v###.###v#',
    '#...#.>.#...>.>.#.###.#',
    '#####v#.#.###v#.#.###.#',
    '#.....#...#...#.#.#...#',
    '#.#########.###.#.#.###',
    '#...###...#...#...#.###',
    '###.###.#.###v#####v###',
    '#...#...#.#.>.>.#.>.###',
    '#.###.###.#.###.#.#v###',
    '#.....###...###...#...#',
    '#####################.#',
]

def parse(lines):
    grid = defaultdict(lambda: '#')
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            grid[(x, y)] = c
    return grid

def adjacent(pos):
    # clockwise, starting up, negative y is up
    for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        yield pos[0] + d[0], pos[1] + d[1]

def walkable(grid, icy, pos):
    c = grid[pos]
    dirs = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    if icy and c in dirs:
        d = dirs[c]
        adj = [(pos[0] + d[0], pos[1] + d[1])]
    else:
        adj = adjacent(pos)
    return adj

def find_route(lines, icy):
    grid = parse(lines)
    start = (1, 0)
    destination = (len(lines[0]) - 2, len(lines) - 1)

    distances = {}
    q = [(maxsize, 0, start, {start})]
    while q:
        _, dist, pos, been = heappop(q)
        if pos not in distances or distances[pos] <= dist:
            distances[pos] = dist
            adj = walkable(grid, icy, pos)
            adj = [np for np in adj if grid[np] != '#' and np not in been]
            for np in adj:
                heappush(q, (maxsize - (dist + 1), dist + 1, np, been | {np}))

    return distances[destination]

def part1(lines):
    """
    # >>> part1(t1)
    94
    """
    return find_route(lines, True)

def display(grid, been, w, h):
    for y in range(h):
        for x in range(w):
            ic = '+' if (x, y) in been else grid[(x, y)]
            if ic == '#':
                ic = ' '
            print(ic, end='')
        print()

def part2(lines):
    """
    # >>> part2(t1)
    154
    """
    return route_using_networkx(lines)

def find_graph(lines):
    grid = parse(lines)
    w, h = len(lines[0]), len(lines)
    start = (1, 0)
    destination = (len(lines[0]) - 2, len(lines) - 1)
    nodes = find_nodes(grid, w, h, start, destination)
    weights = find_weights(grid, nodes)
    return weights, start, destination

def find_weights(grid, nodes):
    weights = {}
    for node in nodes:
        clear = set(p for p in adjacent(node) if grid[p] != '#')
        for np in clear:
            been = {node, np}
            while np not in nodes:
                adj = walkable(grid, False, np)
                npl = [p for p in adj if grid[p] != '#' and p not in been]
                if not npl:
                    break
                assert len(npl) == 1
                been.add(npl[0])
                np = npl[0]
            if np in nodes:
                edge = (min(node, np), max(node, np))
                weight = len(been) - 1
                weights[edge] = weight
    return weights

def find_nodes(grid, w, h, start, destination):
    nodes = {start, destination}
    for x, y in product(range(w), range(h)):
        if grid[(x, y)] != '#':
            adj = set(p for p in adjacent((x, y)) if grid[p] != '#')
            if len(adj) > 2:
                nodes.add((x, y))
    return nodes

def hike_length(weights, x):
    return sum(weights[(min(x[i], x[i + 1]), max(x[i], x[i + 1]))] for i in range(len(x) - 1))

def route_using_networkx(lines):
    weights, start, destination = find_graph(lines)

    # g = nx.from_edgelist(weights.keys())
    g = nx.Graph()
    for e, w in weights.items():
        g.add_edge(e[0], e[1], weight=w)

    longest = max(nx.all_simple_paths(g, start, destination), key=lambda a: hike_length(weights, a))
    pe = list(nx.utils.pairwise(longest))

    visual = False
    if visual:
        plot_graph(g, pe)

    ll = hike_length(weights, longest)
    return ll

def plot_graph(g, pe):
    # pos = nx.spring_layout(g, seed=seed)
    pos = nx.kamada_kawai_layout(g)
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_edges(g, pos, width=3)
    if pe:
        nx.draw_networkx_edges(g, pos, edgelist=pe, edge_color="red", width=6)
    nx.draw_networkx_labels(g, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def main():
    puzzle_input = adventofcode.read_input(23)
    adventofcode.answer(0, 94, part1(t1))
    adventofcode.answer(1, 2310, part1(puzzle_input))
    adventofcode.answer(0, 154, part2(t1))
    adventofcode.answer(2, 6738, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
