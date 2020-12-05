#!/usr/bin/env python3

import re
import adventofcode

t1 = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in',
]

def passports(lines):
    pp = {}
    for line in lines:
        if len(line) < 2:
            if len(pp) > 0:
                yield pp
            pp = {}
        else:
            for f in line.split():
                k, v = f.split(':')
                pp[k] = v
    if len(pp) > 0:
        yield pp

def part1(lines):
    """
    >>> part1(t1)
    2
    """
    tot = 0
    for pp in passports(lines):
        invalid = False
        for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if k not in pp:
                invalid = True
        if not invalid:
            tot += 1
    return tot

def part2(lines):
    tot = 0
    for pp in passports(lines):
        invalid = False
        if 'byr' in pp:
            val = pp['byr']
            if len(val) != 4 or int(val) < 1920 or int(val) > 2002:
                invalid = True
        else:
            invalid = True
        if 'iyr' in pp:
            val = pp['iyr']
            if len(val) != 4 or int(val) < 2010 or int(val) > 2020:
                invalid = True
        else:
            invalid = True
        if 'eyr' in pp:
            val = pp['eyr']
            if len(val) != 4 or int(val) < 2020 or int(val) > 2030:
                invalid = True
        else:
            invalid = True
        if 'hgt' in pp:
            val = pp['hgt']
            if val[-2:] == 'cm':
                n = int(val[:-2])
                if n < 150 or n > 193:
                    invalid = True
            elif val[-2:] == 'in':
                n = int(val[:-2])
                if n < 59 or n > 76:
                    invalid = True
            else:
                invalid = True
        else:
            invalid = True
        if 'hcl' in pp:
            val = pp['hcl']
            if val[0] != '#':
                invalid = True
            elif len(val) != 7:
                invalid = True
            else:
                for c in val[1:]:
                    if c not in '0123456789abcdef':
                        invalid = True
        else:
            invalid = True
        if 'ecl' in pp:
            val = pp['ecl']
            if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                invalid = True
        else:
            invalid = True
        if 'pid' in pp:
            val = pp['pid']
            if len(val) != 9:
                invalid = True
            for c in val:
                if c not in '0123456789':
                    invalid = True
        else:
            invalid = True

        if not invalid:
            tot += 1
    return tot

def valid_height(val):
    allowed = {'cm': (150, 193), 'in': (59, 76)}
    m = re.match(r'^(\d+)(in|cm)$', val)
    if m:
        h = int(m[1])
        ar = allowed[m[2]]
        return ar[0] <= h <= ar[1]
    return False

checks = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': lambda v: valid_height(v),
    'hcl': lambda val: re.match(r'^#[0-9a-f]{6}$', val),
    'ecl': lambda val: val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda val: re.match(r'^[0-9]{9}$', val),
}

def part2_2(lines):
    tot = 0
    for pp in passports(lines):
        invalid = False
        for k, check in checks.items():
            if k not in pp or not check(pp[k]):
                invalid = True
        if not invalid:
            tot += 1
    return tot

def main():
    puzzle_input = adventofcode.read_input(4)
    adventofcode.answer(1, 254, part1(puzzle_input))
    adventofcode.answer(2, 184, part2(puzzle_input))
    adventofcode.answer(2, 184, part2_2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
