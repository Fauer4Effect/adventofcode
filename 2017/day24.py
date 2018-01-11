"""
Author: Kyle Fauerbach
Python solution to advent of code day 24
"""

from collections import defaultdict, deque

def part1():
    """
    answer should be
    """
    with open("24_1_in.txt", "r") as my_input:
        all_pipes = map(str.strip, my_input.readlines())
    pipes = defaultdict(list)
    for pipe in all_pipes:
        pipe1 = pipe.split('/')
        pipes[pipe1[0]].append(pipe)
        pipes[pipe1[1]] .append(pipe)
    explore = deque()
    used = set()
    need = '0'
    explore.extend(pipes[need])
    paths = []
    path = []
    while explore:
        cur_pipe = explore.pop()
        if cur_pipe not in used:
            print path
            pipe1 = cur_pipe.split('/')
            if pipe1[0] == '0' or pipe1[1] == '0':
                used = set()
                need = '0'
                path = []
            if pipe1[0] == need:
                need = pipe1[1]
            elif pipe1[1] == need:
                need = pipe1[0]
            else:
                need = pipe1[0]
            explore.extend(pipes[need])
            used.add(cur_pipe)
            path.append(cur_pipe)
            paths.append(path)

if __name__ == "__main__":
    print "part1", part1()
