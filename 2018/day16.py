"""
Author: Kyle Fauerbach
Python solution to advent of code day 15
"""

import re

def test_opcodes(start, op, end):
    """
    Args: start[] = startingregister values
          op[]    = opcode A B C
          end[]   = ending register values
    return: Number of opcodes that would match
    """
    possible = 0
    _, a, b, c = op
    if a < 4 and b < 4:
        # add register
        res = start.copy()
        res[c] = start[a] + start[b]
        if res == end:
            possible += 1
        # multiply register
        res = start.copy()
        res[c] = start[a] * start[b]
        if res == end:
            possible += 1
        # bitwise and register
        res = start.copy()
        res[c] = start[a] & start[b]
        if res == end:
            possible += 1
        # bitwise or register
        res = start.copy()
        res[c] = start[a] | start[b]
        if res == end:
            possible += 1
        # gtrr
        res = start.copy()
        if res[a] > res[b]:
            res[c] = 1
        else:
            res[c] = 0
        if res == end:
            possible += 1
        # eqrr
        res = start.copy()
        if res[a] == res[b]:
            res[c] = 1
        else:
            res[c] = 0
        if res == end:
            possible += 1

    if a < 4:
        # set register
        res = start.copy()
        res[c] = res[a]
        if res == end:
            possible += 1
        # gtri
        res = start.copy()
        if res[a] > b:
            res[c] = 1
        else:
            res[c] = 0
        if res == end:
            possible += 1
        # eqri
        res = start.copy()
        if res[a] == b:
            res[c] = 1
        else:
            res[c] = 0
        if res == end:
            possible += 1
        # add immediate
        res = start[a] + b
        if end[c] == res:
            possible += 1
        # multiple immediate
        res = start[a] * b
        if end[c] == res:
            possible += 1
        # bitwise and immediate
        res = start[a] & b
        if end[c] == res:
            possible += 1
        # bitwise or immediate
        res = start[a] | b
        if end[c] == res:
            possible += 1

    if b < 4:
        # gtir
        res = start.copy()
        if a > res[b]:
            res[c] = 1
        else:
            res[c] = 0
        if res == end:
            possible += 1
        # eqir
        res = start.copy()
        if a == res[b]:
            res[c] = 1
        else:
            res[c] = 0
        if res == end:
            possible += 1
    
    # set immediate
    res = start.copy()
    res[c] = a
    if res == end:
        possible += 1

    return possible

def part1():
    with open("16_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()

    ans = 0
    # by 4 because we have to account for that blank line in between
    for i in range(0, len(my_input)-2, 4):
        before = my_input[i].strip()
        before = re.findall(r"\d, \d, \d, \d", before)[0].split(', ')
        before = list(map(int, before))

        ops = my_input[i+1].strip().split()
        ops = list(map(int, ops))

        after = my_input[i+2].strip()
        after = re.findall(r"\d, \d, \d, \d", after)[0].split(', ')
        after = list(map(int, after))
        
        matches = test_opcodes(before, ops, after)
        if matches >= 3:
            ans += 1

    return ans

def part2():

    return None

if __name__ == "__main__":
    print(part1())
    print(part2())