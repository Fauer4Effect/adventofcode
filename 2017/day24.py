"""
Author: Kyle Fauerbach
Python solution to advent of code day 24
"""

from collections import defaultdict, deque

def solve():
    """
    answer should be
    """
    with open("24_1_in.txt", "r") as my_input:
        all_pipes = [map(int, line.strip().split('/')) for line in my_input]
    lengths = []
    def find_next(port, remaining, cur_total, length):
        lengths.append([length, cur_total])
        for next_pipe in remaining:
            x, y = next_pipe
            if x == port or y == port:
                new_remaining = [new_pipe for new_pipe in remaining if new_pipe != next_pipe]
                find_next(x if y == port else y, new_remaining, cur_total + sum(next_pipe), length + 1) 
    for pipe in all_pipes:
        x, y = pipe
        if x == 0 or y == 0:
            remaining = [new_pipe for new_pipe in all_pipes if new_pipe != pipe]
            find_next(x if y == 0 else y, remaining, sum(pipe), 1)
    print "part1", max([length[1] for length in lengths])

    longest = max([length[0] for length in lengths])
    print "part2", max([length[1] for length in lengths if length[0] == longest])

if __name__ == "__main__":
    solve()
