#!/usr/bin/env python

def inverse_captcha(puzzle_input):
    """
    >>> inverse_captcha("1122")
    3
    >>> inverse_captcha("1111")
    4
    >>> inverse_captcha("1234")
    0
    >>> inverse_captcha("91212129")
    9
    """
    result = 0
    circle = puzzle_input[:]+puzzle_input[0]
    for x in range(0,len(circle)-1):
        if circle[x] == circle[x+1]:
            result = result + int(circle[x])
    return result

def inverse_captcha_skip(puzzle_input, skip):
    """
    >>> inverse_captcha_skip("1122", 1)
    3
    >>> inverse_captcha_skip("1111", 1)
    4
    >>> inverse_captcha_skip("1234", 1)
    0
    >>> inverse_captcha_skip("91212129", 1)
    9
    >>> inverse_captcha_skip("1212", 2)
    6
    >>> inverse_captcha_skip("1221", 2)
    0
    >>> inverse_captcha_skip("123425", 3)
    4
    >>> inverse_captcha_skip("123123", 3)
    12
    >>> inverse_captcha_skip("12131415", 4)
    4
    """
    result = 0
    for x in range(0,len(puzzle_input)):
        if puzzle_input[x] == puzzle_input[(x+skip)%len(puzzle_input)]:
            result = result + int(puzzle_input[x])
    return result

def inverse_captcha_fun(puzzle_input, skip):
    return sum([int(x) for i,x in enumerate(puzzle_input[:]) if x == puzzle_input[(i+skip)%len(puzzle_input)]])

def main():
    puzzle_input = open("day01_input.txt").read().rstrip()
    print "Part 1 Answer", inverse_captcha(puzzle_input)
    print "Part 1 Answer", inverse_captcha_skip(puzzle_input, 1)
    print "Part 1 Answer", inverse_captcha_fun(puzzle_input, 1)
    print "Part 2 Answer", inverse_captcha_skip(puzzle_input, len(puzzle_input)/2)
    print "Part 2 Answer", inverse_captcha_fun(puzzle_input, len(puzzle_input)/2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

