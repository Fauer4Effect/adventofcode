"""
Author: Kyle Fauerbach
Python solution to advent of code day 1
"""
def part1():
    """
    answer should be 1136
    """
    with open("1_1_in.txt", "r") as my_input:
        my_input = my_input.read()
    prev = ""
    total = 0
    num = ""
    for num in my_input:
        if prev == "":
            first = num
        if num == prev:
            total += int(num)
        prev = num
    if num == first:
        total += int(num)
    return total

def part2():
    """
    answer should be 1092
    """
    with open("1_1_in.txt", "r") as my_input:
        my_input = list(my_input.read())
    length = len(my_input)
    mod = length / 2
    total = 0
    for i in range(length):
        if my_input[i] == my_input[(i + mod) % length]:
            total += int(my_input[i])
    return total

if __name__ == "__main__":
    print "part 1", part1()
    print "part 2", part2()
