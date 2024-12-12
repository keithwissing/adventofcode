#!/usr/bin/env python3
import functools

import adventofcode

t1 = '125 17'

def blink(line):
    ret = []
    for v in line:
        if v == 0:
            ret.append(1)
        elif len(str(v)) % 2 == 0:
            sv = str(v)
            ret.append(int(sv[:len(sv) // 2]))
            ret.append(int(sv[len(sv) // 2:]))
        else:
            ret.append(v * 2024)
    return ret

def part1(line):
    """
    >>> part1(t1)
    55312
    """
    line = [int(x) for x in line.split()]
    for _ in range(25):
        line = blink(line)
    return len(line)

@functools.cache
def nblink(v, n):
    if n == 0:
        return 1
    elif v == 0:
        return nblink(1, n - 1)
    elif len(str(v)) % 2 == 0:
        sv = str(v)
        return nblink(int(sv[:len(sv) // 2]), n - 1) + nblink(int(sv[len(sv) // 2:]), n - 1)
    else:
        return nblink(v * 2024, n - 1)

def part2(line):
    """
    >>> part2(t1)
    65601038650482
    """
    return sum(nblink(int(v), 75) for v in line.split())

def main():
    puzzle_input = adventofcode.read_input(11)
    adventofcode.answer(1, 197157, part1(puzzle_input))
    adventofcode.answer(2, 234430066982597, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
