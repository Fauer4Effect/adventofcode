"""
Author: Kyle Fauerbach
Python solution to advent of code day 17
"""

from collections import deque
import re

def part1():
    with open("17_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()
    clay = set()
    min_y = 100000000
    max_y = 0
    for line in my_input:
        x = re.findall(r"x=[0-9.]*", line)[0][2:]
        y = re.findall(r"y=[0-9.]*", line)[0][2:]
        if '..' in x:
            y = int(y)
            lo, hi = list(map(int, x.split('..')))
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            for x2 in range(lo, hi+1):
                clay.add((x2, y))
        elif '..' in y:
            x = int(x)
            lo, hi = list(map(int, y.split('..')))
            min_y = min(min_y, lo)
            max_y = max(max_y, hi)
            for y2 in range(lo, hi+1):
                clay.add((x, y2))
        else:
            x = int(x)
            y = int(y)
            clay.add((x, y))
            min_y = min(min_y, y)
            max_y = max(max_y, y)

    print(min_y, max_y)
    cur_pos = (500, 0)

    while 1:
        # if you can go down then go down
        # if beneath you is clay or settled water and between to walls you can settle
        # if it's not then you touch but don't settle and you continue down
        # if you can't go down and beneath you is settled or clay you can spread either direction
        # until you hit a wall or are able to continue down

        break


    return None

def part2():

    return None

if __name__ == "__main__":
    print(part1())
    print(part2())
