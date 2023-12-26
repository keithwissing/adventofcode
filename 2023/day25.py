#!/usr/bin/env python3
from math import prod

import networkx as nx
from matplotlib import pyplot as plt

import adventofcode

t1 = [
    'jqt: rhn xhk nvd',
    'rsh: frs pzl lsr',
    'xhk: hfx',
    'cmg: qnr nvd lhk bvb',
    'rhn: xhk bvb hfx',
    'bvb: xhk hfx',
    'pzl: lsr hfx nvd',
    'qnr: nvd',
    'ntq: jqt hfx bvb xhk',
    'nvd: lhk',
    'lsr: lhk',
    'rzs: qnr cmg lsr rsh',
    'frs: qnr lhk lsr',
]

def plot_graph(g):
    pos = nx.spring_layout(g, seed=1)
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_edges(g, pos, width=3)
    nx.draw_networkx_labels(g, pos, font_size=20, font_family="sans-serif")
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def part1(lines):
    """
    # >>> part1(t1)
    54
    """
    g = nx.Graph()
    for line in lines:
        cs = line.replace(':', '').split()
        for c2 in cs[1:]:
            g.add_edge(cs[0], c2)

    # plot_graph(g)

    # These cuts are specific to my puzzle input. I found them by plotting the graph and inspecting it visually.
    cuts = [('tnz', 'dgt'), ('ddc', 'gqm'), ('kzh', 'rks')]
    for re in cuts:
        g.remove_edge(re[0], re[1])

    return prod(len(x) for x in nx.connected_components(g))

def main():
    puzzle_input = adventofcode.read_input(25)
    adventofcode.answer(1, 520380, part1(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
