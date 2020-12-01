"""
Author: Kyle Fauerbach
Python solution to advent of code day 16
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
    matches = set()
    _, a, b, c = op
    if a < 4 and b < 4:
        # add register
        res = start.copy()
        res[c] = start[a] + start[b]
        if res == end:
            matches.add("addr")
            possible += 1
        # multiply register
        res = start.copy()
        res[c] = start[a] * start[b]
        if res == end:
            matches.add("mulr")
            possible += 1
        # bitwise and register
        res = start.copy()
        res[c] = start[a] & start[b]
        if res == end:
            matches.add("banr")
            possible += 1
        # bitwise or register
        res = start.copy()
        res[c] = start[a] | start[b]
        if res == end:
            matches.add("borr")
            possible += 1
        # gtrr
        res = start.copy()
        res[c] = 1 if res[a] > res[b] else 0
        if res == end:
            matches.add("gtrr")
            possible += 1
        # eqrr
        res = start.copy()
        res[c] = 1 if res[a] == res[b] else 0
        if res == end:
            matches.add("eqrr")
            possible += 1

    if a < 4:
        # set register
        res = start.copy()
        res[c] = res[a]
        if res == end:
            matches.add("setr")
            possible += 1
        # gtri
        res = start.copy()
        res[c] = 1 if res[a] > b else 0
        if res == end:
            matches.add("gtri")
            possible += 1
        # eqri
        res = start.copy()
        res[c] = 1 if res[a] == b else 0
        if res == end:
            matches.add("eqri")
            possible += 1
        # add immediate
        res = start[a] + b
        if end[c] == res:
            matches.add("addi")
            possible += 1
        # multiple immediate
        res = start[a] * b
        if end[c] == res:
            matches.add("muli")
            possible += 1
        # bitwise and immediate
        res = start[a] & b
        if end[c] == res:
            matches.add("bani")
            possible += 1
        # bitwise or immediate
        res = start[a] | b
        if end[c] == res:
            matches.add("bori")
            possible += 1

    if b < 4:
        # gtir
        res = start.copy()
        res[c] = 1 if a > res[b] else 0
        if res == end:
            matches.add("gtir")
            possible += 1
        # eqir
        res = start.copy()
        res[c] = 1 if a == res[b] else 0
        if res == end:
            matches.add("eqir")
            possible += 1

    # set immediate
    res = start.copy()
    res[c] = a
    if res == end:
        matches.add("seti")
        possible += 1

    return possible, matches

def addr(op, reg):
    _, a, b, c = op
    reg[c] = reg[a] + reg[b]
    return reg
def addi(op, reg):
    _, a, b, c = op
    reg[c] = reg[a] + b
    return reg
def mulr(op, reg):
    _, a, b, c = op
    reg[c] = reg[a] * reg[b]
    return reg
def muli(op, reg):
    _, a, b, c = op
    reg[c] = reg[a] * b
    return reg
def banr(op, reg):
    _, a, b, c = op
    reg[c] = reg[a] & reg[b]
    return reg
def bani(op, reg):
    _, a, b, c = op
    reg[c] = reg[a] & b
    return reg
def borr(op, reg):
    _, a, b, c = op
    reg[c] = reg[a] | reg[b]
    return reg
def bori(op, reg):
    _, a, b, c = op
    reg[c] = reg[a] | b
    return reg
def setr(op, reg):
    _, a, b, c = op
    reg[c] = reg[a]
    return reg
def seti(op, reg):
    _, a, b, c = op
    reg[c] = a
    return reg
def gtir(op, reg):
    _, a, b, c = op
    reg[c] = 1 if a > reg[b] else 0
    return reg
def gtri(op, reg):
    _, a, b, c = op
    reg[c] = 1 if reg[a] > b else 0
    return reg
def gtrr(op, reg):
    _, a, b, c = op
    reg[c] = 1 if reg[a] > reg[b] else 0
    return reg
def eqir(op, reg):
    _, a, b, c = op
    reg[c] = 1 if a == reg[b] else 0
    return reg
def eqri(op, reg):
    _, a, b, c = op
    reg[c] = 1 if reg[a] == b else 0
    return reg
def eqrr(op, reg):
    _, a, b, c = op
    reg[c] = 1 if reg[a] == reg[b] else 0
    return reg

def map_to_function(opcodes):
    for key, value in opcodes.items():
        if value == "addr":
            opcodes[key] = addr
        elif value == "addi":
            opcodes[key] = addi
        elif value == "mulr":
            opcodes[key] = mulr
        elif value == "muli":
            opcodes[key] = muli
        elif value == "banr":
            opcodes[key] = banr
        elif value == "bani":
            opcodes[key] = bani
        elif value == "borr":
            opcodes[key] = borr
        elif value == "bori":
            opcodes[key] = bori
        elif value == "setr":
            opcodes[key] = setr
        elif value == "seti":
            opcodes[key] = seti
        elif value == "gtir":
            opcodes[key] = gtir
        elif value == "gtri":
            opcodes[key] = gtri
        elif value == "gtrr":
            opcodes[key] = gtrr
        elif value == "eqir":
            opcodes[key] = eqir
        elif value == "eqri":
            opcodes[key] = eqri
        elif value == "eqrr":
            opcodes[key] = eqrr
    return opcodes

def part1():
    with open("16_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()

    ans = 0
    opcodes = {}
    found = set()
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

        num_matches, matches = test_opcodes(before, ops, after)
        if num_matches >= 3:
            ans += 1

        matches = matches - found       # get difference of the sets
        if len(matches) == 1 and ops[0] not in opcodes.keys():
            operation = matches.pop()
            opcodes[ops[0]] = operation
            found.add(operation)

    return ans, opcodes

def part2():
    _, opcodes = part1()

    # by this point, opcodes now contains a mapping of the opcode num to the operation
    # change the mapping of int->string to int->function
    opcodes = map_to_function(opcodes)

    with open("16_2_in.txt", "r") as my_input:
        cmds = my_input.readlines()

    regs = [0, 0, 0, 0]
    for cmd in cmds:
        cmd = list(map(int, cmd.split()))
        regs = opcodes[cmd[0]](cmd, regs)

    return regs[0]

if __name__ == "__main__":
    print(part1()[0])
    print(part2())
