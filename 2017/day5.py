"""
Author: Kyle Fauerbach
Python solution to advent of code day 5
Much faster to run with pypy than with vanilla python
"""
def part1():
    """
    Answer should be 372139
    """
    count = 0
    with open("5_1_in.txt", "r") as my_input:
        vals = {v: k for v, k in enumerate(map(int, my_input.readlines()))}
    index = 0
    last_index = -1
    last_elem = len(vals)
    while index < last_elem:
        if last_index > -1:
            vals[last_index] += 1
        last_index = index
        index += vals[index]
        count += 1
    return count

def part2():
    """
    Answer should be 29629538
    """
    count = 0
    with open("5_1_in.txt", "r") as my_input:
        vals = {v: k for v, k in enumerate(map(int, my_input.readlines()))}
    index = 0
    last_index = -1
    last_elem = len(vals)
    while index < last_elem:
        if last_index > -1:
            if vals[last_index] > 2:
                vals[last_index] -= 1
            else:
                vals[last_index] += 1
        last_index = index
        index += vals[index]
        count += 1
    return count

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
