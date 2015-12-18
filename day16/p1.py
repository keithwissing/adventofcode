#!/usr/bin/env python

def parse(line):
    """
    >>> parse("Sue 1: goldfish: 9, cars: 0, samoyeds: 9")
    {'goldfish': 9, 'cars': 0, 'samoyeds': 9}
    """
    words = line.split()
    retval = {}
    for x in [2, 4, 6]:
        retval[words[x][:-1]] = int(words[x+1].strip(','))
    return retval

def ticker_tape():
    tape = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    return tape

def does_it_match(line, tape):
    for clue in tape:
        if clue in line:
            find = clue+': '+str(tape[clue])
            if find not in line:
                return False
    return True

def broken_machine_match(line, tape):
    for clue in tape:
        known = parse(line)
        if clue in known:
            if clue in ['cats', 'trees']:
                if known[clue] <= tape[clue]:
                    return False
            elif clue in ['pomeranians', 'goldfish']:
                if known[clue] >= tape[clue]:
                    return False
            else:
                if known[clue] != tape[clue]:
                    return False
    return True

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    tape = ticker_tape()
    for line in puzzle_input:
        if does_it_match(line, tape):
            print 'Thought it was', line
        if broken_machine_match(line, tape):
            print 'Real', line

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

