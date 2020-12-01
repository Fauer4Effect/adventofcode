"""
Author: Kyle Fauerbach
Python solution to advent of code day 25
"""

from collections import defaultdict

def part1():
    """
    answer should be 4387
    """
    tape = defaultdict(int)
    state = 'a'
    index = 0
    for _ in range(12208951):
        if index not in tape:
            tape[index] = 0
        if state == 'a':
            if tape[index] == 0:
                tape[index] = 1
                index += 1
                state = 'b'
            elif tape[index] == 1:
                tape[index] = 0
                index -= 1
                state = 'e'
        elif state == 'b':
            if tape[index] == 0:
                tape[index] = 1
                index -= 1
                state = 'c'
            elif tape[index] == 1:
                tape[index] = 0
                index += 1
                state = 'a'
        elif state == 'c':
            if tape[index] == 0:
                tape[index] = 1
                index -= 1
                state = 'd'
            elif tape[index] == 1:
                tape[index] = 0
                index += 1
                state = 'c'
        elif state == 'd':
            if tape[index] == 0:
                tape[index] = 1
                index -= 1
                state = 'e'
            elif tape[index] == 1:
                tape[index] = 0
                index -= 1
                state = 'f'
        elif state == 'e':
            if tape[index] == 0:
                tape[index] = 1
                index -= 1
                state = 'a'
            elif tape[index] == 1:
                tape[index] = 1
                index -= 1
                state = 'c'
        elif state == 'f':
            if tape[index] == 0:
                tape[index] = 1
                index -= 1
                state = 'e'
            elif tape[index] == 1:
                tape[index] = 1
                index += 1
                state = 'a'
    my_sum = 0
    for val in tape.itervalues():
        my_sum += val
    return my_sum

if __name__ == "__main__":
    print "part1", part1()
