#!/usr/bin/env python

def get_cell_value(grid, line, column):
    """
    >>> get_cell_value([ '.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..' ], 0, 0)
    0
    >>> get_cell_value([ '.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..' ], 0, 1)
    1
    """
    if line >= 0 and line < len(grid) and column >= 0 and column < len(grid[line]):
        return 1 if grid[line][column] == '#' else 0
    return 0

def get_live_neighbor_count(grid, line, column):
    """
    >>> get_live_neighbor_count([ '.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..' ], 0, 0)
    1
    """
    neighbors = 0
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if y != 0 or x != 0:
                neighbors += get_cell_value(grid, line + y, column + x)
    return neighbors

def should_i_be_alive(myself, neighbors):
    """
    >>> should_i_be_alive(1, 1)
    0
    >>> should_i_be_alive(1, 3)
    1
    >>> should_i_be_alive(0, 3)
    1
    >>> should_i_be_alive(0, 1)
    0
    """
    if myself == 1:
        newval = 1 if neighbors in [2, 3] else 0
    else:
        newval = 1 if neighbors == 3 else 0
    return newval

def step(grid):
    """
    >>> step([ '.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..' ])
    ['..##..', '..##.#', '...##.', '......', '#.....', '#.##..']
    >>> step(['..##..', '..##.#', '...##.', '......', '#.....', '#.##..'])
    ['..###.', '......', '..###.', '......', '.#....', '.#....']
    """
    out = []
    for line in range(0, len(grid)):
        newline = []
        for cell in range(0, len(grid[line])):
            neighbors = get_live_neighbor_count(grid, line, cell)
            me = get_cell_value(grid, line, cell)
            newval = should_i_be_alive(me, neighbors)
            #print me, neighbors, newval
            newline.append('#' if newval == 1 else '.')
        out.append(''.join(newline))
    return out

def turn_on_corners(grid):
    """
    >>> turn_on_corners([ '.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..' ])
    ['##.#.#', '...##.', '#....#', '..#...', '#.#..#', '####.#']
    """
    grid[0] = '#'+grid[0][1:-1]+'#'
    grid[len(grid)-1] = '#'+grid[len(grid)-1][1:-1]+'#'
    return grid

def total_lights_on(grid):
    return sum([sum([0 if v == '.' else 1 for v in line]) for line in grid])

def lights_after_steps(grid, steps):
    """
    >>> lights_after_steps([ '.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..' ], 4)
    4
    """
    for _ in range(0, steps):
        grid = step(grid)
    return total_lights_on(grid)

def broken_lights_after_steps(grid, steps):
    """
    >>> broken_lights_after_steps([ '.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..' ], 5)
    17
    """
    grid = turn_on_corners(grid)
    for _ in range(0, steps):
        grid = step(grid)
        grid = turn_on_corners(grid)
    return total_lights_on(grid)

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    #print 'Part 1', lights_after_steps(puzzle_input, 100)
    print 'Part 2', broken_lights_after_steps(puzzle_input, 100)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

