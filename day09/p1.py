#!/usr/bin/env python

import itertools

def parse_line(line):
    """
    >>> parse_line("London to Dublin = 464")
    ('London', 'Dublin', 464)
    """
    first,rest = line.split(' to ',1)
    second,distance = rest.split(' = ')
    return (first,second,int(distance))

def get_set_of_all_cities(lines):
    ret = set()
    for x in lines:
        ret.add(x[0])
        ret.add(x[1])
    return ret

def get_dict_of_distances(lines):
    ret = {}
    for line in lines:
        ret[(line[0],line[1])] = line[2]
        ret[(line[1],line[0])] = line[2]
    return ret

def route_distance(route, distances):
    total = 0
    for x in range(1,len(route)):
        leg = (route[x-1],route[x])
        total = total + distances[leg]
    return total

def extreme_route(lines,func):
    parsed = [parse_line(x) for x in lines]
    cities = get_set_of_all_cities(parsed)
    distances= get_dict_of_distances(parsed)
    low = route_distance(list(cities),distances)
    for route in itertools.permutations(cities):
        total = route_distance(route,distances)
        low = func(low,total)
    return low

def shortest_route(lines):
    """
    >>> shortest_route( [\
            "London to Dublin = 464",\
            "London to Belfast = 518",\
            "Dublin to Belfast = 141"] )
    605
    """
    return extreme_route(lines,min)

def longest_route(lines):
    """
    >>> longest_route( [\
            "London to Dublin = 464",\
            "London to Belfast = 518",\
            "Dublin to Belfast = 141"] )
    982
    """
    return extreme_route(lines,max)

def main():
    input = [line.strip() for line in open('input.txt')]
    print shortest_route(input)
    print longest_route(input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

