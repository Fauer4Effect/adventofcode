"""
Author: Kyle Fauerbach
Python solution to advent of code day 2
"""
def part1():
    """
    answer should be 44887
    """
    checksum = 0
    with open("2_1_in.txt", "r") as my_input:
        lines = my_input.readlines()
    for line in lines:
        line = map(int, line.strip().split('\t'))
        checksum += (max(line) - min(line))
    return checksum

def part2():
    """
    Answer should be 242
    """
    checksum = 0
    with open("2_1_in.txt", "r") as my_input:
        lines = my_input.readlines()
    for line in lines:
        line = map(int, line.strip().split('\t'))
        divisible = [(i, j) for i in line for j in line if i%j == 0 and i != j]
        checksum += (divisible[0][0] / divisible[0][1])
    return checksum

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
