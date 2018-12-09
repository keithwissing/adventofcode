#!/usr/bin/env python

import adventofcode

def part1(players, last_marble):
    """
    >>> part1(9, 25)
    32
    >>> part1(10, 1618)
    8317
    """
    score = [0] * players
    circle = [0, 2, 1]
    pos = 1
    marble = 3
    player = 1
    while marble <= last_marble:
        if marble % 23 == 0:
            score[player] += marble
            pos = (pos - 7 + len(circle)) % len(circle)
            score[player] += circle[pos]
            del circle[pos]
        else:
            pos = (pos + 2) % len(circle)
            circle.insert(pos, marble)
        player = (player + 1) % players
        marble += 1
    return max(score)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Circle(object):
    def __init__(self):
        n0 = Node(0)
        n1 = Node(1)
        n2 = Node(2)
        n0.next = n2
        n0.prev = n1
        n2.next = n1
        n2.prev = n0
        n1.next = n0
        n1.prev = n2
        self.node0 = n0
        self.current = n2
    def insert(self, marble):
        n = Node(marble)
        self.current = self.current.next
        n.next = self.current.next
        n.prev = self.current
        self.current.next.prev = n
        self.current.next = n
        self.current = n
    def remove(self):
        for _ in range(7):
            self.current = self.current.prev
        marble = self.current.val
        self.current.next.prev = self.current.prev
        self.current.prev.next = self.current.next
        self.current = self.current.next
        return marble

def part2(players, last_marble):
    """
    >>> part2(9, 25)
    32
    >>> part2(10, 1618)
    8317
    """
    circle = Circle()
    score = [0] * players
    marble = 3
    player = 1
    while marble <= last_marble:
        if marble % 23 == 0:
            score[player] += marble
            score[player] += circle.remove()
        else:
            circle.insert(marble)
        player = (player + 1) % players
        marble += 1
    if marble % 10000 == 0:
        print marble, '<', last_marble
    return max(score)

def main():
    puzzle_input = adventofcode.read_input(9)
    puzzle_input = puzzle_input.split()
    (players, last_marble) = (int(puzzle_input[0]), int(puzzle_input[6]))
    adventofcode.answer(1, 380705, part1(players, last_marble))
    adventofcode.answer(2, 3171801582, part2(players, last_marble * 100))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
