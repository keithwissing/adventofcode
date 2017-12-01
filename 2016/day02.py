#!/usr/bin/env python

pin_dict_x = { 'U': 0, 'D' : 0, 'L': -1, 'R': 1 }
pin_dict_y = { 'U': -1, 'D' : 1, 'L': 0, 'R': 0 }

def restrict(val, low, high):
    if val < low:
        return low
    if val > high:
        return high
    return val

def find_pin(puzzle_input):
    """
    >>> find_pin(["ULL","RRDDD","LURDL","UUUUD"])
    1985
    """
    posx = posy = 1
    pin = 0
    for row in puzzle_input:
        for step in row:
            posx = restrict(posx + pin_dict_x[step], 0, 2)
            posy = restrict(posy + pin_dict_y[step], 0, 2)
        pin = pin * 10 + (posx + 1 + posy * 3)
    return pin

normal_keypad = ["123","456","789"]
keypad = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]

def find_key(key, pad):
    for y in range(len(pad)):
        for x in range(len(pad[y])):
            if pad[y][x] == key:
                return (x,y)
    return (-1,-1)

def funny_keypad_pin(puzzle_input, pad):
    """
    >>> funny_keypad_pin(["ULL","RRDDD","LURDL","UUUUD"], ["123", "456", "789"])
    '1985'
    >>> funny_keypad_pin(["ULL","RRDDD","LURDL","UUUUD"], ["  1  ", " 234 ", "56789", " ABC ", "  D  "])
    '5DB3'
    """
    pin = ''
    pos = find_key('5', pad)
    for row in puzzle_input:
        for step in row:
            posy = restrict(pos[1] + pin_dict_y[step], 0, len(pad)-1)
            posx = restrict(pos[0] + pin_dict_x[step], 0, len(pad[posy])-1)
            key = pad[posy][posx]
            if key != ' ':
                pos = (posx,posy)
        pin = pin + pad[pos[1]][pos[0]]
    return pin

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day02_input.txt")]
    print "Part 1 Answer", find_pin(puzzle_input)
    print "Part 1 Answer", funny_keypad_pin(puzzle_input, normal_keypad)
    print "Part 2 Answer", funny_keypad_pin(puzzle_input, keypad)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

