#!/usr/bin/env python

def reverse_op(data, pos, length):
    """
    >>> reverse_op([0, 1, 2, 3, 4], 0, 3)
    [2, 1, 0, 3, 4]
    >>> reverse_op([0, 1, 2, 3, 4], 3, 4)
    [4, 3, 2, 1, 0]
    >>> reverse_op([0, 1, 2, 3, 4, 5], 3, 4)
    [3, 1, 2, 0, 5, 4]
    """
    if pos+length < len(data):
        return data[:pos] + list(reversed(data[pos:pos+length])) + data[pos+length:]
    retval = data[:]
    for step in range(length):
        retval[(pos+step)%len(data)] = data[(pos+length-step-1)%len(data)]
    return retval

def run_sequence(size, sequence):
    """
    >>> run_sequence(5, "3,4,1,5")
    [3, 4, 2, 1, 0]
    """
    (data, _, _) = run_sequence_once(range(size), 0, 0, [int(x) for x in sequence.split(",")])
    return data

def run_sequence_once(data, pos, skip, sequence):
    for n in sequence:
        data = reverse_op(data, pos, n)
        pos = (pos + n + skip) % len(data)
        skip += 1
    return (data, pos, skip)

def run_sequence_loop(size, sequence):
    data = range(size)
    pos = 0
    skip = 0
    for _ in range(64):
        (data, pos, skip) = run_sequence_once(data, pos, skip, sequence)
    return data

def part1(size, sequence):
    """
    >>> part1(5, "3,4,1,5")
    12
    """
    data = run_sequence(size, sequence)
    return data[0] * data[1]

def input_to_sequence(puzzle_input):
    return [ord(x) for x in puzzle_input] + [17, 31, 73, 47, 23]

def sparse_to_dense(data):
    return [reduce(lambda x, y: x^y, data[pos*16:pos*16+16]) for pos in range(16)]

def dense_to_hex(dense):
    return "".join(["%0.2x" % x for x in dense])

def part2(puzzle_input):
    """
    >>> part2("")
    'a2582a3a0e66e6e86e3812dcb672a272'
    >>> part2("AoC 2017")
    '33efeb34ea91902bb2f59c9920caa6cd'
    >>> part2("1,2,3")
    '3efbe78a8d82f29979031a4aa0b16a9d'
    """
    sequence = input_to_sequence(puzzle_input)
    data = run_sequence_loop(256, sequence)
    dense = sparse_to_dense(data)
    return dense_to_hex(dense)

def main():
    puzzle_input = open("day10_input.txt").read().rstrip()
    print "Part 1 Answer", part1(256, puzzle_input)
    print "Part 2 Answer", part2(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
