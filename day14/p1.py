#!/usr/bin/env python

def parse_line(line):
    """
    >>> parse_line("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
    ('Comet', 14, 10, 127)
    >>> parse_line("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.")
    ('Dancer', 16, 11, 162)
    """
    words = line.split()
    return (words[0], int(words[3]), int(words[6]), int(words[13]))

def distance_traveled(deer, time):
    """
    >>> distance_traveled(('Comet', 14, 10, 127), 1000)
    ('Comet', 1120)
    >>> distance_traveled(('Dancer', 16, 11, 162), 1000)
    ('Dancer', 1056)
    """
    (name, speed, endurance, rest) = deer
    cycle = endurance + rest
    complete_cycles = time / cycle
    remainder = time - complete_cycles * cycle
    return (name, speed * (endurance * complete_cycles + min(remainder, endurance)))

def new_scoring(participants, time):
    """
    >>> new_scoring([('Comet', 14, 10, 127), ('Dancer', 16, 11, 162)], 1000)
    {'Comet': 312, 'Dancer': 689}
    """
    scores = dict.fromkeys([x[0] for x in participants], 0)
    for t in range(1, time+1):
        positions = [distance_traveled(x, t) for x in participants]
        lead = max([x[1] for x in positions])
        for d in positions:
            if d[1] == lead:
                scores[d[0]] += 1
    return scores

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    print max([distance_traveled(parse_line(x), 2503)[1] for x in puzzle_input])
    participants = [parse_line(x) for x in puzzle_input]
    scores = new_scoring(participants, 2503)
    print max(scores.values())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

