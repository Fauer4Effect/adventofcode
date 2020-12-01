"""
Author: Kyle Fauerbach
Python solution to advent of code day 8

We just used eval because we are lazy but if we wanted to we could make it better

COMPARISONS = {
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b,
    '>=': lambda a, b: a >= b,
    '<=': lamdba a, b: a <= b,
    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
}
if (COMPARISONS[comparison])(operand1, operand2):
    do schtuff
"""

def inc(reg, val):
    """
    helper function reimplements inc opcode
    """
    return reg + val
def dec(reg, val):
    """
    helper function reimplements dec opcode
    """
    return reg - val

def part1():
    """
    answer should be 3612
    """
    with open("8_1_in.txt", "r") as my_input:
        commands = map(str.strip, my_input.readlines())
    registers = {}
    for command in commands:
        reg = command.split(' ')[0]
        registers[reg] = 0
    for command in commands:
        reg = command.split(' ')[0]
        opcode = command.split(' ')[1]
        val = int(command.split(' ')[2])
        condition = command.split('if ')[1]
        cond_reg = condition.split(' ')[0]
        if eval(str(registers[cond_reg]) + condition[condition.index(' '):]):
            if opcode == 'inc':
                registers[reg] = inc(registers[reg], val)
            elif opcode == 'dec':
                registers[reg] = dec(registers[reg], val)
    return max(registers.values())

def part2():
    """
    answer should be 3818
    """
    with open("8_1_in.txt", "r") as my_input:
        commands = map(str.strip, my_input.readlines())
    registers = {}
    maxi = 0
    for command in commands:
        reg = command.split(' ')[0]
        registers[reg] = 0
    for command in commands:
        reg = command.split(' ')[0]
        opcode = command.split(' ')[1]
        val = int(command.split(' ')[2])
        condition = command.split('if ')[1]
        cond_reg = condition.split(' ')[0]
        if eval(str(registers[cond_reg]) + condition[condition.index(' '):]):
            if opcode == 'inc':
                registers[reg] = inc(registers[reg], val)
            elif opcode == 'dec':
                registers[reg] = dec(registers[reg], val)
        maxi = max(maxi, max(registers.values()))
    return maxi

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
