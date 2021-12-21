#!/usr/bin/env python3

import heapq

import adventofcode

die = 0
def roll():
    global die
    v = die + 1
    die = (die + 1) % 100
    return v

def part1(lines):
    """
    >>> part1([4, 8])
    739785
    """
    global die
    die = 0
    pos = [lines[0] - 1, lines[1] - 1]
    scores = [0, 0]
    player = 1
    roll_count = 0
    while True:
        player = (player + 1) % 2

        rv = roll() + roll() + roll()
        roll_count += 3

        pos[player] = (pos[player] + rv) % 10
        scores[player] += pos[player] + 1

        if scores[player] >= 1000:
            break
    return min(scores) * roll_count

def part2(lines):
    """
    # >>> part2([4, 8])
    # 444356092776315
    """
    pos = [lines[0] - 1, lines[1] - 1]

    state = (1, lines[0] - 1, lines[1] - 1, 0, 0, 1)
    freq = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]

    wins = [0, 0]

    # count = 0
    q = [state]
    while q:
        state = heapq.heappop(q)
        # count += 1
        # if count % 100000 == 0:
        #     print(len(q))
        #     print(state)
        player = (state[5] + 1) % 2
        for rv in range(3, 10):
            s = list(state)
            s[0] *= freq[rv]
            s[player + 1] = (s[player + 1] + rv) % 10
            s[player + 3] += s[player + 1] + 1
            s[5] = player
            if s[player + 3] >= 21:
                wins[player] += s[0]
            else:
                heapq.heappush(q, tuple(s))
    return max(wins)

def main():
    puzzle_input = adventofcode.read_input(21)
    adventofcode.answer(1, 604998, part1([1, 6]))
    adventofcode.answer(2, 157253621231420, part2([1, 6]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
