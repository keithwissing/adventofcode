#!/usr/bin/env python

import re
import string
from operator import itemgetter

def parse_room(room):
    """
    >>> parse_room("aaaaa-bbb-z-y-x-123[abxyz]")
    ('aaaaa-bbb-z-y-x', 123, 'abxyz')
    """
    pattern = re.compile("(.+)-(.+)\[(.+)\]")
    match = pattern.match(room)
    return ( match.group(1), int(match.group(2)), match.group(3) )


def is_a_real_room(room):
    """
    >>> is_a_real_room("aaaaa-bbb-z-y-x-123[abxyz]")
    True
    >>> is_a_real_room("a-b-c-d-e-f-g-h-987[abcde]")
    True
    >>> is_a_real_room("not-a-real-room-404[oarel]")
    True
    >>> is_a_real_room("totally-real-room-200[decoy]")
    False
    """
    (name,sector,check) = parse_room(room)
    counts = [name.count(x) for x in string.lowercase]
    pairs = [(i,j) for i,j in zip(counts, string.lowercase)]
    pairs.sort(key=itemgetter(0), reverse=True)
    calc = ''.join([b for _,b in pairs[:5]])
    return calc == check

def sum_of_real_room_sectors(puzzle_input):
    real = [room for room in puzzle_input if is_a_real_room(room)]
    parsed = [parse_room(room) for room in real]
    return sum([x for _,x,_ in parsed])

def decrypt_character(char, sector):
    if char == '-':
        return ' '
    return chr( (ord(char)-97+sector) % 26 + 97)

def decrypt_room_name(name, sector):
    """
    >>> decrypt_room_name("qzmt-zixmtkozy-ivhz", 343)
    'very encrypted name'
    """
    return ''.join([decrypt_character(x, sector) for x in name])

def find_north_pole_objects(puzzle_input):
    real = [room for room in puzzle_input if is_a_real_room(room)]
    parsed = [parse_room(room) for room in real]
    for x in parsed:
        if decrypt_room_name(x[0], x[1]) == "northpole object storage":
            return x[1]

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day04_input.txt")]
    print "Part 1 Answer", sum_of_real_room_sectors(puzzle_input)
    print "Part 2 Answer", find_north_pole_objects(puzzle_input)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

