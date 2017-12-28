"""
Author: Kyle Fauerbach
Python solution to advent of code day 18
"""

from collections import deque

def part1():
    """
    answer should be
    """
    with open("18_1_in.txt", "r") as my_input:
        instructions = map(str.strip, my_input.readlines())
    cur_index = 0
    last_played = 0
    registers = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}
    while True:
        cur_inst = instructions[cur_index]
        cur_index += 1
        cur_inst = cur_inst.split(' ')
        opcode = cur_inst[0]
        if opcode == 'snd':
            if cur_inst[1] in registers:
                last_played = registers[cur_inst[1]]
            else:
                last_played = int(cur_inst[1])
        elif opcode == 'set':
            if cur_inst[2] in registers.keys():
                registers[cur_inst[1]] = registers[cur_inst[2]]
            else:
                registers[cur_inst[1]] = int(cur_inst[2])
        elif opcode == 'add':
            if cur_inst[2] in registers.keys():
                registers[cur_inst[1]] += registers[cur_inst[2]]
            else:
                registers[cur_inst[1]] += int(cur_inst[2])
        elif opcode == 'mul':
            if cur_inst[2] in registers.keys():
                registers[cur_inst[1]] *= registers[cur_inst[2]]
            else:
                registers[cur_inst[1]] *= int(cur_inst[2])
        elif opcode == 'mod':
            if cur_inst[2] in registers.keys():
                registers[cur_inst[1]] = registers[cur_inst[1]] % registers[cur_inst[2]]
            else:
                registers[cur_inst[1]] = registers[cur_inst[1]] % int(cur_inst[2])
        elif opcode == 'jgz':
            if cur_inst[1] in registers.keys():
                if registers[cur_inst[1]] > 0:
                    cur_index = cur_index - 1 + int(cur_inst[2])
            elif int(cur_inst[1]) > 0:
                cur_index = cur_index - 1 + int(cur_inst[2])
        elif opcode == 'rcv':
            if cur_inst[1] in registers.keys() and registers[cur_inst[1]] != 0:
                break
            elif int(cur_inst[1]) != 0:
                break
    return last_played

def part2():
    """
    the programs can run asynchronous so we will run the first until it waits
    then run second until it waits
    and as long as first and second aren't waiting at the same time we continue
    one tricky thing is decrementing the program counter so we don't skip the wait
    instruction
    answer should be 8001
    """
    with open("18_1_in.txt", "r") as my_input:
        instructions = map(str.strip, my_input.readlines())

    reg0 = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}
    reg1 = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 1}
    index0 = 0
    index1 = 0
    queue0 = deque()
    queue1 = deque()
    waiting0 = False
    waiting1 = False
    sent1 = 0

    while not (waiting0 and waiting1):
        while True:
            cur_inst = instructions[index0]
            index0 += 1
            cur_inst = cur_inst.split(' ')
            opcode = cur_inst[0]
            if opcode == 'snd':
                waiting1 = False
                if cur_inst[1] in reg0:
                    queue1.append(reg0[cur_inst[1]])
                else:
                    queue1.append(int(cur_inst[1]))
            elif opcode == 'set':
                if cur_inst[2] in reg0.keys():
                    reg0[cur_inst[1]] = reg0[cur_inst[2]]
                else:
                    reg0[cur_inst[1]] = int(cur_inst[2])
            elif opcode == 'add':
                if cur_inst[2] in reg0.keys():
                    reg0[cur_inst[1]] += reg0[cur_inst[2]]
                else:
                    reg0[cur_inst[1]] += int(cur_inst[2])
            elif opcode == 'mul':
                if cur_inst[2] in reg0.keys():
                    reg0[cur_inst[1]] *= reg0[cur_inst[2]]
                else:
                    reg0[cur_inst[1]] *= int(cur_inst[2])
            elif opcode == 'mod':
                if cur_inst[2] in reg0.keys():
                    reg0[cur_inst[1]] = reg0[cur_inst[1]] % reg0[cur_inst[2]]
                else:
                    reg0[cur_inst[1]] = reg0[cur_inst[1]] % int(cur_inst[2])
            elif opcode == 'jgz':
                if cur_inst[1] in reg0.keys():
                    if reg0[cur_inst[1]] > 0:
                        index0 = index0 - 1 + int(cur_inst[2])
                elif int(cur_inst[1]) > 0:
                    index0 = index0 - 1 + int(cur_inst[2])
            elif opcode == 'rcv':
                if not queue0:
                    waiting0 = True
                    index0 -= 1
                    break
                else:
                    reg0[cur_inst[1]] = queue0.popleft()

        while True:
            cur_inst = instructions[index1]
            index1 += 1
            cur_inst = cur_inst.split(' ')
            opcode = cur_inst[0]
            if opcode == 'snd':
                waiting0 = False
                sent1 += 1
                if cur_inst[1] in reg1:
                    queue0.append(reg1[cur_inst[1]])
                else:
                    queue0.append(int(cur_inst[1]))
            elif opcode == 'set':
                if cur_inst[2] in reg1.keys():
                    reg1[cur_inst[1]] = reg1[cur_inst[2]]
                else:
                    reg1[cur_inst[1]] = int(cur_inst[2])
            elif opcode == 'add':
                if cur_inst[2] in reg1.keys():
                    reg1[cur_inst[1]] += reg1[cur_inst[2]]
                else:
                    reg1[cur_inst[1]] += int(cur_inst[2])
            elif opcode == 'mul':
                if cur_inst[2] in reg1.keys():
                    reg1[cur_inst[1]] *= reg1[cur_inst[2]]
                else:
                    reg1[cur_inst[1]] *= int(cur_inst[2])
            elif opcode == 'mod':
                if cur_inst[2] in reg1.keys():
                    reg1[cur_inst[1]] = reg1[cur_inst[1]] % reg1[cur_inst[2]]
                else:
                    reg1[cur_inst[1]] = reg1[cur_inst[1]] % int(cur_inst[2])
            elif opcode == 'jgz':
                if cur_inst[1] in reg1.keys():
                    if reg1[cur_inst[1]] > 0:
                        if cur_inst[2] in reg1.keys():
                            index1 = index1 - 1 + reg1[cur_inst[2]]
                        else:
                            index1 = index1 - 1 + int(cur_inst[2])
                elif int(cur_inst[1]) > 0:
                    index1 = index1 - 1 + int(cur_inst[2])
            elif opcode == 'rcv':
                if not queue1:
                    waiting1 = True
                    index1 -= 1
                    break
                else:
                    reg1[cur_inst[1]] = queue1.popleft()
    return sent1

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
