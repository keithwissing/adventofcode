#!/usr/bin/env python

def move_steps(puzzle_input):
    """
    >>> move_steps(1)
    0
    >>> move_steps(12)
    3
    >>> move_steps(23)
    2
    >>> move_steps(1024)
    31
    """
    puzzle_input = int(puzzle_input)
    result = 0
    if puzzle_input == 1:
        return 0
    l = 1
    while l**2 < puzzle_input:
        l += 2
    d = l**2 - puzzle_input
    return l/2 + abs((d % (l-1)) - l/2)

def main():
    puzzle_input = open("day03_input.txt").read().rstrip()
    print "Part 1 Answer", move_steps(puzzle_input)
    #print "Part 2 Answer", inverse_captcha_fun(puzzle_input, len(puzzle_input)/2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

