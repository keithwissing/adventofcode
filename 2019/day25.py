#!/usr/bin/env python3

import adventofcode
from intcomputer import IntComputer

instr = """
south
take monolith
east
take asterisk
west
north
west
take coin
north
east
take astronaut ice cream
west
south
east
north
north
take mutex
west
take astrolabe
west
take dehydrated water
west
take wreath
east
south
east
north
north
inv
drop astronaut ice cream
drop coin
drop dehydrated water
drop mutex
north
"""

# take wreath
# take asterisk
# take monolith
# take astrolabe

items = [
    'astronaut ice cream',
    'wreath',
    'coin',
    'dehydrated water',
    'asterisk',
    'monolith',
    'astrolabe',
    'mutex',
]

def drop_all():
    c = ['drop '+i+'\n' for i in items]
    c = ''.join(c)
    return [ord(x) for x in c]

def pu(nv):
    ss = bin(nv)[2:].zfill(8)
    cmd = ''
    for n, v in enumerate(ss):
        if v == '1':
            cmd += 'take '+items[n]+'\n'
    return [ord(x) for x in cmd]

def part1(program):
    comp = IntComputer(program)
    out = comp.run_until_prompt([ord(x) for x in instr])
    print(''.join([chr(x) for x in out]))
    nv = 77
    while True:
        cmd = input('?')
        if cmd == 'da':
            inp = drop_all()
        elif cmd == 'p':
            nv += 1
            print(f'Trying combo {nv}')
            inp = drop_all()
            inp.extend(pu(nv))
            inp.extend([ord(x) for x in 'north\n'])
        else:
            inp = [ord(c) for c in cmd+'\n']
        print(inp)
        out = comp.run_until_prompt(inp)
        print(''.join([chr(x) for x in out]))

def main():
    puzzle_input = adventofcode.read_input(25)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 2155873288, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
