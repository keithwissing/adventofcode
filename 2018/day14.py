#!/usr/bin/env python

import adventofcode

def part1(puzzle_input):
    """
    >>> part1(9)
    5158916779
    """
    scores = [3, 7]
    elf = [0, 1]
    while len(scores) < puzzle_input + 10:
        nr = scores[elf[0]] + scores[elf[1]]
        if nr >= 10:
            scores.append(nr/10)
        scores.append(nr%10)
        elf[0] = (elf[0] + scores[elf[0]] + 1) % len(scores)
        elf[1] = (elf[1] + scores[elf[1]] + 1) % len(scores)
    return int(''.join([str(x) for x in scores[puzzle_input:puzzle_input+10]]))

def part2(puzzle_input):
    """
    >>> part2('51589')
    9
    >>> part2('01245')
    5
    >>> part2('92510')
    18
    >>> part2('59414')
    2018
    """
    scores = '37'
    elf = [0, 1]
    answer = 0
    while answer <= 0:
        nr = int(scores[elf[0]]) + int(scores[elf[1]])
        if nr >= 10:
            scores += str(nr/10)
        scores += str(nr%10)
        elf[0] = (elf[0] + int(scores[elf[0]]) + 1) % len(scores)
        elf[1] = (elf[1] + int(scores[elf[1]]) + 1) % len(scores)
        answer = scores.find(puzzle_input)
    return answer

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Board(object):
    def __init__(self):
        self.root = Node(3)
        self.root.next = Node(7)
        self.last = self.root.next
        self.find_pos = self.root
        self.answer = 0

    def advance(self, current):
        a = 1 + current.val
        for _ in range(a):
            current = current.next
            if not current:
                current = self.root
        return current

    def add_score(self, new_score):
        for x in str(new_score):
            self.last.next = Node(int(x))
            self.last = self.last.next

    def short_find(self, seeking):
        while True:
            comp = ''
            pos = self.find_pos
            for _ in range(len(seeking)):
                comp += str(pos.val)
                pos = pos.next
                if not pos:
                    break
            if len(comp) < len(seeking):
                break
            if comp == seeking:
                return self.answer
            self.find_pos = self.find_pos.next
            self.answer += 1
        return -1

def part2_2(puzzle_input):
    """
    >>> part2_2('51589')
    9
    >>> part2_2('01245')
    5
    >>> part2_2('92510')
    18
    >>> part2_2('59414')
    2018
    """
    scores = Board()
    elf = [scores.root, scores.root.next]
    answer = 0
    while answer <= 0:
        nr = elf[0].val + elf[1].val
        scores.add_score(nr)
        elf[0] = scores.advance(elf[0])
        elf[1] = scores.advance(elf[1])
        answer = scores.short_find(puzzle_input)
    return answer

def main():
    puzzle_input = adventofcode.read_input(14)
    adventofcode.answer(1, 1052903161, part1(int(puzzle_input)))
    adventofcode.answer(2, 20165504, part2_2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
