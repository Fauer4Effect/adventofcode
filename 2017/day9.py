"""
Author: Kyle Fauerbach
Python solution to advent of code day 8
"""

import re

def part1():
    """
    answer should be 11089
    """
    with open("9_1_in.txt", "r") as my_input:
        streams = my_input.read().strip()
    # handle all negations
    streams = re.sub(r'![\w\W]', '', streams)
    # handle all garbage *? makes it non greedy
    streams = re.sub(r'<.*?>', '', streams)
    depth = 0
    total = 0
    for char in streams:
        if char == "{":
            depth += 1
        elif char == "}":
            total += depth
            depth -= 1
    return total

def part2():
    """
    answer should be 5288
    """
    with open("9_1_in.txt", "r") as my_input:
        streams = my_input.read().strip()
    # remove all negations
    streams = re.sub(r'![\w\W]', '', streams)
    count = False
    garbage = 0
    for char in streams:
        if char == '<' and not count:
            count = True
        elif count:
            if char == '>':
                count = False
            else:
                garbage += 1
    return garbage

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
