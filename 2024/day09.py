#!/usr/bin/env python3

import adventofcode

t1 = '2333133121414131402'

def part1(line):
    """
    >>> part1(t1)
    1928
    """
    blocks = {}
    pos = 0
    for i, s in enumerate(line):
        for _ in range(int(s)):
            blocks[pos] = i // 2 if i % 2 == 0 else '.'
            pos += 1
    end = pos - 1
    pos = 0
    while pos < end:
        if blocks[pos] == '.':
            blocks[pos] = blocks[end]
            blocks[end] = '.'
            end -= 1
            while blocks[end] == '.':
                end -= 1
        pos += 1
    # print(''.join(str(blocks[i]) for i in range(len(blocks))))

    total = 0
    for k, v in blocks.items():
        if v != '.':
            total += k * int(v)
    return total

# def part2(line):
#     """
#     >>> part2(t1)
#     2858
#     """
#     spans = []
#     for i, s in enumerate(line):
#         spans.append((i // 2 if i % 2 == 0 else '.', int(s)))
#     c = max(spans, key=lambda s: s[0] if s[0] != '.' else 0)[0]
#     while c:
#         print(c)
#         pos = [i for i, v in enumerate(spans) if v[0] == c][0]
#         fid, size = spans[pos]
#         if fid == ',':
#             del spans[pos]
#             continue
#         print(spans)
#         for i in range(pos):
#             if spans[i][0] == '.' and spans[i][1] >= size:
#                 spans = spans[:i] + [spans[pos]] + [('.', spans[i][1] - size)] + spans[i + 1:pos] + spans[pos + 1:]
#                 break
#         spans = [v for v in spans if v[1] > 0]
#         c -= 1
#     spans = [v for v in spans if v[1] > 0]
#     print(spans)

def part2(line):
    """
    >>> part2(t1)
    2858
    """
    blocks = []
    for i, s in enumerate(line):
        blocks += [i // 2 if i % 2 == 0 else '.'] * int(s)
    c = len(line) // 2
    while c:
        sp = blocks.index(c)
        sc = blocks[sp:sp + 10].count(c)
        for dp in range(sp):
            if blocks[dp] == '.' and all(v == '.' for v in blocks[dp:dp + sc]):
                for z in range(dp, dp + sc):
                    blocks[z] = c
                for z in range(sp, sp + sc):
                    blocks[z] = '.'
                break
        c -= 1

    return sum(i * v for i, v in enumerate(blocks) if v != '.')

def main():
    puzzle_input = adventofcode.read_input(9)
    adventofcode.answer(1, 6225730762521, part1(puzzle_input))
    adventofcode.answer(2, 6250605700557, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
