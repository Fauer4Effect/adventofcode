"""
Author: Kyle Fauerbach
Python solution to advent of code day 21
"""

import numpy as np
import itertools

def build_np_array(s):
    """
    build a boolean np array from the input
    """
    return np.array([[c == '#' for c in l] for l in s.split('/')])

def enlarge(grid, rules):
    """
    Args:
        grid: Numpy array for the actual image
        rules: Dictionary that defines the replacement strategy
    expand the image
    """
    size = len(grid)
    by = 2 if size % 2 == 0 else 3
    # lambda function to find what the new size should be
    new_size = (lambda x: x * (by+1) // by)(size)
    solution = np.empty((new_size, new_size), dtype=bool)
    squares = range(0, size, by)
    new_squares = range(0, new_size, by+1)

    for i, next_i in itertools.izip(squares, new_squares):
        for j, next_j in itertools.izip(squares, new_squares):
            square = grid[i:i+by, j:j+by]
            enhanced = rules[square.tobytes()]
            solution[next_i:next_i+by+1, next_j:next_j+by+1] = enhanced
    return solution, rules

def solve(iterations):
    """
    Args:
        iterations = how many times should the image be expanded
    part 1 answer should be 184
    part 2 answer should be 2810258
    """
    with open("21_1_in.txt", "r") as my_input:
        instructions = my_input.readlines()
    rules = {}
    start = '.#./..#/###'
    # build dictionary of rules from the puzzle input
    for line in instructions:
        k, v = map(build_np_array, line.strip().split(' => '))
        for a in (k, np.fliplr(k)):
            # preflip all the rules to save time when checking for replacements
            for r in range(4):
                # numpy arrays are not hashable but use tobytes() to create hashable byte string
                rules[np.rot90(a, r).tobytes()] = v
    # build our initial array and then expand the fractal
    grid = build_np_array(start)
    for _ in range(iterations):
        grid, rules = enlarge(grid, rules)
    return int(grid.sum())

if __name__ == "__main__":
    print "part1", solve(5)
    print "part2", solve(18)
