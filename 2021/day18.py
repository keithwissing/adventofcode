#!/usr/bin/env python3

import json
import re
from itertools import permutations

import adventofcode

t1 = [
    '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
    '[[[5,[2,8]],4],[5,[[9,9],0]]]',
    '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
    '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
    '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
    '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
    '[[[[5,4],[7,7]],8],[[8,3],8]]',
    '[[9,3],[[9,9],[6,[4,9]]]]',
    '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
    '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]',
]

def magnitude(n):
    """
    >>> magnitude([9,1])
    29
    >>> magnitude([1,9])
    21
    >>> magnitude([[9,1],[1,9]])
    129
    >>> magnitude([[1,2],[[3,4],5]])
    143
    >>> magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]])
    1384
    >>> magnitude([[[[1,1],[2,2]],[3,3]],[4,4]])
    445
    >>> magnitude([[[[3,0],[5,3]],[4,4]],[5,5]])
    791
    >>> magnitude([[[[5,0],[7,4]],[5,5]],[6,6]])
    1137
    >>> magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])
    3488
    >>> magnitude('[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]')
    3993
    """
    if isinstance(n, str):
        n = json.loads(n)
    a = magnitude(n[0]) if isinstance(n[0], list) else n[0]
    b = magnitude(n[1]) if isinstance(n[1], list) else n[1]
    return 3 * a + 2 * b

def explode(sfn):
    """
    >>> explode('[[[[[9, 8], 1], 2], 3], 4]')
    '[[[[0, 9], 2], 3], 4]'
    >>> explode('[7, [6, [5, [4, [3, 2]]]]]')
    '[7, [6, [5, [7, 0]]]]'
    >>> explode('[[6,[5,[4,[3,2]]]],1]')
    '[[6, [5, [7, 0]]], 3]'
    >>> explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
    '[[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]'
    >>> explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
    '[[3, [2, [8, 0]]], [9, [5, [7, 0]]]]'
    """
    if isinstance(sfn, str):
        sfn = list(filter(None, re.split(r'([\[\]\,]|\d+)', sfn)))
        sfn = [c for c in sfn if c != ' ']

    depth = 0
    for i, v in enumerate(sfn):
        if v == '[':
            depth += 1
        if v == ']':
            depth -= 1
        if v.isdigit() and depth >= 5:
            b = sfn[i - 1:i + 4]
            l = int(b[1])
            r = int(b[3])
            for s in range(i - 1, 0, -1):
                if sfn[s].isdigit():
                    sfn[s] = str(int(sfn[s]) + l)
                    break
            for s in range(i + 4, len(sfn)):
                if sfn[s].isdigit():
                    sfn[s] = str(int(sfn[s]) + r)
                    break
            sfn = sfn[:i - 1] + ['0'] + sfn[i + 4:]
            break
    return ''.join(sfn).replace(',', ', ')

def split(sfn):
    """
    >>> split('[[[[0,7],4],[15,[0,13]]],[1,1]]')
    '[[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]'
    >>> split('[[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]')
    '[[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]'
    """
    if isinstance(sfn, str):
        sfn = list(filter(None, re.split(r'([\[\]\,]|\d+)', sfn)))
        sfn = [c for c in sfn if c != ' ']

    for i, v in enumerate(sfn):
        if v.isdigit() and int(v) >= 10:
            v = int(v)
            l = v // 2
            r = (v + 1) // 2
            sfn = sfn[:i] + ['[', str(l), ',', str(r), ']'] + sfn[i + 1:]
            break
    return ''.join(sfn).replace(',', ', ')

def reduce(sfn):
    """
    >>> reduce('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
    '[[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]'
    """
    while True:
        nn = explode(sfn)
        if nn != sfn:
            sfn = nn
        else:
            nn = split(sfn)
            if nn != sfn:
                sfn = nn
            else:
                break
    return sfn

def add(n1, n2):
    return f'[{n1}, {n2}]'

def part1(lines):
    """
    >>> part1(t1)
    4140
    """
    sfn = lines[0]
    for l in lines[1:]:
        sfn = add(sfn, l)
        sfn = reduce(sfn)
    return magnitude(sfn)

def part2(lines):
    """
    >>> part2(t1)
    3993
    """
    m = 0
    for a, b in permutations(lines, 2):
        t = magnitude(reduce(add(a, b)))
        if m < t:
            m = t
    return m

def main():
    puzzle_input = adventofcode.read_input(18)
    adventofcode.answer(1, 4457, part1(puzzle_input))
    adventofcode.answer(2, 4784, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
