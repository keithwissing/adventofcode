#!/usr/bin/env python

import adventofcode

test_1 = """
Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
""".split('\n')

boost = 0

def part1(groups):
    """
    >>> part1(parse_input(test_1))
    5216
    """
    global boost
    boost = 0
    while groups.conflict_remains():
        fight(groups)
    return groups.remaining_units()

def part2(puzzle_input):
    """
    >>> part2(test_1)
    51
    """
    b = 0
    while True:
        # print 'Trying with boost', b,
        groups = parse_input(puzzle_input)
        winner, remain = winner_with_boost(groups, b)
        # print 'Winner', winner, remain
        if winner == 'S':
            return remain
        b += 1

def winner_with_boost(groups, b):
    global boost
    boost = b
    while groups.conflict_remains():
        kills = fight(groups)
        if kills == 0:
            break
    return groups.winning_side(), groups.remaining_units()

def fight(armys):
    select_order = [(g.effective_power(), g.initiative, g.id) for g in armys.remaining_groups()]
    select_order.sort()
    select_order.reverse()
    already_targeted = []
    planned = []
    for s in select_order:
        a = armys.get(s[2])
        targets = [(damage_amount(a, d), d.effective_power(), d.initiative, d.id) for d in armys.remaining_opponents(a.side)]
        targets = [t for t in targets if t[0] > 0 and t[3] not in already_targeted]
        if targets:
            targets.sort()
            targets.reverse()
            t = targets[0]
            planned.append((s[1], s[2], t[3]))
            already_targeted.append(t[3])
    planned.sort()
    planned.reverse()
    kills = 0
    for b in planned:
        kills += armys.attack(b[1], b[2])
    return kills

class Armys(object):
    def __init__(self):
        self.groups = []

    def display(self):
        #for x in self.groups:
        for x in self.remaining_groups():
            x.display()

    def remaining_units(self):
        return sum(x.units for x in self.remaining_groups())

    def copy(self):
        c = Armys()
        c.groups = self.groups[:]

    def attack(self, a_id, d_id):
        a = self.get(a_id)
        d = self.get(d_id)
        if a.units > 0:
            kills = damage_amount(a, d) / d.hp
            d.units -= kills
            return kills
        return 0

    def append(self, group):
        self.groups.append(group)

    def get(self, id):
        return [g for g in self.groups if g.id == id][0]

    def remaining_groups(self):
        for x in self.groups:
            if x.units > 0:
                yield x

    def remaining_opponents(self, side):
        for x in self.remaining_groups():
            if x.side != side:
                yield x

    def conflict_remains(self):
        sides = [x.side for x in self.remaining_groups()]
        return sides.count('S') > 0 and sides.count('I') > 0

    def winning_side(self):
        if self.conflict_remains():
            return None
        return [x.side for x in self.remaining_groups()][0]

def damage_amount(a, d):
    return a.effective_power() * d.damage_multiplier(a.attack_type)

class Group(object):
    def __init__(self, id, side, units, hp, attack, attack_type, initiative, mods):
        self.id = id
        self.side = side
        self.units = units
        self.hp = hp
        self.attack = attack
        self.attack_type = attack_type
        self.initiative = initiative
        self.mods = mods

    def display(self):
        print 'id', self.id, 'side', self.side, 'units', self.units, 'hp', self.hp, 'eff', self.effective_power(), 'i', self.initiative, self.attack_type, self.mods

    def effective_power(self):
        global boost
        if self.side == 'S':
            return self.units * (self.attack + boost)
        return self.units * self.attack

    def damage_multiplier(self, attack_type):
        for m in self.mods:
            if attack_type in m:
                return 2 if m[0] == 'weak' else 0
        return 1

def parse_mods(mods):
    if mods.count('to') > 1:
        t2 = mods[2:].index('to')+2
        mods = [mods[:t2-1], mods[t2-1:]]
    else:
        mods = [mods[:]]
    for i in mods:
        if i:
            i.remove('to')
    return mods

def parse_input(puzzle_input):
    armys = Armys()
    side = ''
    for ln, line in enumerate(puzzle_input):
        if not line:
            continue
        if 'Immune System:' in line:
            side = 'S'
        if 'Infection:' in line:
            side = 'I'
        if 'units each with' in line:
            parts = line.replace('(', '').replace(')', '').replace(',', '').replace(';', '').split()
            units = int(parts[0])
            hp = int(parts[4])
            di = parts.index('does')
            attack = int(parts[di+1])
            attack_type = parts[di+2]
            initiative = int(parts[di+6])
            mods = parts[7:parts[6:].index('with')+6]
            mods = parse_mods(mods)
            ng = Group(ln, side, units, hp, attack, attack_type, initiative, mods)
            armys.append(ng)
    return armys

def main():
    puzzle_input = adventofcode.read_input(24)
    units = parse_input(puzzle_input)
    adventofcode.answer(1, 10723, part1(units))
    adventofcode.answer(2, 5120, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
