#!/usr/bin/env python3

import adventofcode

def part1_1(lines):
    """
    This implementation keeps the whole list in memory, therefore does not work for part 2.
    >>> part1_1('0,3,6')
    436
    """
    spoken = [int(x) for x in lines.split(',')]
    for _ in range(len(spoken), 2020):
        l = spoken[-1]
        hist = [i for i, x in enumerate(spoken) if x == l]
        if len(hist) < 2:
            spoken.append(0)
        else:
            spoken.append(hist[-1] - hist[-2])
    return spoken[-1]

def game(line, iterations):
    """
    This time, only keep track of the last time each number was spoken.
    It assumes there are no duplicate numbers in the starting numbers.
    """
    seed = [int(x) for x in line.split(',')]
    spoken = {x: i for i, x in enumerate(seed)}
    up = 0
    for t in range(len(spoken), iterations - 1):
        if up in spoken:
            age = t - spoken[up]
            spoken[up] = t
            up = age
        else:
            spoken[up] = t
            up = 0
    return up

def part1(lines):
    """
    >>> part1('0,3,6')
    436
    >>> part1('1,3,2')
    1
    >>> part1('2,1,3')
    10
    >>> part1('1,2,3')
    27
    """
    return game(lines, 2020)

def part2(lines):
    """
    # >>> part2('0,3,6')
    # 175594
    # >>> part2('1,3,2')
    # 2578
    # >>> part2('2,1,3')
    # 3544142
    # >>> part2('1,2,3')
    # 261214
    # >>> part2('2,3,1')
    # 6895259
    # >>> part2('3,2,1')
    # 18
    # >>> part2('3,1,2')
    # 362
    """
    return game(lines, 30000000)

def main():
    puzzle_input = adventofcode.read_input(15)
    # puzzle_input = '16,12,1,0,15,7,11'
    adventofcode.answer(1, 403, part1(puzzle_input))
    adventofcode.answer(2, 6823, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
