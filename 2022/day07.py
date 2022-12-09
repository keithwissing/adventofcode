#!/usr/bin/env python3
import os

import adventofcode

t1 = [
    '$ cd /',
    '$ ls',
    'dir a',
    '14848514 b.txt',
    '8504156 c.dat',
    'dir d',
    '$ cd a',
    '$ ls',
    'dir e',
    '29116 f',
    '2557 g',
    '62596 h.lst',
    '$ cd e',
    '$ ls',
    '584 i',
    '$ cd ..',
    '$ cd ..',
    '$ cd d',
    '$ ls',
    '4060174 j',
    '8033020 d.log',
    '5626152 d.ext',
    '7214296 k',
]

def parse(lines):
    cwd = '/'
    dirs = set(cwd)
    files = []
    for line in lines:
        if line == '$ cd /':
            cwd = '/'
        elif line == '$ cd ..':
            cwd, _ = os.path.split(cwd)
        elif line.startswith('$ cd'):
            cwd = os.path.join(cwd, line[5:])
        elif line == '$ ls':
            pass
        else:
            ls = line.split()
            if ls[0] == 'dir':
                pass
            else:
                size = int(ls[0])
                files.append((cwd, ls[1], size))
        dirs.add(cwd)
    return dirs, files

def dir_sizes(dirs, files):
    return [(d, sum(f[2] for f in files if f[0].startswith(d))) for d in dirs]

def part1(lines):
    """
    >>> part1(t1)
    95437
    """
    dirs, files = parse(lines)
    dsizes = dir_sizes(dirs, files)
    return sum(d[1] for d in dsizes if d[1] < 100000)

def part2(lines):
    """
    >>> part2(t1)
    24933642
    """
    dirs, files = parse(lines)
    dsizes = dir_sizes(dirs, files)
    disk_size = 70000000
    used_space = next(d[1] for d in dsizes if d[0] == '/')
    return min([d[1] for d in dsizes if disk_size - used_space + d[1] >= 30000000])

def main():
    puzzle_input = adventofcode.read_input(7)
    adventofcode.answer(1, 1723892, part1(puzzle_input))
    adventofcode.answer(2, 8474158, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
