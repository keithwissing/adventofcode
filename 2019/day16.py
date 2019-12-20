#!/usr/bin/env python3

from itertools import cycle, chain, repeat, islice
import adventofcode

def pattern(p, l):
    """
    >>> list(pattern(1, 10))
    [1, 0, -1, 0, 1, 0, -1, 0, 1, 0]
    """
    pat = cycle(chain(repeat(0, p), repeat(1, p), repeat(0, p), repeat(-1, p)))
    next(pat)
    return islice(pat, l)

def ones(a):
    return a%10 if a >= 0 else -a%10

def phase(signal):
    """
    >>> phase('12345678')
    '48226158'
    """
    out = []
    for i, digit in enumerate(signal):
        out.append(str(ones(sum(int(a)*b for a, b in zip(signal, pattern(i+1, len(signal)))))))
    return ''.join(out)

def part1(signal):
    """
    >>> part1('80871224585914546619083218645595')
    '24176176'
    """
    for _ in range(100):
        signal = phase(signal)
    return signal[:8]

# def part2(signal):
#     """
#     # >>> part2('03036732577212944063491565474664')
#     # 84462026
#     """
#     off = int(signal[:7])
#     signal = signal * 10000
#     for _ in range(100):
#         signal = phase(signal)
#     return signal[off:off+8]

def main():
    puzzle_input = adventofcode.read_input(16)
    # puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, '53296082', part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
