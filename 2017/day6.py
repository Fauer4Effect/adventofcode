"""
Author: Kyle Fauerbach
Python solution to advent of code day 6
"""

def rep(memory):
    """
    convert the list to a hashable string to store it in the set
    """
    return ' '.join(map(str, memory))

def part1():
    """
    anwer should be 3156
    """
    with open("6_1_in.txt", "r") as my_input:
        mem = map(int, my_input.read().strip().split('\t'))
    rounds = 0
    seen = set()
    while not rep(mem) in seen:
        seen.add(rep(mem))
        biggest = max(mem)
        index = mem.index(biggest)
        mem[index] = 0
        index += 1
        while biggest > 0:
            mem[index % 16] += 1
            index += 1
            biggest -= 1
        rounds += 1
    return rounds

def part2():
    """
    anwer should be 1610
    """
    with open("6_1_in.txt", "r") as my_input:
        mem = map(int, my_input.read().strip().split('\t'))
    rounds = 0
    seen = {}
    while rep(mem) not in seen.values():
        seen[rounds] = rep(mem)
        biggest = max(mem)
        index = mem.index(biggest)
        mem[index] = 0
        index += 1
        while biggest > 0:
            mem[index % 16] += 1
            index += 1
            biggest -= 1
        rounds += 1
    cur = rep(mem)
    for k, v in seen.iteritems():
        if v == cur:
            return rounds - k

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
