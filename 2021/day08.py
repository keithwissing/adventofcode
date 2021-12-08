#!/usr/bin/env python3

import adventofcode

t1 = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
]

def part1(lines):
    """
    >>> part1(t1)
    26
    """
    count = 0
    for line in lines:
        count += sum([1 for x in line.split('|')[1].split() if len(x) in [2, 4, 3, 7]])
    return count

def decode(line):
    """
    >>> decode('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf')
    5353
    >>> decode(t1[0])
    8394
    >>> decode(t1[1])
    9781
    """
    pre, post = line.split('|')
    pre = pre.split()
    for i, v in enumerate(pre):
        t = [c for c in v]
        t.sort()
        pre[i] = ''.join(t)
    post = post.split()
    for i, v in enumerate(post):
        t = [c for c in v]
        t.sort()
        post[i] = ''.join(t)
    match = [None] * 10
    oo = [i for i, x in enumerate(pre) if len(x) == 2][0]
    match[oo] = 1
    oo = [i for i, x in enumerate(pre) if len(x) == 4][0]
    match[oo] = 4
    oo = [i for i, x in enumerate(pre) if len(x) == 3][0]
    match[oo] = 7
    oo = [i for i, x in enumerate(pre) if len(x) == 7][0]
    match[oo] = 8
    for oo in [i for i, x in enumerate(pre) if len(x) == 5]:
        qq = match.index(1)
        if all([x in list(pre[oo]) for x in list(pre[qq])]):
            match[oo] = 3
    for oo in [i for i, x in enumerate(pre) if len(x) == 6]:
        qq = match.index(1)
        if not all([x in list(pre[oo]) for x in list(pre[qq])]):
            match[oo] = 6
        qq = match.index(3)
        if all([x in list(pre[oo]) for x in list(pre[qq])]):
            match[oo] = 9
        if not match[oo]:
            match[oo] = 0
    for oo in [i for i, x in enumerate(pre) if len(x) == 5]:
        if not match[oo]:
            qq = match.index(9)
            if all([x in list(pre[qq]) for x in list(pre[oo])]):
                match[oo] = 5
            else:
                match[oo] = 2
    v = 0
    for x in post:
        v *= 10
        v += match[pre.index(x)]
    return v

def part2(lines):
    """
    >>> part2(t1)
    61229
    """
    return sum([decode(x) for x in lines])

def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 445, part1(puzzle_input))
    adventofcode.answer(2, 1043101, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
