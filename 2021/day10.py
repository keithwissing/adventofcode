#!/usr/bin/env python3

import adventofcode

t1 = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]',
]

opens = '([{<'
closes = ')]}>'

def check(line):
    s = []
    first = -1
    misses = [0] * 4
    for c in line:
        if c in opens:
            s.append(c)
        if c in closes:
            m = s.pop()
            if opens.index(m) != closes.index(c):
                misses[closes.index(c)] += 1
                if first == -1:
                    first = closes.index(c)
    return s, first, misses

def part1(lines):
    """
    >>> part1(t1)
    26397
    """
    score = 0
    vals = [3, 57, 1197, 25137]
    for line in lines:
        _, first, misses = check(line)
        if first >= 0:
            score += misses[first] * vals[first]
    return score

def part2(lines):
    """
    >>> part2(t1)
    288957
    """
    scores = []
    for line in lines:
        s, first, _ = check(line)
        if first == -1:
            score = 0
            while s:
                c = s.pop()
                score *= 5
                score += opens.index(c) + 1
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]

def main():
    puzzle_input = adventofcode.read_input(10)
    adventofcode.answer(1, 296535, part1(puzzle_input))
    adventofcode.answer(2, 4245130838, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
