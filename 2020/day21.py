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

def find_safe(foods, all_ingredients, all_allergens):
    safe = set(all_ingredients)
    for a in all_allergens:
        p = set(all_ingredients)
        for f in foods:
            if a in f[1]:
                p &= set(f[0])
        safe = safe.difference(p)
    return safe

def find_possible_ingredients_for_allergens(foods, all_allergens, danger):
    could = {}
    for a in all_allergens:
        p = set(danger)
        for f in foods:
            if a in f[1]:
                p = p.intersection(f[0])
        could[a] = list(p)
    return could

def reduce_possibilities(could):
    remaining = {k: v[:] for k, v in could.items()}  # don't change the input
    changed = True
    while changed:
        changed = False
        for k, vs in remaining.items():
            if len(vs) == 1:
                v = vs[0]
                for k2, v2 in remaining.items():
                    if k != k2 and v in v2:
                        v2.remove(v)
                        remaining[k2] = v2
                        changed = True
    return {k: vs.pop() for k, vs in remaining.items()}

def part1(lines):
    """
    >>> part1(t1)
    5
    """
    foods = parse(lines)
    all_ingredients = set(a for f in foods for a in f[0])
    all_allergens = set(a for f in foods for a in f[1])
    safe = find_safe(foods, all_ingredients, all_allergens)
    return sum(len(set(f[0]).intersection(safe)) for f in foods)

def part2(lines):
    """
    >>> part2(t1)
    'mxmxvkd,sqjhc,fvjkl'
    """
    foods = parse(lines)
    all_ingredients = set(a for f in foods for a in f[0])
    all_allergens = set(a for f in foods for a in f[1])
    safe = find_safe(foods, all_ingredients, all_allergens)

    danger = all_ingredients.difference(safe)
    could = find_possible_ingredients_for_allergens(foods, all_allergens, danger)

    results = reduce_possibilities(could)
    return ','.join(results[k] for k in sorted(results.keys()))

def main():
    puzzle_input = adventofcode.read_input(21)
    adventofcode.answer(1, 2874, part1(puzzle_input))
    adventofcode.answer(2, 'gfvrr,ndkkq,jxcxh,bthjz,sgzr,mbkbn,pkkg,mjbtz', part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
