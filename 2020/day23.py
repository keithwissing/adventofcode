#!/usr/bin/env python3

# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque
import adventofcode

def iteratelist(cups):
    cc = len(cups)
    pick = cups[1:4]
    pulled = cups[:1] + cups[4:]
    dest = (cups[0] - 2) % cc + 1
    while dest not in pulled:
        dest = (dest - 2) % cc + 1
    # print(pick, pulled, dest)
    idx = (pulled.index(dest) + 1) % cc
    rep = pulled[:idx] + pick + pulled[idx:]
    return rep[1:] + rep[:1]

def iteratedeque(cups):
    cc = len(cups)
    current = cups.popleft()
    cups.append(current)
    pick = [cups.popleft() for _ in range(3)]
    dest = (current - 2) % cc + 1
    while dest in pick:
        dest = (dest - 2) % cc + 1
    # print(pick, list(cups), dest)
    idx = cups.index(dest) + 1
    cups.insert(idx, pick[0])
    cups.insert(idx + 1, pick[1])
    cups.insert(idx + 2, pick[2])
    return cups

def qf(cups, pos):
    a = []
    for _ in range(9):
        a.append(str(pos))
        pos = cups[pos][1]
    return ' '.join(a)

def iterate_dict(cups, current, cc):
    i = current
    pick = [i := cups[i] for _ in range(3)]
    cups[current] = cups[pick[2]]
    dest = (current - 2) % cc + 1
    while dest in pick:
        dest = (dest - 2) % cc + 1
    t = cups[dest]
    cups[dest] = pick[0]
    cups[pick[2]] = t
    return cups[current]

def part1_dict(lines, rounds):
    """
    >>> part1_dict('389125467', 10)
    92658374
    >>> part1_dict('389125467', 100)
    67384529
    """
    inp = [int(x) for x in lines]
    cups = {}
    for i, v in enumerate(inp):
        cups[v] = inp[(i + 1) % len(inp)]
    current = inp[0]
    for _ in range(rounds):
        current = iterate_dict(cups, current, len(inp))
    a = []
    pos = 1
    for _ in range(8):
        pos = cups[pos]
        a.append(str(pos))
    return int(''.join(a))

def part2_dict(lines, pad, rounds):
    """
    # >>> part2_dict('389125467', 1000000, 10000000)
    # 149245887792
    """
    inp = [int(x) for x in lines]
    cups = {}
    for i, v in enumerate(inp):
        cups[v] = inp[(i + 1) % len(inp)]
    cups[inp[-1]] = len(inp)
    for v in range(len(inp), pad):
        cups[v] = v + 1
    cups[pad] = inp[0]

    print(len(cups), len(cups) == pad)

    current = inp[0]
    for r in range(rounds):
        if r % 100000 == 0:
            print(r, current)
        current = iterate_dict(cups, current, len(inp))

    a = []
    pos = 1
    for _ in range(2):
        pos = cups[pos]
        a.append(pos)
    print(a)
    return a[0] * a[1]

def part1(lines, rounds):
    """
    >>> part1('389125467', 10)
    92658374
    >>> part1('389125467', 100)
    67384529
    """
    cupl = [int(x) for x in lines]
    cupd = deque(cupl)
    for _ in range(rounds):
        cupl = iteratelist(cupl)
        iteratedeque(cupd)

    idx = (cupl.index(1) + 1) % len(cupl)
    ansl = int(''.join(str(c) for c in cupl[idx:] + cupl[:idx - 1]))

    idx = cupd.index(1)
    cupd.rotate(-idx)
    ansd = int(''.join(str(x) for x in list(cupd)[1:]))

    assert ansl == ansd
    return ansl

def iterate_a(cups, current):
    cc = len(cups) - 1
    i = current
    pick = [i := cups[i] for _ in range(3)]
    cups[current] = cups[pick[2]]
    dest = (current - 2) % cc + 1
    while dest in pick:
        dest = (dest - 2) % cc + 1
    # print(pick, dest)
    t = cups[dest]
    cups[dest] = pick[0]
    cups[pick[2]] = t
    return cups[current]

def part1_a(lines, rounds):
    """
    >>> part1_a('389125467', 10)
    92658374
    >>> part1_a('389125467', 100)
    67384529
    """
    inp = [int(x) for x in lines]
    cups = [0] * (len(inp) + 1)
    for i, _ in enumerate(inp):
        cups[inp[i]] = inp[(i + 1) % len(inp)]

    current = inp[0]
    for _ in range(rounds):
        current = iterate_a(cups, current)
    a = []
    pos = 1
    for _ in range(8):
        pos = cups[pos]
        a.append(str(pos))
    return int(''.join(a))

def part2_a(lines, pad=1000000, rounds=10000000):
    """
    # >>> part2_dict('389125467', 1000000, 10000000)
    # 149245887792
    """
    inp = [int(x) for x in lines]
    cups = [x + 1 for x in range(pad + 1)]
    cups[0] = 0
    for i, _ in enumerate(inp):
        cups[inp[i]] = inp[(i + 1) % len(inp)]
    cups[inp[-1]] = len(inp) + 1
    cups[pad] = inp[0]

    current = inp[0]
    for _ in range(rounds):
        current = iterate_a(cups, current)

    a = []
    pos = 1
    for _ in range(2):
        pos = cups[pos]
        a.append(pos)
    return a[0] * a[1]

def main():
    puzzle_input = adventofcode.read_input(23)
    puzzle_input = '925176834'
    adventofcode.answer(1, 69852437, part1(puzzle_input, 100))
    adventofcode.answer(1, 69852437, part1_dict(puzzle_input, 100))
    adventofcode.answer(1, 69852437, part1_a(puzzle_input, 100))
    adventofcode.answer(2, 91408386135, part2_a(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
