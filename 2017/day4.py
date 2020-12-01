"""
Author: Kyle Fauerbach
Python solution to advent of code day 4
This works with normal python but pypy gives the wrong answer
"""
def part1():
    """
    answer should be 451
    """
    with open("4_1_in.txt", "r") as my_input:
        lines = my_input.readlines()
    good = 0
    for line in lines:
        line = line.strip().split(' ')
        same = [i for i in line for j in line if i == j and i.index != j.index]
        if not same:
            good += 1
    return good

def part2():
    """
    answer should be 223
    """
    with open("4_1_in.txt", "r") as my_input:
        lines = my_input.readlines()
    good = 0
    for line in lines:
        line = map(sorted, map(list, line.strip().split(' ')))
        same = [a for a in line for b in line if a == b and a.index != b.index]
        if not same:
            good += 1
    return good

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
