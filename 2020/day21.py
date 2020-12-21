#!/usr/bin/env python3

import re
import adventofcode

t1 = [
    'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
    'trh fvjkl sbzzf mxmxvkd (contains dairy)',
    'sqjhc fvjkl (contains soy)',
    'sqjhc mxmxvkd sbzzf (contains fish)',
]

def parse(lines):
    foods = []
    for line in lines:
        m = re.match(r'^(.+) \(contains (.+)\)$', line)
        foods.append([m[1].split(), m[2].split(', ')])
    return foods

def part1(lines):
    """
    >>> part1(t1)
    5
    """
    foods = parse(lines)
    all_allergens = set()
    all_ingredients = set()
    for f in foods:
        all_ingredients.update(f[0])
        all_allergens.update(f[1])
    safe = set(all_ingredients)
    for a in all_allergens:
        p = set(all_ingredients)
        for f in foods:
            if a in f[1]:
                p &= set(f[0])
        safe = safe.difference(p)
    tot = 0
    for f in foods:
        tot += len(set(f[0]).intersection(safe))
    return tot

def part2(lines):
    """
    >>> part2(t1)
    'mxmxvkd,sqjhc,fvjkl'
    """
    foods = parse(lines)
    all_allergens = set()
    all_ingredients = set()
    for f in foods:
        all_ingredients.update(f[0])
        all_allergens.update(f[1])
    safe = set(all_ingredients)
    for a in all_allergens:
        p = set(all_ingredients)
        for f in foods:
            if a in f[1]:
                p &= set(f[0])
        safe = safe.difference(p)
    tot = 0
    for f in foods:
        tot += len(set(f[0]).intersection(safe))
    for f in foods:
        for i in safe:
            if i in f[0]:
                f[0].remove(i)
    danger = all_ingredients.difference(safe)
    could = {}
    for a in all_allergens:
        p = set(danger)
        for f in foods:
            if a in f[1]:
                p = p.intersection(f[0])
        could[a] = p
    changed = True
    while changed:
        changed = False
        for k, vs in could.items():
            if len(vs) == 1:
                for v in vs:
                    for k2, v2 in could.items():
                        if k != k2 and v in v2:
                            v2.remove(v)
                            could[k2] = v2
                            changed = True
    a = ','.join(could[k].pop() for k in sorted(could.keys()))
    return a

def main():
    puzzle_input = adventofcode.read_input(21)
    adventofcode.answer(1, 2874, part1(puzzle_input))
    adventofcode.answer(2, 'gfvrr,ndkkq,jxcxh,bthjz,sgzr,mbkbn,pkkg,mjbtz', part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
