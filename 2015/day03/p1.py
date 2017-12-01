#!/usr/bin/env python

class Santa(object):
    def __init__(self):
        self.state = {(0, 0) : 1}
        self.posx = 0
        self.posy = 0

    def move(self, char):
        if char == '<': self.posx = self.posx - 1
        elif char == '>': self.posx = self.posx + 1
        elif char == '^': self.posy = self.posy + 1
        elif char == 'v': self.posy = self.posy - 1
        else: return False
        pos = (self.posx, self.posy)
        self.state[pos] = self.state.get(pos, 0) + 1
        return True

def year1(puzzle_input):
    """
    >>> year1(">")
    2
    >>> year1("^>v<")
    4
    >>> year1("^v^v^v^v^v")
    2
    """
    santa = Santa()
    for char in puzzle_input:
        santa.move(char)
    print len(santa.state)

def year2(puzzle_input):
    """
    >>> year2("^v")
    3
    >>> year2("^>v<")
    3
    >>> year2("^v^v^v^v^v")
    11
    """
    santa2 = Santa()
    robo = Santa()
    real = True
    for char in puzzle_input:
        if real:
            real = real ^ santa2.move(char)
        else:
            real = real ^ robo.move(char)
    total = {k: santa2.state.get(k, 0)+robo.state.get(k, 0) for k in santa2.state.viewkeys() | robo.state.viewkeys()}
    print len(total)

def main():
    puzzle_input = open("input.txt").read()
    year1(puzzle_input)
    year2(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

