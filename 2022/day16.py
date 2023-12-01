#!/usr/bin/env python3

import adventofcode

t1 = [
    'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
    'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
    'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
    'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
    'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
    'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
    'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
    'Valve HH has flow rate=22; tunnel leads to valve GG',
    'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
    'Valve JJ has flow rate=21; tunnel leads to valve II',
]

class Valve:
    def __init__(self, line):
        w = line.split()
        self.valve = w[1]
        self.flow = int(w[4][5:-1])
        self.tunnels = [v[:2] for v in w[9:]]

    def print(self):
        print(f'Valve {self.valve} flow {self.flow} tunnels {self.tunnels}')

class Valves:
    def __init__(self, valves):
        self.valves = valves

    def get(self, v):
        return next(filter(lambda x: x.valve == v, self.valves))

class State:
    def __init__(self):
        self.remaining_time = 30
        self.open_valves = set()
        self.pos = 'AA'
        self.relief = 0

def parse(lines):
    return [Valve(line) for line in lines]

def distance(src, dst, valves):
    steps = 0
    reached = set([src])
    while dst not in reached:
        steps += 1
        stretch = set()
        for v in reached:
            stretch.update(valves.get(v).tunnels)
        reached.update(stretch)
    return steps

def step(state, valves):
    possible = [v.valve for v in valves.valves if v.flow != 0 and v.valve not in state.open_valves]
    aa = [(v, distance(state.pos, v, valves)) for v in possible]
    bb = [(v, d, (state.remaining_time - d + 1) * valves.get(v).flow) for v, d in aa]
    print(bb)

def part1(lines):
    """
    >>> part1(t1)
    1651
    """
    valves = Valves(parse(lines))
    state = State()
    step(state, valves)

def part2(lines):
    """
    # >>> part2(t1)
    """

def main():
    puzzle_input = adventofcode.read_input(16)
    # puzzle_input = [int(x) for x in puzzle_input]
    # adventofcode.answer(1, 0, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
