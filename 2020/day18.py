#!/usr/bin/env python3

import adventofcode

def proc(line, start):
    """
    This was a really stupid way to do this
    """
    if line[start] == '(':
        tot, c = proc(line, start+1)
        pos = start + c + 2
    else:
        tot = int(line[start])
        pos = start+1
    while pos < len(line):
        op = line[pos]
        if op == ')':
            return (tot, pos - start)
        if line[pos+1] == '(':
            v, c = proc(line, pos + 2)
        else:
            v, c = int(line[pos+1]), -1
        if op == '+':
            tot += v
        if op == '*':
            tot *= v
        pos += c + 3
    return tot, pos - start

def calculate1(line):
    """
    >>> calculate1('1 + 2 * 3 + 4 * 5 + 6')
    71
    >>> calculate1('1 + (2 * 3) + (4 * (5 + 6))')
    51
    >>> calculate1('2 * 3 + (4 * 5)')
    26
    >>> calculate1('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    437
    >>> calculate1('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    12240
    >>> calculate1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    13632
    """
    line = line.replace(' ', '')
    v, _ = proc(line, 0)
    return v

def calculate2(line):
    """
    >>> calculate2('1 + 2 * 3 + 4 * 5 + 6')
    231
    >>> calculate2('1 + (2 * 3) + (4 * (5 + 6))')
    51
    >>> calculate2('2 * 3 + (4 * 5)')
    46
    >>> calculate2('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    1445
    >>> calculate2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    669060
    >>> calculate2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    23340

    Looked up and used algorithm from:
    https://en.wikipedia.org/wiki/Shunting-yard_algorithm#The_algorithm_in_detail
    """
    out = []
    op = []
    for t in line.replace(' ', ''):
        if t not in '+*()':
            out.append(t)
        elif t in '+*':
            while op and (t == '*' and op[-1] == '+') and op[-1] != '(':
                out.append(op.pop())
            op.append(t)
        elif t == '(':
            op.append(t)
        elif t == ')':
            while op[-1] != '(':
                out.append(op.pop())
            if op and op[-1] == '(':
                op.pop()
    while op:
        out.append(op.pop())
    stack = []
    while out:
        op = out.pop(0)
        if op == '+':
            stack.append(stack.pop() + stack.pop())
        elif op == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(op))
    return stack[0]

def part1(lines):
    tot = 0
    for line in lines:
        tot += calculate1(line)
    return tot

def part2(lines):
    tot = 0
    for line in lines:
        tot += calculate2(line)
    return tot

def main():
    puzzle_input = adventofcode.read_input(18)
    adventofcode.answer(1, 5783053349377, part1(puzzle_input))
    adventofcode.answer(2, 74821486966872, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
