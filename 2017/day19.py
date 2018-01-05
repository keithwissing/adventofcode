#!/usr/bin/env python

import adventofcode

def find_directions(lines, posx, posy):
    # should probably check for out of bounds coordinates, but this worked for my input
    dirs = []
    if lines[posy-1][posx] != ' ':
        dirs.append('n')
    if lines[posy+1][posx] != ' ':
        dirs.append('s')
    if lines[posy][posx-1] != ' ':
        dirs.append('w')
    if lines[posy][posx+1] != ' ':
        dirs.append('e')
    return dirs

opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

def part1(lines):
    (letters, _) = route_packet(lines)
    return letters

def part2(lines):
    (_, steps) = route_packet(lines)
    return steps

def route_packet(lines):
    posy = 0
    posx = lines[0].index("|")
    dir = 's'
    letters = []
    stepcount = 0
    while True:
        stepcount += 1
        posy += 1 if dir == 's' else -1 if dir == 'n' else 0
        posx += 1 if dir == 'e' else -1 if dir == 'w' else 0
        char = lines[posy][posx]
        if char == 'F':
            pass
        if char.isalpha():
            letters.append(char)
        elif char in ['|', '-']:
            pass
        elif char == ' ':
            break
        elif char == '+':
            dirs = find_directions(lines, posx, posy)
            dirs.remove(opposite[dir])
            dir = dirs[0]
    return ("".join(letters), stepcount)

def test1():
    """
    >>> test1()
    'ABCDEF'
    """
    lines = [
        '     |          ',
        '     |  +--+    ',
        '     A  |  C    ',
        ' F---|----E|--+ ',
        '     |  |  |  D ',
        '     +B-+  +--+ ',
        '                ']
    return part1(lines)

def main():
    lines = adventofcode.read_input(19)
    adventofcode.answer(1, 'GEPYAWTMLK', part1(lines))
    adventofcode.answer(2, 17628, part2(lines))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
