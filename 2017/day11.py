"""
Author: Kyle Fauerbach
Python solution to advent of code day 11
"""

class Hexagon(object):
    """
    A single hexagon at a point on a hexagonal tiling

    Attributes:
        x, y, z describe our location
        Default location is (0, 0, 0)
    Methods:
        all of the methods adjust the coordinates of the hexagon
        Based on its movement in one of the 6 possible directions
        in the hexagonal tiling
    """
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def n(self):
        self.y += 1
        self.z -= 1
    def ne(self):
        self.x += 1
        self.z -= 1
    def se(self):
        self.x += 1
        self.y -= 1
    def s(self):
        self.y -= 1
        self.z += 1
    def sw(self):
        self.x -=1
        self.z += 1
    def nw(self):
        self.x -= 1
        self.y += 1

def cube_distance(a, b):
    """
    Arguments
        a: Hexagon
        b: Hexagon
    calculates the manhattan distance between two hexagons on a hexagonal tiling
    """
    return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) / 2

def part1():
    """
    awesome reference all about hexagonal tilings
        https://www.redblobgames.com/grids/hexagons/
    we are going to use the cube approach for ordering the hexagons
    so a hexagon is represented as (x, y, z)
    with the constraint that x + y + z = 0
    so from the image on the website we can find how the coordinates
    change by direction
    Mapping
        n   --> (0, 1, -1)
        ne  --> (1, 0, -1)
        se  --> (1, -1, 0)
        s   --> (0, -1, 1)
        sw  --> (-1, 0, 1)
        nw  --> (-1, 1, 0)

    answer should be 696
    """
    with open("11_1_in.txt", "r") as my_input:
        commands = my_input.read().strip().split(',')
    origin = Hexagon()
    cur = Hexagon()
    for command in commands:
        if command == 'n':
            cur.n()
        elif command == 'ne':
            cur.ne()
        elif command == 'se':
            cur.se()
        elif command == 's':
            cur.s()
        elif command == 'sw':
            cur.sw()
        elif command == 'nw':
            cur.nw()
    return cube_distance(origin, cur)

def part2():
    """
    answer should be 1461
    """
    with open("11_1_in.txt", "r") as my_input:
        commands = my_input.read().strip().split(',')
    origin = Hexagon()
    cur = Hexagon()
    max_dist = 0
    for command in commands:
        if command == 'n':
            cur.n()
        elif command == 'ne':
            cur.ne()
        elif command == 'se':
            cur.se()
        elif command == 's':
            cur.s()
        elif command == 'sw':
            cur.sw()
        elif command == 'nw':
            cur.nw()
        distance = cube_distance(origin, cur)
        max_dist = max(max_dist, distance)
    return max_dist

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
