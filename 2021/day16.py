#!/usr/bin/env python3

from functools import reduce
import adventofcode

def parse(ha, pos, limit=None):
    vt = 0
    vals = []
    count = 0
    while pos < len(ha) - 9 and (not limit or count < limit):
        version = int(ha[pos:pos + 3], 2)
        typeid = int(ha[pos + 3:pos + 6], 2)
        pos += 6
        vt += version
        count += 1
        if typeid == 4:  # literal
            a = []
            while True:
                n = ha[pos:pos + 5]
                pos += 5
                a += n[1:]
                if n[0] == '0':
                    break
            vals.append(int(''.join(a), 2))
        else:
            lengthType = ha[pos]
            pos += 1
            if lengthType == '0':
                total = int(ha[pos:pos + 15], 2)
                pos += 15
                sb = ha[pos:pos + total]
                pos += total
                p, v, t = parse(sb, 0)
                vt += t
            else:
                subs = int(ha[pos:pos + 11], 2)
                pos += 11
                p, v, t = parse(ha[pos:], 0, subs)
                pos += p
                vt += t
            if typeid == 0:  # sum
                vals.append(sum(v))
            elif typeid == 1:  # product
                vals.append(reduce(lambda x, y: x * y, v))
            elif typeid == 2:
                vals.append(min(v))
            elif typeid == 3:
                vals.append(max(v))
            elif typeid == 5:
                vals.append(1 if v[0] > v[1] else 0)
            elif typeid == 6:
                vals.append(1 if v[0] < v[1] else 0)
            elif typeid == 7:
                vals.append(1 if v[0] == v[1] else 0)
    return pos, vals, vt

def part1(lines):
    """
    >>> part1('8A004A801A8002F478')
    16
    >>> part1('620080001611562C8802118E34')
    12
    >>> part1('C0015000016115A2E0802F182340')
    23
    >>> part1('A0016C880162017C3686B18A3D4780')
    31
    """
    num_of_bits = len(lines) * 4
    ha = bin(int(lines, 16))[2:].zfill(num_of_bits)
    return parse(ha, 0)[2]

def part2(lines):
    """
    >>> part2('C200B40A82')
    3
    >>> part2('04005AC33890')
    54
    """
    num_of_bits = len(lines) * 4
    ha = bin(int(lines, 16))[2:].zfill(num_of_bits)
    return parse(ha, 0)[1][0]

def main():
    puzzle_input = adventofcode.read_input(16)
    adventofcode.answer(1, 977, part1(puzzle_input))
    adventofcode.answer(2, 101501020883, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
