#!/usr/bin/env python3

import adventofcode

t1 = [
    '939',
    '7,13,x,x,59,x,31,19',
]

def part1(lines):
    """
    >>> part1(t1)
    295
    """
    earliest = int(lines[0])
    busses = lines[1].split(',')
    busses = [int(x) for x in busses if x != 'x']
    leave = earliest
    while True:
        leave += 1
        bus = [x for x in busses if leave % x == 0]
        if bus:
            break
    return bus[0] * (leave - earliest)

def part2(line):
    """
    >>> part2('17,x,13,19')
    3417
    >>> part2('67,7,59,61')
    754018
    >>> part2('67,x,7,59,61')
    779210
    >>> part2('67,7,x,59,61')
    1261476
    >>> part2('1789,37,47,1889')
    1202161486
    """
    busses = line.split(',')
    busses = [0 if x == 'x' else int(x) for x in busses]

    if len(line) > 20:
        # print(','.join([f'(t+{i}) mod {x}=0' for i, x in enumerate(busses) if x != 0]))
        print('{' + ', '.join(f'Mod[t + {i}, {x}] == 0' for i, x in enumerate(busses) if x != 0) + '}')
        # Feed above printout to Wolfram Alpha
        # t = 1145159583560291 n + 939490236001473, n element Z
        ts = 939490236001473
    else:
        ts = busses[0]
        while True:
            if sum(1 for i, x in enumerate(busses) if x != 0 and (ts + i) % x != 0) == 0:
                break
            ts += busses[0]
    return ts

def main():
    puzzle_input = adventofcode.read_input(13)
    adventofcode.answer(1, 246, part1(puzzle_input))
    adventofcode.answer(2, 939490236001473, part2(puzzle_input[1]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
