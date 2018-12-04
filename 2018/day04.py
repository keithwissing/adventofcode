#!/usr/bin/env python

import adventofcode

def test1(puzzle_input):
    """
    >>> test1( ["[1518-11-01 00:00] Guard #10 begins shift", \
        "[1518-11-01 00:05] falls asleep", \
        "[1518-11-01 00:25] wakes up", \
        "[1518-11-01 00:30] falls asleep", \
        "[1518-11-01 00:55] wakes up", \
        "[1518-11-01 23:58] Guard #99 begins shift", \
        "[1518-11-02 00:40] falls asleep", \
        "[1518-11-02 00:50] wakes up", \
        "[1518-11-03 00:05] Guard #10 begins shift", \
        "[1518-11-03 00:24] falls asleep", \
        "[1518-11-03 00:29] wakes up", \
        "[1518-11-04 00:02] Guard #99 begins shift", \
        "[1518-11-04 00:36] falls asleep", \
        "[1518-11-04 00:46] wakes up", \
        "[1518-11-05 00:03] Guard #99 begins shift", \
        "[1518-11-05 00:45] falls asleep", \
        "[1518-11-05 00:55] wakes up"])
    240
    4455
    """
    puzzle_input.sort()
    print part1(puzzle_input)
    print part2(puzzle_input)

def part1(puzzle_input):
    times = build_guard_sleep_times(puzzle_input)
    total_sleep = {id:sum(v) for (id, v) in times.items()}
    max_slept_time = max(total_sleep.values())
    choosen_guard = [x for (x, v) in total_sleep.items() if v == max_slept_time][0]
    max_minute_value = max(times[choosen_guard])
    choosen_minute = times[choosen_guard].index(max_minute_value)
    return choosen_guard * choosen_minute

def part2(puzzle_input):
    times = build_guard_sleep_times(puzzle_input)
    max_sleep = {id:max(v) for (id, v) in times.items()}
    max_slept_at_hour = max(max_sleep.values())
    choose = [(gid, v.index(max_slept_at_hour)) for (gid, v) in times.items() if max(v) == max_slept_at_hour][0]
    return choose[0] * choose[1]

def build_guard_sleep_times(puzzle_input):
    data = dict()
    for line in puzzle_input:
        if "Guard" in line:
            guard_id = int(line[26:].split()[0])
        if "asleep" in line:
            sleep = int(line[15:17])
        if "up" in line:
            up = int(line[15:17])
            data = add_to_sleep_map(data, guard_id, sleep, up)
    return data

def add_to_sleep_map(data, guard_id, sleep, up):
    if not data.has_key(guard_id):
        data[guard_id] = [0] * 60
    for x in range(sleep, up):
        data[guard_id][x] += 1
    return data

def main():
    puzzle_input = adventofcode.read_input(4)
    puzzle_input.sort()
    adventofcode.answer(1, 142515, part1(puzzle_input))
    adventofcode.answer(2, 5370, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
