"""
Author: Kyle Fauerbach
Python solution to advent of code day 1
"""

def part1():
    with open("1_1_in.txt", "r") as my_input:
        my_input = my_input.read().split()
    freq = 0
    for l in my_input:
        freq = eval("{}{}".format(freq, l))
    return freq

def part2():
    with open("1_1_in.txt", "r") as my_input:
        my_input = my_input.read().split()
    freq = 0
    seen = set()
    while 1:
        for l in my_input:
            seen.add(freq)
            freq = eval("{}{}".format(freq, l))
            if freq in seen:
                return freq

if __name__ == "__main__":
    print(part1())
    print(part2())