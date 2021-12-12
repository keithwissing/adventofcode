#!/usr/bin/env python3

import adventofcode

t1 = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]

t2 = [
    'dc-end',
    'HN-start',
    'start-kj',
    'dc-start',
    'dc-HN',
    'LN-dc',
    'HN-end',
    'kj-sa',
    'kj-HN',
    'kj-dc',
]

def parse(lines):
    for line in lines:
        x = line.split('-')
        yield (x[0], x[1])
        yield (x[1], x[0])

def step(links, path, pos, paths):
    if pos == 'end':
        paths.add('|'.join(path))
        return
    ch = set([x[1] for x in links if x[0] == pos])
    for m in ch:
        if m.isupper() or m not in path:
            step(links, path[:] + [m], m, paths)

def step2(links, visits, twice, path, pos, paths):
    if pos == 'end':
        paths.add('|'.join(path))
        return
    ch = set([x[1] for x in links if x[0] == pos])
    for m in ch:
        if m not in visits:
            v = set(visits)
            if m.islower() and twice:
                v.add(m)
                step2(links, v, twice, path[:] + [m], m, paths)
            elif m.islower():
                step2(links, v, True, path[:] + [m], m, paths)
                v.add(m)
                step2(links, v, False, path[:] + [m], m, paths)
            else:
                step2(links, v, twice, path[:] + [m], m, paths)

def part1(lines):
    """
    >>> part1(t1)
    10
    >>> part1(t2)
    19
    """
    links = list(parse(lines))
    paths = set()
    step(links, ['start'], 'start', paths)
    return len(paths)

def part2(lines):
    """
    >>> part2(t1)
    36
    >>> part2(t2)
    103
    """
    links = list(parse(lines))
    paths = set()
    step2(links, set(['start']), False, ['start'], 'start', paths)
    return len(paths)

def main():
    puzzle_input = adventofcode.read_input(12)
    adventofcode.answer(1, 3495, part1(puzzle_input))
    adventofcode.answer(2, 94849, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
