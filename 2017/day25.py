#!/usr/bin/env python

import adventofcode

def parse_input_lines(lines):
    """
    >>> part1(parse_input_lines([ \
        "Begin in state A.", \
        "Perform a diagnostic checksum after 6 steps.", \
        "", \
        "In state A:", \
        "  If the current value is 0:", \
        "    - Write the value 1.", \
        "    - Move one slot to the right.", \
        "    - Continue with state B.", \
        "  If the current value is 1:", \
        "    - Write the value 0.", \
        "    - Move one slot to the left.", \
        "    - Continue with state B.", \
        "", \
        "In state B:", \
        "  If the current value is 0:", \
        "    - Write the value 1.", \
        "    - Move one slot to the left.", \
        "    - Continue with state A.", \
        "  If the current value is 1:", \
        "    - Write the value 1.", \
        "    - Move one slot to the right.", \
        "    - Continue with state A.",]))
    3

    ('A', 6, {'A': [(1, 'r', 'B'), (0, 'l', 'B')], 'B': [(1, 'l', 'A'), (1, 'r', 'A')]})
    """
    begin = lines[0].split("state ")[1][0]
    steps = int(lines[1].split()[5])
    states = {}
    for rowidx in range(2, len(lines), 10):
        state_lines = lines[rowidx:rowidx+10]
        current = state_lines[1].split("state ")[1][0]
        states[current] = parse_state_conditions(state_lines)
    return (begin, steps, states)

def parse_state_conditions(lines):
    return [parse_input_condition(lines[x:x+3]) for x in [3, 7]]

def parse_input_condition(lines):
    """
    >>> parse_input_condition([ \
        "    - Write the value 1.", \
        "    - Move one slot to the right.", \
        "    - Continue with state B.",])
    (1, 'r', 'B')
    """
    write = int(lines[0].split("value")[1].strip('.'))
    move = lines[1].split("the")[1][1]
    state = lines[2].split("state")[1][1]
    return (write, move, state)

class Tape(object):
    def __init__(self):
        self.state = {}
        self.position = 0

    def move(self, direction):
        self.position += 1 if direction == 'r' else -1

    def read(self):
        return self.state.get(self.position, 0)

    def write(self, value):
        if value:
            self.state[self.position] = value
        elif self.state.get(self.position):
            del self.state[self.position]

    def count_ones(self):
        return len(self.state)

def iterate(tape, state, blueprint):
    instr = blueprint[2][state]
    (write, move, nxt) = instr[tape.read()]
    tape.write(write)
    tape.move(move)
    return (tape, nxt)

def part1(blueprint):
    tape = Tape()
    state = blueprint[0]
    for _ in range(blueprint[1]):
        (tape, state) = iterate(tape, state, blueprint)
    return tape.count_ones()

def main():
    puzzle_input = adventofcode.read_input(25)
    blueprint = parse_input_lines(puzzle_input)
    adventofcode.answer(1, 4769, part1(blueprint))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
