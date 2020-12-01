"""
Author: Kyle Fauerbach
Python solution to advent of code day 23
"""
def part1():
    """
    answer should be 3969
    """
    with open("23_1_in.txt", "r") as my_input:
        instructions = map(str.strip, my_input.readlines())
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
    eip = 0
    num_mul = 0
    while eip < len(instructions):
        cur_inst = instructions[eip].split(' ')
        if cur_inst[0] == 'set':
            eip += 1
            if cur_inst[2] in registers:
                registers[cur_inst[1]] = registers[cur_inst[2]]
            else:
                registers[cur_inst[1]] = int(cur_inst[2])
        if cur_inst[0] == 'sub':
            eip += 1
            if cur_inst[2] in registers:
                registers[cur_inst[1]] -= registers[cur_inst[2]]
            else:
                registers[cur_inst[1]] -= int(cur_inst[2])
        if cur_inst[0] == 'mul':
            eip += 1
            num_mul += 1
            if cur_inst[2] in registers:
                registers[cur_inst[1]] *= registers[cur_inst[2]]
            else:
                registers[cur_inst[1]] *= int(cur_inst[2])
        if cur_inst[0] == 'jnz':
            if cur_inst[1] in registers:
                if registers[cur_inst[1]] != 0 and cur_inst[2] in registers:
                    eip += registers[cur_inst[2]]
                elif registers[cur_inst[1]] != 0:
                    eip += int(cur_inst[2])
                else:
                    eip += 1
            elif int(cur_inst[1]) != 0:
                if cur_inst[2] in registers:
                    eip += registers[cur_inst[2]]
                else:
                    eip += int(cur_inst[2])
            else:
                eip += 1
    return num_mul

def isPrime(number):
    """
    close to Lucas' primality test. In order to be complete, we would need to check
    that 2**((Number-1)/k) for all k prime factors of Number-1 are also equal to 1.
    The wikipedia page gives the full complete algorithm
    """
    return 2 in [pow(2, number, number)]

def part2():
    """
-----------------------------------------------------------
set b 65        b = 65
set c b         c = b
jnz a 2         if a != 0 we will execute starting at mul b 100
jnz 1 5         else we will start at set f 1
mul b 100
sub b -100000   this block of code is b = b*100 - -100000
set c b         c = b - -17000
sub c -17000
    set f 1         f = 1
    set d 2         d = 2
        set e 2         e = 2
            set g d         g = d
            mul g e         g = g * e
            sub g b         g = g - b
            jnz g 2         if g == 0
            set f 0             f = 0
            sub e -1        e = e - -1
            set g e         g = e
            sub g b         g = g - b
            jnz g -8        if g != 0 go back to set g d
        sub d -1        d = d - -1
        set g d         g = d
        sub g b         g = g - b
        jnz g -13       if g != go back to set e = 2
    jnz f 2         if f == 0
    sub h -1            h = h - -1
    set g b         g = b
    sub g c         g = g - c
    jnz g 2         if g != 0 go to sub b -17
    jnz 1 3         if g == 0 exit
    sub b -17
    jnz 1 -23
-----------------------------------------------------------
b = 65
c = b = 65
if a != 0
    b = b * 100 + 100000
    c = b + 17000

f = 1
d = 2
    e = 2
        g = d * e - b
        if g == 0
            f = 0
        e = e + 1
        g = e - b
        if g != 0 loop to g = d * e - b
    d = d + 1
    g = d - b
    if g != 0 loop to e = 2
if f == 0
    h = h + 1
g = b - c
if g == 0
    break
b = b + 17
loop to f = 1
-----------------------------------------------------------
a is always not equal to 0

b = 65 * 100 + 100000
c = b + 17000

we exit when b - c = 0 so we are looping from b to c
b = b + 17 at very end tells us that we are incrementing by 17 in our loop
for b in range(b, c+1, 17):
    f = 1

    we exit when d - b = 0 so looping from d(which is 2) to b
    d = d + 1 means that we are incrementing by 1
    for d in range(2, b+1):

        we exit when e - b = 0 so looping from e(which is 2) to b
        e = e + 1 means that we are incrementing by 1
        for e in range(2, b+1):
            g = d * e - b
            if g == 0:
                f = 0

    if f == 0:
        h += 1
-----------------------------------------------------------
b = 106500
c = 123500
for b in range(b, c+1, 17):
    f = 1
    for d in range(2, b+1):
        for e in range(2, b+1):
            if d * e == b:
                f = 0
    if f == 0:
        h += 1
-----------------------------------------------------------
so the two inner loops are checking if b is composite
we can see that for any b in the range, we are trying to find
two numbers d and e that combine to make b
so as long as b is not prime we should be able to find those values
that simplifies it enough down to our later code
-----------------------------------------------------------
our answer should be 917
    """
    h = 0
    for b in range(106500, 123500+1, 17):
        if not isPrime(b):
            h += 1
    return h
if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
