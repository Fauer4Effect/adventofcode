"""
Author: Kyle Fauerbach
Python solution to advent of code day 15
"""

import itertools

def part1():
    """
    we will use itertools.izip because if we just used zip then
    we would end up making the actual list of tuples which at 40000000
    would be too big and get memory error
    answer should be 600
    """
    def genA(num):
        """
        generator for a
        """
        count = 0
        valA = 699
        while count < num:
            valA = (valA * 16807) % 2147483647
            count += 1
            yield valA
    def genB(num):
        """
        generator for b
        """
        count = 0
        valB = 124
        while count  < num:
            valB = (valB * 48271) % 2147483647  
            count += 1
            yield valB
    gen_a = genA(40000000)
    gen_b = genB(40000000)
    matches = 0
    for (a, b) in itertools.izip(gen_a, gen_b):
        if bin(a)[-16:] == bin(b)[-16:]:
            matches += 1
    return matches

def part2():
    """
    answer should be 313
    """
    def genA(num):
        """
        generator for a
        """
        count = 0
        valA = 699
        while count < num:
            valA = (valA * 16807) % 2147483647
            while valA % 4 != 0:
                valA = (valA * 16807) % 2147483647
            count += 1
            yield valA
    def genB(num):
        """
        generator for b
        """
        count = 0
        valB = 124
        while count  < num:
            valB = (valB * 48271) % 2147483647
            while valB % 8 != 0:
                valB = (valB * 48271) % 2147483647    
            count += 1
            yield valB
    gen_a = genA(5000000)
    gen_b = genB(5000000)
    matches = 0
    for (a, b) in itertools.izip(gen_a, gen_b):
        if bin(a)[-16:] == bin(b)[-16:]:
            matches += 1
    return matches

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
