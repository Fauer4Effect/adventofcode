"""
Author: Kyle Fauerbach
Python solution to advent of code day 12
"""
def part1():
    """
    answer should be 175
    """
    with open("12_1_in.txt", "r") as my_input:
        my_in = map(str.strip, my_input.readlines())
    pipes = {}
    for pipe in my_in:
        pipe = pipe.split(' <-> ')
        pipes[pipe[0]] = pipe[1].split(', ')
    neighbors = pipes['0']
    seen = set()
    while neighbors:
        explore = neighbors.pop()
        if explore not in seen:
            seen.add(explore)
            neighbors += pipes[explore]
    return len(seen)

def part2():
    """
    answer should be 213
    """
    with open("12_1_in.txt", "r") as my_input:
        my_in = map(str.strip, my_input.readlines())
    pipes = {}
    all_programs = set()
    for pipe in my_in:
        pipe = pipe.split(' <-> ')
        all_programs.add(pipe[0])
        pipes[pipe[0]] = pipe[1].split(', ')
    explored = set()
    groups = 0
    for program in all_programs:
        if program not in explored:
            groups += 1
            neighbors = pipes[program]
            seen = set()
            while neighbors:
                explore = neighbors.pop()
                if explore not in seen:
                    seen.add(explore)
                    neighbors += pipes[explore]
            explored = explored.union(seen)
    return groups

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()