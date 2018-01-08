#!/usr/bin/env python

import adventofcode

def parse_input_line(line):
    """
    >>> parse_input_line("50/39")
    [50, 39]
    """
    return [int(x) for x in line.split("/")]

# Eww, globals. Got the job done for now, and this isn't production code.

def is_it_stronger(bridge):
    global strongest
    str = sum(bridge)
    strongest = max(str, strongest)

def is_it_longer_stronger(bridge):
    global strongest
    global length
    if len(bridge) > length:
        length = len(bridge)
        strongest = sum(bridge)
    elif len(bridge) == length:
        str = sum(bridge)
        strongest = max(str, strongest)

def find_link_fit(bridge, seek, components, found_proc):
    candidates = [x for x in components if seek in x]
    if not candidates:
        found_proc(bridge)
    else:
        for tuck in candidates:
            other = tuck[0] if tuck[1] == seek else tuck[1]
            remaining = components[:]
            remaining.remove(tuck)
            find_link_fit(bridge + tuck, other, remaining, found_proc)

def part1(components):
    """
    >>> part1([[0, 2], [2, 2], [2, 3], [3, 4], [3, 5], [0, 1], [10, 1], [9, 10]])
    31
    """
    global strongest
    strongest = 0
    find_link_fit([], 0, components, is_it_stronger)
    return strongest

def part2(components):
    global strongest
    global length
    (strongest, length) = (0, 0)
    find_link_fit([], 0, components, is_it_longer_stronger)
    return strongest

def main():
    puzzle_input = adventofcode.read_input(24)
    components = [parse_input_line(x) for x in puzzle_input]
    adventofcode.answer(1, 1859, part1(components))
    adventofcode.answer(2, 1799, part2(components))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
