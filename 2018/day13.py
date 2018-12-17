"""
Author: Kyle Fauerbach
Python solution to advent of code day 13
"""

from collections import deque
from operator import attrgetter

class Cart(object):
    """
    an object
    Attributes:
        none
    Methods:
        none
    """
    def __init__(self, pos_x, pos_y, orientation):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.orientation = orientation
        self.intersection = self.do_intersection()

    def do_intersection(self):
        """
        Generator to move through the intersection
        """
        count = 0
        while 1:
            if count % 3 == 0:
                # left
                if self.orientation == 'N':
                    self.orientation = 'W'
                elif self.orientation == 'E':
                    self.orientation = 'N'
                elif self.orientation == 'S':
                    self.orientation = 'E'
                elif self.orientation == 'W':
                    self.orientation = 'S'
            elif count % 3 == 1:
                # straight
                yield self.orientation
            elif count % 3 == 2:
                # right
                if self.orientation == 'N':
                    self.orientation = 'E'
                elif self.orientation == 'E':
                    self.orientation = 'S'
                elif self.orientation == 'S':
                    self.orientation = 'W'
                elif self.orientation == 'W':
                    self.orientation = 'N'
            count += 1

    def move(self, cur_piece):
        # check if you need to update the orientation
        if cur_piece == '+':
            self.orientation = next(self.intersection)
        elif cur_piece == '\\':
            if self.orientation == 'N':
                self.orientation = 'W'
            elif self.orientation == 'E':
                self.orientation = 'S'
            elif self.orientation == 'S':
                self.orientation = 'E'
            elif self.orientation == 'W':
                self.orientation = 'N'
        elif cur_piece == '/':
            if self.orientation == 'N':
                self.orientation = 'E'
            elif self.orientation == 'E':
                self.orientation = 'N'
            elif self.orientation == 'S':
                self.orientation = 'W'
            elif self.orientation == 'W':
                self.orientation = 'S'

        # do the move
        if self.orientation == 'N':
            self.pos_y -= 1
        elif self.orientation == 'S':
            self.pos_y += 1
        elif self.orientation == 'W':
            self.pos_x -= 1
        elif self.orientation == 'E':
            self.pos_x += 1

def check_collisions(carts):
    positions = set()
    for cart in carts:
        pos = (cart.pos_x, cart.pos_y)
        if pos in positions:
            return pos
        positions.add(pos)
    return None

def part1():
    """
    we could try to keep a 2d array of the map and then have cart objects that we will store
    for position and shit
    As far as moving we could keep a queue of the carts sorted by their position
    then we could do tick for each in order to do the move and then check collision every time?
    """

    with open("13_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()
    grid = [list(line.strip()) for line in my_input]

    carts = deque()
    num_carts = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                carts.append(Cart(x, y, 'N'))
                num_carts += 1
                grid[y][x] = '|'
            elif grid[y][x] == '<':
                carts.append(Cart(x, y, 'W'))
                num_carts += 1
                grid[y][x] = '-'
            elif grid[y][x] == '>':
                carts.append(Cart(x, y, 'E'))
                num_carts += 1
                grid[y][x] = '-'
            elif grid[y][x] == 'v':
                carts.append(Cart(x, y, 'S'))
                num_carts += 1
                grid[y][x] = '|'

    collided = check_collisions(carts)
    # while not collided:
    for _ in range(20):
        carts = deque(sorted(carts, key=attrgetter('pos_y', 'pos_x')))
        for _ in range(num_carts):
            cart = carts.popleft()
            cart.move(grid[cart.pos_y][cart.pos_x])
            carts.append(cart)
        collided = check_collisions(carts)
        for cart in carts:
            print(cart.pos_y, cart.pos_x)
        print("-"*20)


    return collided

def part2():

    return None

if __name__ == "__main__":
    print(part1())
    print(part2())
