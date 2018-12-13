"""
Author: Kyle Fauerbach
Python solution to advent of code day 10
"""

import re

def part1():
    """
    You know you should stop when the rectangle encompassing all the points starts
    to get bigger again. At this point the points are moving farther away from each other.
    this makes sense because when they form words they should be organized and pretty
    compact vs when its just garbage. At least for this input. It wouldn't work if they all
    started compact and then moved outwards
    """

    with open("10_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()

    positions = [0 for _ in range(len(my_input))]
    velocities = [0 for _ in range(len(my_input))]

    get_nums = re.compile(r"-*[0-9]+")  # save some time by only doing this once
    i = 0
    for line in my_input:
        # we verified this will unpack correctly by checking that all lengths were 4 first
        pos_x, pos_y, vel_x, vel_y = list(map(int, get_nums.findall(line)))
        positions[i] = (pos_x, pos_y)
        velocities[i] = (vel_x, vel_y)
        i += 1

    # TODO the actual hard stuff

    return None

def part2():

    return None

if __name__ == "__main__":
    print(part1())
    print(part2())
