"""
Author: Kyle Fauerbach
Python solution to advent of code day 5
"""

import itertools as it

def are_opposites(a, b):
    return (a.lower() == b.lower() and
            ((a.isupper() and b.islower()) or
             (a.islower() and b.isupper())))

def collapse_polymer(poly):
    polymer = []

    for c in poly:
        if polymer and are_opposites(c, polymer[-1]):
            polymer.pop()
        else:
            polymer.append(c)

    return len(polymer)

def part1():
    with open("5_1_in.txt", "r") as my_input:
        my_input = my_input.read().strip()
    polymer = list(my_input)

    return collapse_polymer(polymer)

def part2():
    with open("5_1_in.txt", "r") as my_input:
        my_input = my_input.read().strip()
    types = set(my_input.lower())

    length = len(my_input)
    polymer = list(my_input)
    for type in types:
        new_polymer = [x for x in polymer if (x != type and (x.lower() != type))]
        length = min(length, collapse_polymer(new_polymer))

    return length

if __name__ == "__main__":
    print(part1())
    print(part2())
