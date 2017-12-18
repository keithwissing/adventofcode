#!/usr/bin/env python

def parse_input_line(line):
    """
    >>> parse_input_line("set p 316")
    ['set', 'p', '316']
    """
    return line.split()

def run_program(instructions):
    reg = {}
    ip = 0
    while ip >= 0 and ip < len(instructions):
        inst = instructions[ip]
        if len(inst) > 2:
            val = reg.get(inst[2], 0) if inst[2].isalpha() else int(inst[2])
        else:
            val = 0
        if inst[0] == "set":
            reg[inst[1]] = val
        elif inst[0] == "add":
            reg[inst[1]] = reg.get(inst[1], 0) + val
        elif inst[0] == "mul":
            reg[inst[1]] = reg.get(inst[1], 0) * val
        elif inst[0] == "mod":
            reg[inst[1]] = reg.get(inst[1], 0) % val
        elif inst[0] == "snd":
            reg["snd"] = reg.get(inst[1], 0)
        elif inst[0] == "rcv":
            if reg.get(inst[1], 0) != 0:
                reg[inst[1]] = reg.get("snd", 0)
                return reg[inst[1]]
        elif inst[0] == "jgz":
            if reg.get(inst[1], 0) > 0:
                ip += val - 1
        ip += 1
    return "done"

def part1(instructions):
    return run_program(instructions)

def test1(lines):
    """
    >>> test1(["set a 1","add a 2","mul a a","mod a 5","snd a","set a 0","rcv a","jgz a -1","set a 1","jgz a -2"])
    4
    """
    instructions = [parse_input_line(line) for line in lines]
    return part1(instructions)

class Program(object):
    def __init__(self, id, inqueue, outqueue, instructions):
        self.id = id
        self.inq = inqueue
        self.outq = outqueue
        self.instructions = instructions
        self.reg = {'p': id}
        self.ip = 0
        self.sendcount = 0

    def argval(self, arg):
        return self.reg.get(arg, 0) if arg.isalpha() else int(arg)

    def run(self):
        if self.ip >= 0 and self.ip < len(self.instructions):
            inst = self.instructions[self.ip]
            val = self.argval(inst[2]) if len(inst) > 2 else 0
            if inst[0] == "set":
                self.reg[inst[1]] = val
            elif inst[0] == "add":
                self.reg[inst[1]] = self.reg.get(inst[1], 0) + val
            elif inst[0] == "mul":
                self.reg[inst[1]] = self.reg.get(inst[1], 0) * val
            elif inst[0] == "mod":
                self.reg[inst[1]] = self.reg.get(inst[1], 0) % val
            elif inst[0] == "snd":
                self.outq.insert(0, self.argval(inst[1]))
                self.sendcount += 1
            elif inst[0] == "rcv":
                if len(self.inq) > 0:
                    self.reg[inst[1]] = self.inq.pop()
                else:
                    return "wait"
            elif inst[0] == "jgz":
                if self.argval(inst[1]) > 0:
                    self.ip += val - 1
            self.ip += 1
            return "run"
        return "done"

def part2(instructions):
    queues = [[], []]
    programs = [Program(0, queues[0], queues[1], instructions), Program(1, queues[1], queues[0], instructions)]
    status = ["run", "run"]
    while status.count("run") > 0:
        last = status[:]
        status[0] = programs[0].run()
        status[1] = programs[1].run()
    return programs[1].sendcount

def test2(lines):
    """
    >>> test2(["snd 1","snd 2","snd p","rcv a","rcv b","rcv c","rcv d"])
    3
    """
    instructions = [parse_input_line(line) for line in lines]
    return part2(instructions)

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day18_input.txt")]
    instructions = [parse_input_line(x) for x in puzzle_input]
    a1 = part1(instructions)
    print "Part 1 Answer", a1
    assert a1 == 2951
    a2 = part2(instructions)
    print "Part 2 Answer", a2
    assert a2 == 7366

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
