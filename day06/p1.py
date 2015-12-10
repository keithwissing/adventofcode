#!/usr/bin/env python

def p1ton(old):
    return 1

def p1toff(old):
    return 0

def p1toggle(old):
    return 1-old

def p2ton(old):
    return old + 1

def p2toff(old):
    return max(old - 1, 0)

def p2toggle(old):
    return old + 2

class Lights():
    def __init__(self):
        self.board = [[0 for x in range(1000)] for x in range(1000)]
        #self.functions = { 'on' : p1ton, 'off' : p1toff, 'toggle' : p1toggle }
        self.functions = {'on' : p2ton, 'off' : p2toff, 'toggle' : p2toggle}

    def get_count(self):
        rowcs = [sum(r) for r in self.board]
        return sum(rowcs)

    def over(self, x1, y1, x2, y2, func):
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                self.board[x][y] = func(self.board[x][y])

    def process(self, parts):
        func = self.functions[parts[0]]
        self.over(parts[1][0], parts[1][1], parts[2][0], parts[2][1], func)

def parse_coordinate(puzzle_input):
    return [int(v) for v in puzzle_input.split(',')]

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    display = Lights()
    for line in puzzle_input:
        parts = line.split()
        if len(parts) == 5:
            parts = parts[1:]
        parts = [parts[0], parse_coordinate(parts[1]), parse_coordinate(parts[3])]
        print parts
        display.process(parts)
    print display.get_count()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

