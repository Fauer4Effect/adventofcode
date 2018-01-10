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
    bridges = []
    need = '0'
    valid = deque(pipes[need])
    used = set()
    while valid:
        cur_pipe = valid.pop()
        if cur_pipe not in used:
            print cur_pipe
            pipe = cur_pipe.split('/')
            if pipe[0] == need:
                need = pipe[1]
            else:
                need = pipe[0]
            valid.extend(pipes[need])
            used.add(cur_pipe)

if __name__ == "__main__":
    print "part1", part1()
