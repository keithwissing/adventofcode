#!/usr/bin/env python

face_dict = { 'R': 1, 'L': -1 }
x_dict = { 0: 0, 1: 1, 2: 0, 3: -1 }
y_dict = { 0: 1, 1: 0, 2: -1, 3: 0 }

def travel(start, move):
    (posx, posy, face) = start
    move = move.strip()
    turn = move[0]
    dist = int(move[1:])
    face = ( face + face_dict[turn] + 4 ) % 4
    posx = posx + x_dict[face] * dist
    posy = posy + y_dict[face] * dist
    return (posx, posy, face)

def shortest_distance(puzzle_input):
    """
    >>> shortest_distance("R2, L3")
    5
    >>> shortest_distance("R2, R2, R2")
    2
    >>> shortest_distance("R5, L5, R5, R3")
    12
    """
    posx = posy = face = 0
    for s in puzzle_input.split(","):
        (posx, posy, face) = travel((posx,posy,face), s)
    return abs(posx) + abs(posy)

def all_visits(start, move):
    (posx, posy, face) = start
    move = move.strip()
    turn = move[0]
    dist = int(move[1:])
    face = ( face + face_dict[turn] + 4 ) % 4
    for loop in range(dist):
        posx = posx + x_dict[face]
        posy = posy + y_dict[face]
        yield (posx,posy)

def distance_to_first_twice(puzzle_input):
    """
    >>> distance_to_first_twice("R8, R4, R4, R8")
    4
    """
    history = set()
    posx = posy = face = 0
    for s in puzzle_input.split(","):
        for visit in all_visits((posx,posy,face), s):
            if visit in history:
                (posx,posy) = visit
                return abs(posx) + abs(posy)
            history.add(visit)
        (posx, posy, face) = travel((posx,posy,face), s)
    print history
    return -1

def main():
    puzzle_input = open("day01_input.txt").read()
    print "Part 1 Answer", shortest_distance(puzzle_input)
    print "Part 2 Answer", distance_to_first_twice(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

