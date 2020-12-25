"""
Author: Kyle Fauerbach
Python solution to advent of code day 20
"""

def part1():
    # need to select the longest everytime the regex branches
    # so when we hit a ( we need to find the matching one on the end
    # then you need to split by | but only the main ones that aren't also in their
    # own () which would make them independant
    # so probably some sort of recursive algorithm type deal
    # maybe one that substitutes chunks of the regex with their length? might be an easier start

    return None

def part2():

    return None

if __name__ == "__main__":
    print(part1())
    print(part2())
