"""
Author: Kyle Fauerbach
Python solution to advent of code day 6
"""

from collections import defaultdict
import numpy as np
import operator

# return the point number that is closest to your point
def closest(points, coord_x, coord_y):
    distances = defaultdict(int)
    for n, (k, l) in enumerate(points):
        distances[n] = abs(coord_x-k) + abs(coord_y-l)
    lowest = min(distances.items(), key=operator.itemgetter(1))
    distances[lowest[0]] = 1000
    lowest2 = min(distances.items(), key=operator.itemgetter(1))
    # if it is same distance to multiple points it doesn't count
    if lowest[1] == lowest2[1]:
        return 'X'
    return lowest[0]

def part1():
    with open("6_1_in.txt", "r") as my_input:
        points = [list(map(int, i.strip().split(", "))) for i in my_input.readlines()]
    max_x = max(map(lambda x: x[0], points))
    max_y = max(map(lambda x: x[1], points))
    min_x = min(map(lambda x: x[0], points))
    min_y = min(map(lambda x: x[1], points))

    grid = defaultdict(int)
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            grid[closest(points, i, j)] += 1
    grid['X'] = 0

    # Any region that has a point on the edge is infinite
    infinites = set()
    for x in range(min_x, max_x+1):
        infinites.add(closest(points, x, min_y))
    for y in range(min_y, max_y+1):
        infinites.add(closest(points, min_x, y))
    for x in range(min_x, max_x+1):
        infinites.add(closest(points, x, max_y))
    for y in range(min_y, max_y+1):
        infinites.add(closest(points, max_x, y))
    for point in infinites:
        grid[point] = 0

    return max(grid.items(), key=operator.itemgetter(1))[1]


def part2():
    with open("6_1_in.txt", "r") as my_input:
        points = [list(map(int, i.strip().split(", "))) for i in my_input.readlines()]
    max_x = max(map(lambda x: x[0], points))
    max_y = max(map(lambda x: x[1], points))

    # + 1 because we want to make sure to include the thing on the grid
    xx, yy = np.meshgrid(np.arange(max_x+1), np.arange(max_y+1))

    layers = []
    for point in points:
        # This gets you a rectangular grid that has the manhattan distance from the point
        mdists = np.abs(xx - point[0]) + np.abs(yy - point[1])
        layers.append(mdists)

    dist_array = np.array(layers)
    # collapse the layers to get the sum distance of every point on the grid to each of the
    # marked points
    tot_dists = dist_array.sum(axis=0)
    return (tot_dists < 10000).sum()

if __name__ == "__main__":
    print(part1())
    print(part2())
