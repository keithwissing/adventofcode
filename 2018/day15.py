#!/usr/bin/env python

import itertools
import adventofcode

test_1 = [
    '#######',
    '#.G...#',
    '#...EG#',
    '#.#.#G#',
    '#..G#E#',
    '#.....#',
    '#######']
test_2 = [
    '#######',
    '#G..#E#',
    '#E#E.E#',
    '#G.##.#',
    '#...#E#',
    '#...E.#',
    '#######']
test_3 = [
    '#######',
    '#E..EG#',
    '#.#G.E#',
    '#E.##E#',
    '#G..#.#',
    '#..E#.#',
    '#######']
test_4 = [
    '#######',
    '#E.G#.#',
    '#.#G..#',
    '#G.#.G#',
    '#G..#.#',
    '#...E.#',
    '#######']
test_5 = [
    '#######',
    '#.E...#',
    '#.#..G#',
    '#.###.#',
    '#E#G#G#',
    '#...#G#',
    '#######']
test_6 = [
    '#########',
    '#G......#',
    '#.E.#...#',
    '#..##..G#',
    '#...##..#',
    '#...#...#',
    '#.G...G.#',
    '#.....G.#',
    '#########']

def part1(puzzle_input):
    """
    >>> part1(test_1)
    27730
    >>> part1(test_2)
    36334
    >>> part1(test_3)
    39514
    >>> part1(test_4)
    27755
    >>> part1(test_5)
    28944
    >>> part1(test_6)
    18740
    """
    board = Board(puzzle_input, 3)
    return outcome_for_the_board(board, False)

def outcome_for_the_board(board, elves_must_live):
    turn = 0
    done = False
    while not done:
        if elves_must_live and board.has_an_elf_died():
            return -1
        turn_order = board.find_turn_order()
        for pn in turn_order:
            p = board.get_player_by_pn(pn)
            if p.hp <= 0:
                continue
            enemy_locations = board.get_locations_of_all_by_side(oppose(p.side))
            if not enemy_locations:
                done = True
                break
            adjacent = board.player_is_adjacent_to_enemy(pn)
            if not adjacent:
                enemy_locations = board.get_locations_of_all_by_side(oppose(p.side))
                if not enemy_locations:
                    break
                goals = [a for sl in [adjacents(l[0], l[1]) for l in enemy_locations] for a in sl]
                goals = [x for x in goals if board.current[x[1]][x[0]] == '.']
                goals = board.filter_to_reachable((p.x, p.y), goals)
                if goals:
                    goal = board.find_closest_goal((p.x, p.y), goals)
                    board.move_toward(pn, goal)
            adjacent = board.player_is_adjacent_to_enemy(pn)
            if adjacent:
                target = board.fewest_hitpoints(adjacent)
                board.attack(pn, target[0], target[1])
        if not done:
            turn += 1
    #print turn
    #board.display()
    return board.hitpoints_remaining() * turn

class Player(object):
    def __init__(self, pn, side, x, y, elf_power):
        self.pn = pn
        self.side = side
        self.x = x
        self.y = y
        self.attack = 3 if side == 'G' else elf_power
        self.hp = 200

def oppose(side):
    return {'E':'G', 'G':'E'}[side]

def adjacents(x, y):
    return [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]

class Board(object):
    def __init__(self, puzzle_input, elf_power):
        self.current = [list(line) for line in puzzle_input]
        self.players = []
        count = 0
        for (x, y) in itertools.product(xrange(len(puzzle_input)), xrange(len(puzzle_input[0]))):
            square = puzzle_input[y][x]
            if square in 'EG':
                self.players.append(Player(count+1, square, x, y, elf_power))
                count += 1

    def display(self):
        for y, row in enumerate(self.current):
            print ' '.join(row),
            pir = []
            for p in self.players:
                if p.y == y and p.hp > 0:
                    pir.append((p.x, p.side, p.hp))
            pir.sort()
            for p in pir:
                print "%s(%d)" % (p[1], p[2]),
            print

    def has_an_elf_died(self):
        return True and [p for p in self.players if p.hp <= 0 and p.side == 'E']

    def find_turn_order(self):
        data = [(p.y, p.x, p.pn) for p in self.players if p.hp > 0]
        data.sort()
        return [p[2] for p in data]

    def get_player_by_pn(self, pn):
        return [p for p in self.players if p.pn == pn][0]

    def get_player_by_location(self, x, y):
        return [p for p in self.players if p.x == x and p.y == y and p.hp > 0][0]

    def get_locations_of_all_by_side(self, side):
        return [(p.x, p.y) for p in self.players if p.side == side and p.hp > 0]

    def player_is_adjacent_to_enemy(self, pn):
        p = self.get_player_by_pn(pn)
        enemy_locations = self.get_locations_of_all_by_side(oppose(p.side))
        adjacent = list(set(enemy_locations).intersection(set(adjacents(p.x, p.y))))
        return adjacent

    def fewest_hitpoints(self, adjacent):
        data = [(p.hp, p.y, p.x) for p in self.players if (p.x, p.y) in adjacent and p.hp > 0]
        data.sort()
        return (data[0][2], data[0][1])

    def attack(self, pn, x, y):
        p = self.get_player_by_pn(pn)
        e = self.get_player_by_location(x, y)
        e.hp -= p.attack
        if e.hp <= 0:
            self.current[e.y][e.x] = '.'

    def filter_to_reachable(self, pos, goals):
        reachable = self.find_all_reachable(pos)
        return list(set(reachable).intersection(set(goals)))

    def find_all_reachable(self, pos):
        reach = adjacents(pos[0], pos[1])
        reach = [t for t in reach if self.current[t[1]][t[0]] == '.']
        i = 0
        while i < len(reach):
            more = adjacents(reach[i][0], reach[i][1])
            for t in more:
                if t not in reach:
                    if self.current[t[1]][t[0]] == '.':
                        reach.append(t)
            i += 1
        return reach

    def find_closest_goal(self, pos, goals):
        grid = self.distances(pos)
        data = [(grid[l[1]][l[0]], l[1], l[0]) for l in goals if type(grid[l[1]][l[0]]) == int]
        data.sort()
        return (data[0][2], data[0][1])

    def move_toward(self, pn, goal):
        grid = self.distances(goal)
        p = self.get_player_by_pn(pn)
        adj = adjacents(p.x, p.y)
        adj = [(grid[l[1]][l[0]], l[1], l[0]) for l in adj if type(grid[l[1]][l[0]]) == int]
        adj.sort()
        step_to = (adj[0][2], adj[0][1])
        self.current[p.y][p.x] = '.'
        p.x = step_to[0]
        p.y = step_to[1]
        self.current[p.y][p.x] = p.side

    def distances(self, pos):
        grid = [row[:] for row in self.current]
        grid[pos[1]][pos[0]] = 0
        more = True
        while more:
            more = False
            for (x, y) in itertools.product(xrange(len(grid)), xrange(len(grid[0]))):
                if grid[y][x] == '.':
                    adj = adjacents(x, y)
                    adj = [grid[l[1]][l[0]] for l in adj if type(grid[l[1]][l[0]]) == int]
                    if adj:
                        grid[y][x] = min(adj)+1
                        more = True
        return grid

    def hitpoints_remaining(self):
        return sum([p.hp for p in self.players if p.hp > 0])

def part2(puzzle_input):
    """
    >>> part2(test_1)
    4988
    >>> part2(test_3)
    31284
    >>> part2(test_4)
    3478
    >>> part2(test_5)
    6474
    >>> part2(test_6)
    1140
    """
    elf_power = 3 if len(puzzle_input) < 30 else 23
    while True:
        elf_power += 1
        board = Board(puzzle_input, elf_power)
        outcome = outcome_for_the_board(board, True)
        if outcome == -1 or board.has_an_elf_died():
            #print "Failed at power", elf_power
            continue
        break
    return outcome

def main():
    puzzle_input = adventofcode.read_input(15)
    adventofcode.answer(1, 181952, part1(puzzle_input))
    adventofcode.answer(2, 47296, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
