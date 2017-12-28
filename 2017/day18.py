"""
Author: Kyle Fauerbach
Python solution to advent of code day 18
"""
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

if __name__ == "__main__":
    print "part1", part1()
