"""
Author: Kyle Fauerbach
Python solution to advent of code day 15
"""

def test_opcodes(start, op, end):
    """
    Args: start[] = startingregister values
          op[]    = opcode A B C
          end[]   = ending register values
    return: Number of opcodes that would match
    """
    possible = 0
    opcode, a, b, c = op
    if a < 4 and b < 4:
        # add register
        res = start[a] + start[b]
        if res == end[c]:
            possible += 1
        # multiply register
        res = start[a] * start[b]
        if res == end[c]:
            possible += 1
        # bitwise and register
        res = start[a] & start[b]
        if res == end[c]:
            possible += 1
        # bitwise or register
        res = start[a] ^ start[b]
        if res == end[c]:
            possible += 1
    

    return possible

def part1():

    return None

def part2():

    return None

if __name__ == "__main__":
    print(part1())
    print(part2())