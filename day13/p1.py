#!/usr/bin/env python

import itertools

def parse_line(line):
    """
    >>> parse_line("Alice would gain 54 happiness units by sitting next to Bob.")
    ('Alice', 'Bob', 54)
    >>> parse_line("Alice would lose 79 happiness units by sitting next to Carol.")
    ('Alice', 'Carol', -79)
    """
    first, rest = line.split(' would ', 1)
    rest, second = rest.split(' happiness units by sitting next to ')
    rest = rest.split(' ')
    third = int(rest[1]) if rest[0] == 'gain' else -int(rest[1])
    second = second[:-1]
    return (first, second, third)

def get_set_of_all_people(lines):
    ret = set()
    for x in lines:
        ret.add(x[0])
        ret.add(x[1])
    return ret

def get_dict_of_happiness(lines):
    ret = {}
    for line in lines:
        ret[(line[0], line[1])] = line[2]
    return ret

def route_distance(route, distances):
    total = 0
    for x in range(0, len(route)):
        leg1 = (route[x], route[(x+1)%len(route)])
        leg2 = (route[(x+1)%len(route)], route[x])
        total = total + distances[leg1] + distances[leg2]
    return total

def extreme_route(lines, func, post=None):
    parsed = [parse_line(x) for x in lines]
    cities = get_set_of_all_people(parsed)
    distances = get_dict_of_happiness(parsed)

    if post:
        post(cities, distances)

    low = route_distance(list(cities), distances)
    for route in itertools.permutations(cities):
        total = route_distance(route, distances)
        low = func(low, total)
    return low

def add_myself(cities, distances):
    for p in cities:
        distances[(p, 'me')] = 0
        distances[('me', p)] = 0
    cities.add('me')

def shortest_route(lines):
    """
    >>> shortest_route( [\
            'Alice would gain 54 happiness units by sitting next to Bob.',\
            'Alice would lose 79 happiness units by sitting next to Carol.',\
            'Alice would lose 2 happiness units by sitting next to David.',\
            'Bob would gain 83 happiness units by sitting next to Alice.',\
            'Bob would lose 7 happiness units by sitting next to Carol.',\
            'Bob would lose 63 happiness units by sitting next to David.',\
            'Carol would lose 62 happiness units by sitting next to Alice.',\
            'Carol would gain 60 happiness units by sitting next to Bob.',\
            'Carol would gain 55 happiness units by sitting next to David.',\
            'David would gain 46 happiness units by sitting next to Alice.',\
            'David would lose 7 happiness units by sitting next to Bob.',\
            'David would gain 41 happiness units by sitting next to Carol.'] )
    330
    """
    return extreme_route(lines, max)

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    print shortest_route(puzzle_input)
    print extreme_route(puzzle_input, max, add_myself)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

