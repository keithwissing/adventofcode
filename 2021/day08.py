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

def sort_leters_in_words(words):
    """
    >>> sort_leters_in_words(['zma', 'alphabet'])
    ['amz', 'aabehlpt']
    """
    for i, v in enumerate(words):
        t = [c for c in v]
        t.sort()
        words[i] = ''.join(t)
    return words

def all_in(src, dst):
    """
    >>> all_in('abeg', 'abcdefg')
    True
    >>> all_in('abcdefg', 'abeg')
    False
    """
    return all([x in list(dst) for x in list(src)])

def i_of_len(pre, l):
    return [i for i, x in enumerate(pre) if len(x) == l]

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
    pre = sort_leters_in_words(pre.split())
    post = sort_leters_in_words(post.split())
    match = [None] * 10

    # find the digits that can only be one value based on length
    for l, v in [(2, 1), (4, 4), (3, 7), (7, 8)]:
        i = i_of_len(pre, l)[0]
        match[i] = v
    known_1 = pre[match.index(1)]

    # 3 is the only 5 segment number with all the segments in 1
    for i in i_of_len(pre, 5):
        if all_in(known_1, pre[i]):
            match[i] = 3
    known_3 = pre[match.index(3)]

    for i in i_of_len(pre, 6):
        if not all_in(known_1, pre[i]):
            match[i] = 6
        elif all_in(known_3, pre[i]):
            match[i] = 9
        else:
            match[i] = 0
    known_9 = pre[match.index(9)]

    for i in i_of_len(pre, 5):
        if not match[i]:
            if all_in(pre[i], known_9):
                match[i] = 5
            else:
                match[i] = 2

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
