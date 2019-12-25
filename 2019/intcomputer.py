#!/usr/bin/env python3

from collections import defaultdict

def split_code(code):
    """
    >>> split_code(1103)
    ('0011', 3)
    """
    opcode = code % 100
    modes = str(code // 100).zfill(4)
    return (modes, opcode)

class IntComputer:
    def __init__(self, mem, inputs=None):
        self.ip = 0
        self.rbase = 0
        self.mem = defaultdict(lambda: 0, {k:v for k, v in enumerate(mem)})
        self.inputs = [] if inputs is None else inputs[:] if isinstance(inputs, list) else [inputs]
        self.outputs = []

    def get_param(self, n, modes):
        if modes[4-n] == '0':
            return self.mem[self.mem[self.ip+n]]
        if modes[4-n] == '1':
            return self.mem[self.ip+n]
        if modes[4-n] == '2':
            return self.mem[self.rbase+self.mem[self.ip+n]]
        raise Exception('invalid read param mode')

    def write(self, n, modes, value):
        if modes[4-n] == '0':
            self.mem[self.mem[self.ip+n]] = value
        elif modes[4-n] == '2':
            self.mem[self.rbase+self.mem[self.ip+n]] = value
        else:
            raise Exception('invalid write param mode')

    def step(self):
        ip = self.ip
        (modes, opcode) = split_code(self.mem[self.ip])
        if opcode == 99:
            return -1
        if opcode == 3: # input
            self.write(1, modes, self.inputs.pop(0))
            return ip + 2
        p1 = self.get_param(1, modes)
        if opcode == 4: # output
            self.outputs.append(p1)
            return ip + 2
        if opcode == 9: # relative base adjust
            self.rbase += p1
            return ip + 2
        p2 = self.get_param(2, modes)
        if opcode == 5: # jump-if-true
            return p2 if p1 != 0 else ip + 3
        if opcode == 6: # jump-if-false
            return p2 if p1 == 0 else ip + 3
        if opcode == 1: # add
            self.write(3, modes, p1 + p2)
            return ip + 4
        if opcode == 2: # multiply
            self.write(3, modes, p1 * p2)
            return ip + 4
        if opcode == 7: # less than
            self.write(3, modes, 1 if p1 < p2 else 0)
            return ip + 4
        if opcode == 8: # equals
            self.write(3, modes, 1 if p1 == p2 else 0)
            return ip + 4
        raise Exception(f'invalid opcode {opcode} at {ip}')

    def run_program(self):
        while self.ip >= 0:
            self.ip = self.step()
        return self.outputs

    def run_until_output(self, inputs=None):
        self.inputs = [] if inputs is None else inputs[:] if isinstance(inputs, list) else [inputs]
        self.outputs = []
        while self.ip >= 0 and not self.outputs:
            self.ip = self.step()
        return self.outputs[0] if self.outputs else -1

    def run_until_outputs(self, inputs=None):
        self.inputs = [] if inputs is None else inputs[:] if isinstance(inputs, list) else [inputs]
        self.outputs = []
        while self.ip >= 0 and len(self.outputs) < 3:
            self.ip = self.step()
        return self.outputs if self.outputs else []

    def run_until_outputs_or_no_input(self, inputs=None):
        self.inputs = [] if inputs is None else inputs[:] if isinstance(inputs, list) else [inputs]
        self.outputs = []
        while self.ip >= 0 and len(self.outputs) < 3 and len(self.inputs) > 0:
            self.ip = self.step()
        return self.outputs if self.outputs else []

    def run_until_prompt(self, inputs):
        self.inputs = inputs
        self.outputs = []
        while self.ip >= 0:
            if not self.inputs and self.outputs and self.outputs[-3:] == [ord('n'), ord('d'), ord('?')]:
                break
            self.ip = self.step()
        return self.outputs if self.outputs else []
