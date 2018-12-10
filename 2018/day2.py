"""
Author: Kyle Fauerbach
Python solution to advent of code day 2
"""

def part1():
    with open("2_1_in.txt", "r") as my_input:
        my_input = my_input.read().split()
    x2 = 0
    x3 = 0
    for box in my_input:
        for char in box:
            if box.count(char) == 2:
                x2 += 1
                break
        for char in box:
            if box.count(char) ==3:
                x3 += 1
                break
    return x2 * x3

def differences(s1, s2):
    diff = 0
    same = ''
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
        else:
            same += s1[i]
    return diff, same

def part2():
    with open("2_1_in.txt", "r") as my_input:
        my_input = my_input.read().split()
    my_input = set(my_input)

    for box1 in my_input:
        for box2 in my_input:
            diffs, same = differences(box1, box2)
            if diffs == 1:
                return same
    return None

if __name__ == "__main__":
    print(part1())
    print(part2())
