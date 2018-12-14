"""
Author: Kyle Fauerbach
Python solution to advent of code day 10
"""

import re

def solve():
    """
    THIS IS WAY FASTER IF YOU USE pypy

    You know you should stop when the rectangle encompassing all the points starts
    to get bigger again. At this point the points are moving farther away from each other.
    this makes sense because when they form words they should be organized and pretty
    compact vs when its just garbage. At least for this input. It wouldn't work if they all
    started compact and then moved outwards
    """

    with open("10_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()

    get_nums = re.compile(r'-?\d+')  # save some time by only doing this once
    data = [list(map(int, get_nums.findall(line))) for line in my_input]

    bounding_boxes = []
    # arbitrarily guess that we will find the pattern by then
    for sec in range(20000):
        minx, maxx, miny, maxy = 10000, 0, 10000, 0
        for x, y, vx, vy in data:
            minx = min(minx, x + sec * vx)
            maxx = max(maxx, x + sec * vx)
            miny = min(miny, y + sec * vy)
            maxy = max(maxy, y + sec * vy)
        bounding_boxes.append([maxx, minx, maxy, miny])

    # find the minimum bounding box achieved in that time
    min_bounding = min(maxx - minx + maxy - miny for maxx, minx, maxy, miny in bounding_boxes)
    # find what second aligns with that minimum bounding box
    for sec, (maxx, minx, maxy , miny) in enumerate(bounding_boxes):
        if min_bounding == maxx - minx + maxy - miny:
            break
    grid = [[' ' for _ in range(minx, maxx+1)] for _ in range(miny, maxy+1)]
    for (x, y, vx, vy) in data:
        grid[y + sec * vy - miny][x + sec * vx - minx] = '#'

    ans = []
    for row in grid:
        ans.append(''.join(row))

    return '\n'.join(ans), sec

if __name__ == "__main__":
    string, time = solve()
    print(string)
    print(time)
