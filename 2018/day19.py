"""
Author: Kyle Fauerbach
Python solution to advent of code day 16
"""

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

def part1():
    with open("19_1_in.txt", "r") as my_input:
        cmds = list(map(str.strip, my_input.readlines()))

    opcodes = {"addr": addr, "addi": addi, "mulr": mulr, "muli": muli, "banr": banr, "bani": bani,
               "borr": borr, "bori": bori, "setr": setr, "seti": seti, "gtir": gtir, "gtri": gtri,
               "gtrr": gtrr, "eqir": eqir, "eqri": eqri, "eqrr": eqrr}

    regs = [0, 0, 0, 0, 0, 0]
    ip = 0
    # instruction pointer bound to register 5
    bound = 5

    # as long as the ip points to a valid instruction
    while ip < len(cmds):
        # print("ip={} {}".format(ip, regs), end=' ')
        # write ip to the register
        regs[bound] = ip

        # get the current instruction
        cur_inst = cmds[ip].split()
        op, a, b, c = cur_inst
        a = int(a)
        b = int(b)
        c = int(c)

        # execute the instruction
        regs = opcodes[op]([op, a, b, c], regs)

        # write back the value to ip
        ip = regs[bound]

        # add one to the ip
        ip += 1

        # print("{} {}".format(cur_inst, regs))

    return regs[0]

def part2():
    # changing the registers really increases the number of instructions that are evaluated
    # so we probably need to understand what is goind on and find a way to optimize the program
    # instruction pointer still bound to register 5
    """
    REGISTERS = A, B, C, D, E IP
------------------------------------------------------------------------------------------------
    FIRST THING IS CONVERT ALL TO NORMAL INSTRUCTIONS
    0   addi 5 16 5 # IP += 16
    1   seti 1 9 1  # B = 1
    2   seti 1 5 4  # E = 1
    3   mulr 1 4 3  # D = B * E
    4   eqrr 3 2 3  # D = (D == C)
    5   addr 3 5 5  # IP += D
    6   addi 5 1 5  # IP += 1
    7   addr 1 0 0  # A += B
    8   addi 4 1 4  # E += 1
    9   gtrr 4 2 3  # D = (E > C)
    10  addr 5 3 5  # IP += D
    11  seti 2 4 5  # IP = 2
    12  addi 1 1 1  # B += 1
    13  gtrr 1 2 3  # D = (B > C)
    14  addr 3 5 5  # IP += D
    15  seti 1 9 5  # IP = 1
    16  mulr 5 5 5  # IP = IP*IP
    17  addi 2 2 2  # C += 2
    18  mulr 2 2 2  # C = C * C
    19  mulr 5 2 2  # C = IP * C
    20  muli 2 11 2 # C = 11 * C
    21  addi 3 8 3  # D += 8
    22  mulr 3 5 3  # D = IP * D
    23  addi 3 16 3 # D += 16
    24  addr 2 3 2  # C += D
    25  addr 5 0 5  # IP += A
    26  seti 0 7 5  # IP = 0
    27  setr 5 3 3  # D = IP
    28  mulr 3 5 3  # D = IP * D
    29  addr 5 3 3  # D += IP
    30  mulr 5 3 3  # D = IP * D
    31  muli 3 14 3 # D = 14 * D
    32  mulr 3 5 3  # D = IP * D
    33  addr 2 3 2  # C += D
    34  seti 0 1 0  # a = 0
    35  seti 0 6 5  # IP = 0
------------------------------------------------------------------------------------------------
    THEN CONVERT IP to it's instruction value when it's an operand
    0   addi 5 16 5 # IP += 16
    1   seti 1 9 1  # B = 1
    2   seti 1 5 4  # E = 1
    3   mulr 1 4 3  # D = B * E
    4   eqrr 3 2 3  # D = (D == C)
    5   addr 3 5 5  # IP += D
    6   addi 5 1 5  # IP += 1
    7   addr 1 0 0  # A += B
    8   addi 4 1 4  # E += 1
    9   gtrr 4 2 3  # D = (E > C)
    10  addr 5 3 5  # IP += D
    11  seti 2 4 5  # IP = 2
    12  addi 1 1 1  # B += 1
    13  gtrr 1 2 3  # D = (B > C)
    14  addr 3 5 5  # IP += D
    15  seti 1 9 5  # IP = 1
    16  mulr 5 5 5  # IP = 16 * 16
    17  addi 2 2 2  # C += 2
    18  mulr 2 2 2  # C = C * C
    19  mulr 5 2 2  # C = 19 * C
    20  muli 2 11 2 # C = 11 * C
    21  addi 3 8 3  # D += 8
    22  mulr 3 5 3  # D = 22 * D
    23  addi 3 16 3 # D += 16
    24  addr 2 3 2  # C += D
    25  addr 5 0 5  # IP += A
    26  seti 0 7 5  # IP = 0
    27  setr 5 3 3  # D = 27
    28  mulr 3 5 3  # D = 28 * D
    29  addr 5 3 3  # D += 29
    30  mulr 5 3 3  # D = 30 * D
    31  muli 3 14 3 # D = 14 * D
    32  mulr 3 5 3  # D = 32 * D
    33  addr 2 3 2  # C += D
    34  seti 0 1 0  # a = 0
    35  seti 0 6 5  # IP = 0
------------------------------------------------------------------------------------------------
    NEXT FOLLOW THE ACTUAL FLOW OF THE PROGRAM
    0   addi 5 16 5 # IP += 16              IP = 0 + 16 + 1 -> GOTO 17

    17  addi 2 2 2  # C += 2                c = 2
    18  mulr 2 2 2  # C = C * C             c = 4
    19  mulr 5 2 2  # C = 19 * C            c = 76
    20  muli 2 11 2 # C = 11 * C            c = 836
    21  addi 3 8 3  # D += 8                d = 8
    22  mulr 3 5 3  # D = 22 * D            d = 176
    23  addi 3 16 3 # D += 16               d = 192
    24  addr 2 3 2  # C += D                c = 1028
    25  addr 5 0 5  # IP += A               IP = 25 + A (a=1) = 25 + 1 + 1 = 27 -> GOTO 27

    27  setr 5 3 3  # D = 27                d = 27
    28  mulr 3 5 3  # D = 28 * D            d = 756
    29  addr 5 3 3  # D += 29               d = 785
    30  mulr 5 3 3  # D = 30 * D            d = 23550
    31  muli 3 14 3 # D = 14 * D            d = 329700
    32  mulr 3 5 3  # D = 32 * D            d = 10550400
    33  addr 2 3 2  # C += D                c = 10551428
    34  seti 0 1 0  # a = 0                 a = 0
    35  seti 0 6 5  # IP = 0                IP = 0 + 1 = 1 -> GOTO 1

    1   seti 1 9 1  # B = 1                 b = 1
    2   seti 1 5 4  # E = 1                 e = 1

    3   mulr 1 4 3  # D = B * E             d = b * e
    4   eqrr 3 2 3  # D = (D == C)          d = (d == c)
    5   addr 3 5 5  # IP += D               if d == c d = 1 -> IP = 5 + 1 + 1 = 7 -> GOTO 7
                                            if d != c d = 0 -> IP = 5 + 0 + 1 = 6
    6   addi 5 1 5  # IP += 1               IP = 6 + 1 + 1 = 8 -> GOTO 8

    7   addr 1 0 0  # A += B                a += b
    8   addi 4 1 4  # E += 1                e += 1

    9   gtrr 4 2 3  # D = (E > C)           d = ( e > c)
    10  addr 5 3 5  # IP += D               if e > c d = 1 -> IP = 10 + 1 + 1 = 12
                                            if e <= c d = 0 -> IP = 10 + 0 + 1 = 11
    11  seti 2 4 5  # IP = 2                IP = 2 -> GOTO 3

    12  addi 1 1 1  # B += 1                b += 1

    13  gtrr 1 2 3  # D = (B > C)           d = b > c
    14  addr 3 5 5  # IP += D               if d > c d = 1 -> IP = 14 + 1 + 1 = 16
                                            if d <= c d = 0 -> IP = 14 + 0 + 1 = 15
    15  seti 1 9 5  # IP = 1                IP = 1 -> GOTO 2
    16  mulr 5 5 5  # IP = 16 * 16          IP = 16 * 16 -> Break
------------------------------------------------------------------------------------------------
    CONVERT SOME OF THOSE INTO MORE READABLE CODE
    0   addi 5 16 5 # IP += 16              GOTO 17

    17  addi 2 2 2  # C += 2                c = 2
    18  mulr 2 2 2  # C = C * C             c = 4
    19  mulr 5 2 2  # C = 19 * C            c = 76
    20  muli 2 11 2 # C = 11 * C            c = 836
    21  addi 3 8 3  # D += 8                d = 8
    22  mulr 3 5 3  # D = 22 * D            d = 176
    23  addi 3 16 3 # D += 16               d = 192
    24  addr 2 3 2  # C += D                c = 1028
    25  addr 5 0 5  # IP += A               GOTO 27

    27  setr 5 3 3  # D = 27                d = 27
    28  mulr 3 5 3  # D = 28 * D            d = 756
    29  addr 5 3 3  # D += 29               d = 785
    30  mulr 5 3 3  # D = 30 * D            d = 23550
    31  muli 3 14 3 # D = 14 * D            d = 329700
    32  mulr 3 5 3  # D = 32 * D            d = 10550400
    33  addr 2 3 2  # C += D                c = 10551428
    34  seti 0 1 0  # a = 0                 a = 0
    35  seti 0 6 5  # IP = 0                GOTO 1

    c = 10551428
    d = 10550400

    1   seti 1 9 1  # B = 1                 b = 1
    2   seti 1 5 4  # E = 1                 e = 1


    if ((b*e) == c) {
        GOTO 7
    } else {
        GOTO 8
    }
    3   mulr 1 4 3  # D = B * E             d = b * e
    4   eqrr 3 2 3  # D = (D == C)          d = (d == c)
    5   addr 3 5 5  # IP += D               if d == c d = 1 -> IP = 5 + 1 + 1 = 7
                                            if d != c d = 0 -> IP = 5 + 0 + 1 = 6
    6   addi 5 1 5  # IP += 1               IP = 6 + 1 + 1 = 8

    7   addr 1 0 0  # A += B                a += b
    8   addi 4 1 4  # E += 1                e += 1

    if (e > c) {
        GOTO 12
    } else {
        GOTO 3
    }
    9   gtrr 4 2 3  # D = (E > C)           d = ( e > c)
    10  addr 5 3 5  # IP += D               if e > c d = 1 -> IP = 10 + 1 + 1 = 12
                                            if e <= c d = 0 -> IP = 10 + 0 + 1 = 11
    11  seti 2 4 5  # IP = 2                IP = 2 -> GOTO 3

    12  addi 1 1 1  # B += 1                b += 1

    if (b > c) {
        return
    } else {
        GOTO 3
    }
    13  gtrr 1 2 3  # D = (B > C)           d = b > c
    14  addr 3 5 5  # IP += D               if d > c d = 1 -> IP = 14 + 1 + 1 = 16
                                            if d <= c d = 0 -> IP = 14 + 0 + 1 = 15
    15  seti 1 9 5  # IP = 1                IP = 1 -> GOTO 2
    16  mulr 5 5 5  # IP = 16 * 16          IP = 16 * 16 -> Break
------------------------------------------------------------------------------------------------
    PUTTING THIS INTO MORE ORDER
    a = 0
    c = 10551428
    d = 10550400
    1:  b = 1
    2:  e = 1
    3:  if ((b*e) == c) {
            GOTO 7
        } else {
            GOTO 8
        }
    7:  a += b
    8:  e += 1
    9:  if (e > c) {
            GOTO 12
        } else {
            GOTO 3
        }

    12: b += 1
    13: if (b > c) {
            return
        } else {
            GOTO 3
        }
------------------------------------------------------------------------------------------------
    COLLAPSE IT DOWN
    a = 0
    c = 10551428
    d = 10550400

    if (b*e) == c:
        a += b
    else:
        e += 1
        if (e > c):
            b += 1
            if (b > c):
                return
            else:
                if (b*e) == c:
                    ....
                    ...
        else :
            if (b*e) == c:
                .....
                ....
------------------------------------------------------------------------------------------------
    FINALLY PYTHON
    a = 0
    c = 10551428
    d = 10550400
    for b in range(1, c+1):
        for e in range(1, c+1):
            if b*e == c:
                a += b
------------------------------------------------------------------------------------------------
    SO WHAT IS THIS ACTUALLY DOING??????????

    we are summing the factors of c
    a is the running total and starts at 0
    we check b from 1 to c, looking if it is a factor
    b is a factor if there is another integer e such that b*e == c
    so it's just a really bad factoring algorithm
------------------------------------------------------------------------------------------------
    From there we can just use wolfram alpha "sum of factors of 10551428"
    of use this super easy code that takes advantage of optimized modulo in python
------------------------------------------------------------------------------------------------
    Funnily enough the same principle works for part 1, the difference being that part 1 looks
        0   addi 5 16 5 # IP += 16              IP = 0 + 16 + 1 -> GOTO 17

        17  addi 2 2 2  # C += 2                c = 2
        18  mulr 2 2 2  # C = C * C             c = 4
        19  mulr 5 2 2  # C = 19 * C            c = 76
        20  muli 2 11 2 # C = 11 * C            c = 836
        21  addi 3 8 3  # D += 8                d = 8
        22  mulr 3 5 3  # D = 22 * D            d = 176
        23  addi 3 16 3 # D += 16               d = 192
        24  addr 2 3 2  # C += D                c = 1028
        25  addr 5 0 5  # IP += A               IP = 25 + A (a=0) = 25 + 0 + 1 = 26 -> GOTO 26

        26  seti 0 7 5  # IP = 0                IP = 0 + 1 -> GOTO 1

        1   seti 1 9 1  # B = 1                 b = 1
        2   seti 1 5 4  # E = 1                 e = 1

        3   mulr 1 4 3  # D = B * E             d = b * e
        4   eqrr 3 2 3  # D = (D == C)          d = (d == c)
        5   addr 3 5 5  # IP += D               if d == c d = 1 -> IP = 5 + 1 + 1 = 7 -> GOTO 7
                                                if d != c d = 0 -> IP = 5 + 0 + 1 = 6
        6   addi 5 1 5  # IP += 1               IP = 6 + 1 + 1 = 8 -> GOTO 8

        7   addr 1 0 0  # A += B                a += b
        8   addi 4 1 4  # E += 1                e += 1

        9   gtrr 4 2 3  # D = (E > C)           d = ( e > c)
        10  addr 5 3 5  # IP += D               if e > c d = 1 -> IP = 10 + 1 + 1 = 12
                                                if e <= c d = 0 -> IP = 10 + 0 + 1 = 11
        11  seti 2 4 5  # IP = 2                IP = 2 -> GOTO 3

        12  addi 1 1 1  # B += 1                b += 1

        13  gtrr 1 2 3  # D = (B > C)           d = b > c
        14  addr 3 5 5  # IP += D               if d > c d = 1 -> IP = 14 + 1 + 1 = 16
                                                if d <= c d = 0 -> IP = 14 + 0 + 1 = 15
        15  seti 1 9 5  # IP = 1                IP = 1 -> GOTO 2
        16  mulr 5 5 5  # IP = 16 * 16          IP = 16 * 16 -> Break

    So it's the same in part 1 we are just finding the sum of the factors of 1028, which is much
    smaller so it's more efficient to do it in their super bad way, but we can make the code below
    also work for part 1
    """

    c = 10551428
    total = 0
    for i in range(1, c+1):
        if c % i == 0:
            total += i
    return total

if __name__ == "__main__":
    print(part1())
    print(part2())
