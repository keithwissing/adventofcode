#!/usr/bin/env python

import adventofcode

def parse_move(move):
    if move[0] == 's':
        return ('s', int(move[1:]))
    if move[0] == 'x':
        args = [int(x) for x in move[1:].split('/')]
        return ('x', args[0], args[1])
    if move[0] == 'p':
        args = move[1:].split('/')
        return ('p', args[0], args[1])
    print move
    raise "error"

def parse_input_line(line):
    """
    >>> parse_input_line("s1,x3/4,pe/b")
    [('s', 1), ('x', 3, 4), ('p', 'e', 'b')]
    """
    moves = [parse_move(x) for x in line.split(",")]
    return moves

def part1(size, moves):
    """
    >>> part1(5, parse_input_line("s1,x3/4,pe/b"))
    'baedc'
    >>> part1(5, parse_input_line("s3"))
    'cdeab'
    >>> part1(5, parse_input_line("pa/e"))
    'ebcda'
    >>> part1(5, parse_input_line("x1/4"))
    'aecdb'
    >>> part1(16, parse_input_line("pe/m,s8,x5/12,pp/k,s15"))
    'jplemokabcdnfghi'
    """
    group = [chr(97+x) for x in range(size)]
    group = dance(group, moves)
    return "".join(group)

def dance(group, moves):
    for move in moves:
        if move[0] == "s":
            arg0 = move[1]
            #group = group[arg0-len(group):] + group[:arg0] # rotate the wrong direction
            group = group[-arg0:] + group[:len(group)-arg0] # the right direction
        elif move[0] == "x":
            echange = group[move[1]]
            group[move[1]] = group[move[2]]
            group[move[2]] = echange
        elif move[0] == "p":
            first = group.index(move[1])
            second = group.index(move[2])
            group[first] = move[2]
            group[second] = move[1]
        else:
            raise "error"
    return group

def part2(size, moves):
    return part2var(size, moves, 1000000000)

def part2var(size, moves, iterations):
    """
    >>> part2var(5, parse_input_line("s1,x3/4,pe/b"), 2)
    'ceadb'
    """
    group = [chr(97+x) for x in range(size)]
    cache = {}
    step = 0
    first = True
    while step < iterations:
        key = "".join(group)
        if key not in cache:
            cache[key] = dance(group, moves)
        elif first:
            first = False
            step += step * ((iterations / step) - 1)
        step += 1
        group = cache[key][:]
    return "".join(group)

def main():
    puzzle_input = adventofcode.read_input(16)
    moves = parse_input_line(puzzle_input)
    adventofcode.answer(1, 'nlciboghjmfdapek', part1(16, moves))
    adventofcode.answer(2, 'nlciboghmkedpfja', part2(16, moves))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
