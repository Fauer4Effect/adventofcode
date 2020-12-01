"""
Author: Kyle Fauerbach
Python solution to advent of code day 11
"""

import numpy as np
from scipy import signal

def get_power(x, y, serial):
    rack_id = x+10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = int("{}".format(power).zfill(3)[-3])
    power -= 5
    return power

def do_convolution(kernel_size):
    """
    https://stackoverflow.com/a/19533655

    Create a 300x300 2D array, where each cell contains the power level of that cell.
    Then convolve that array with a 3x3 kernel, the resulting array will have total power in a 3x3
    region in each cell.
    Then find the cell with the largest value.
    """

    serial = 8444

    # grid = [[0 for _ in range(300)] for _ in range(300)]
    grid = np.zeros((300, 300))
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            grid[y, x] = get_power(x+1, y+1, serial)

    # we don't want to change anything so just use all 1's
    kernel = np.ones((kernel_size, kernel_size))
    # XXX specify valid so we only get ones that are fully in the matrix
    convolved = signal.convolve2d(grid, kernel, mode='valid')

    # The maximum power in the 3x3 area
    max_power = convolved.max()
    # get the coordinates of the max point
    # this should correspond to the top left corner of our 3x3 region
    max_coords = np.unravel_index(np.argmax(convolved), convolved.shape)
    # remember to flip the order since you want x-y not y-x
    x = max_coords[1]+1
    y = max_coords[0]+1

    return x, y, max_power

def part1():
    return do_convolution(3)

def part2():
    best_val = 0
    # XXX after running from 1-301 I'm going to cheat this so we can re run it faster
    for kernel_size in range(1, 50):
        x, y, val = do_convolution(kernel_size)
        if val > best_val:
            best_x = x
            best_y = y
            best_kernel = kernel_size
            best_val = val
    return best_x, best_y, best_kernel, best_val

if __name__ == "__main__":
    x, y, val = part1()
    print("PART 1: x={}, y={}, val={}".format(x, y, val))
    x, y, size, val = part2()
    print("PART 2: x={}, y={}, size={}, val={}".format(x, y, size, val))
