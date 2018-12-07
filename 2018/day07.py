#!/usr/bin/env python

import adventofcode

def part1(puzzle_input):
    """
    >>> part1([('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')])
    'CABDFE'
    """
    result = ""
    (reqs, todo) = build_requirements(puzzle_input)
    finished = set()
    while todo:
        ns = find_next_step(reqs, todo, finished)
        result += ns
        todo.remove(ns)
        finished.add(ns)
    return result

def part2(puzzle_input, workers, add_time):
    """
    >>> part2([('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')], 2, 0)
    15
    """
    (reqs, todo) = build_requirements(puzzle_input)
    finished = set()
    working = [None] * workers
    finish = [0] * workers
    now = 0
    while True:
        for i in range(workers):
            if working[i] != None and finish[i] <= now:
                finished.add(working[i])
                working[i] = None
                finish[i] = 0
        if not todo and working.count(None) == workers:
            return now
        while None in working:
            ns = find_next_step(reqs, todo, finished)
            if ns is None:
                break
            idx = working.index(None)
            working[idx] = ns
            finish[idx] = now + add_time + ord(ns) - ord('A') + 1
            todo.remove(ns)
        now += 1

def find_next_step(reqs, todo, finished):
    for t in todo:
        if not reqs.has_key(t):
            return t
        if reqs[t].issubset(finished):
            return t
    return None

def build_requirements(puzzle_input):
    reqs = dict()
    todo = set()
    for req in puzzle_input:
        if not reqs.has_key(req[1]):
            reqs[req[1]] = set()
        todo.add(req[0])
        todo.add(req[1])
        reqs[req[1]].add(req[0])
    todo = list(todo)
    todo.sort()
    return (reqs, todo)

def parse_line(line):
    return (line[5], line[36])

def main():
    puzzle_input = adventofcode.read_input(7)
    puzzle_input = map(parse_line, puzzle_input)
    adventofcode.answer(1, 'GKPTSLUXBIJMNCADFOVHEWYQRZ', part1(puzzle_input))
    adventofcode.answer(2, 920, part2(puzzle_input, 5, 60))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
