#!/usr/bin/env python

state = {}

def has_signal(wire):
    return wire.isdigit() or wire in state.keys()

def set_signal(wire,signal):
    state[wire] = signal

def get_signal(wire):
    if wire.isdigit():
        return int(wire)
    else:
        return state[wire]

def once_through(lines):
    for line in lines:
        [left,right] = line.split(" -> ")
        if not has_signal(right):
            tokens = left.split()
            if len(tokens) == 1: # assignment
                if has_signal(tokens[0]):
                    state[right] = get_signal(tokens[0])
            elif len(tokens) == 2: # NOT
                if has_signal(tokens[1]):
                    state[right] = ( ~ get_signal(tokens[1]) ) & 0xffff
            else:
                if tokens[1] == "AND":
                    if has_signal(tokens[0]) and has_signal(tokens[2]):
                        state[right] = get_signal(tokens[0]) & get_signal(tokens[2])
                if tokens[1] == "OR":
                    if has_signal(tokens[0]) and has_signal(tokens[2]):
                        state[right] = get_signal(tokens[0]) | get_signal(tokens[2])
                if tokens[1] == "LSHIFT":
                    if has_signal(tokens[0]):
                        state[right] = ( get_signal(tokens[0]) << int(tokens[2]) ) & 0xffff
                if tokens[1] == "RSHIFT":
                    if has_signal(tokens[0]):
                        state[right] = ( get_signal(tokens[0]) >> int(tokens[2]) ) & 0xffff

def run(lines):
    last = -1
    while len(state) > last:
        last = len(state)
        once_through(lines)

def run_and_print_all(lines):
    """
    >>> run_and_print_all( [\
        "123 -> x",\
        "456 -> y",\
        "x AND y -> d",\
        "x OR y -> e",\
        "x LSHIFT 2 -> f",\
        "y RSHIFT 2 -> g",\
        "NOT x -> h",\
        "NOT y -> i" ] )
    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456
    """
    run(lines)

    wires = state.keys()
    wires.sort()
    for wire in wires:
        print "%s: %d" % (wire, state[wire])

def main():
    global state

    input = [line.strip() for line in open('input.txt')]

    state = {}
    run(input)
    print state['a']

    state = { 'b' : state['a'] }
    run(input)
    print state['a']

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

