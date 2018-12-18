"""
Author: Kyle Fauerbach
Python solution to advent of code day 13
"""

from operator import attrgetter

class Cart(object):
    """
    cart object
    Attributes:
        x, y: coordinates on the grid
        dx, dy: "velocity" for movement on the grid
        count: how many intersections hit
        turns: swap velocity when we turn at intersections
        curves: how to scale velocity when we need to turn
    Methods:
        move(grid): make the move based on the point on the grid. Also update velocity if needed
    """
    def __init__(self, position, displacement, count=0):
        self.x = position[0]
        self.y = position[1]
        self.dx = displacement[0]
        self.dy = displacement[1]
        self.count = count
        self.turns = [lambda d: (d[1], -d[0]), lambda d: d, lambda d: (-d[1], d[0])]
        self.curves = {'\\': 1, '/': -1}

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def move(self, grid):
        self.x += self.dx
        self.y += self.dy
        new_spot = grid[self.y][self.x]

        if new_spot == '+':
            self.dx, self.dy = self.turns[self.count % 3]((self.dx, self.dy))
            self.count += 1
        if new_spot in self.curves:
            factor = self.curves[new_spot]
            self.dx, self.dy = (self.dy * factor, self.dx * factor)


def part1():
    with open('13_1_in.txt') as my_input:
        grid = [list(l) for l in my_input.read().split('\n')]

    moves = {'^': (0, -1), '>': (1,  0), 'v': (0,  1), '<': (-1,  0)}
    cart_syms = list(moves.keys())

    carts = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            cur = grid[y][x]
            if cur in cart_syms:
                carts.append(Cart([x, y], moves[cur], 0))
                grid[y][x] = '-' if cur in ['<', '>'] else '|'

    while 1:
        carts = sorted(carts, key=attrgetter('y', 'x'))

        for i, cart in enumerate(carts):
            cart.move(grid)
            pos = (cart.x, cart.y)
            # Check if we have collided
            for j in range(len(carts)):
                # don't check self
                if j == i:
                    continue
                cart2 = carts[j]
                if (cart2.x, cart2.y) == pos:
                    return pos
    return None

def part2():
    with open('13_1_in.txt') as my_input:
        grid = [list(l) for l in my_input.read().split('\n')]

    moves = {'^': (0, -1), '>': (1,  0), 'v': (0,  1), '<': (-1,  0)}
    cart_syms = list(moves.keys())

    carts = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            cur = grid[y][x]
            if cur in cart_syms:
                carts.append(Cart([x, y], moves[cur], 0))
                grid[y][x] = '-' if cur in ['<', '>'] else '|'

    while len(carts) > 1:
        carts = sorted(carts, key=attrgetter('y', 'x'))
        collisions = []

        for i, cart in enumerate(carts):
            if cart in collisions:
                continue
            cart.move(grid)
            pos = (cart.x, cart.y)
            for j in range(len(carts)):
                if j == i:
                    continue
                cart2 = carts[j]
                if (cart2.x, cart2.y) == pos:
                    collisions.append(cart)
                    collisions.append(cart2)

        carts = [c for c in carts if c not in collisions]

    return carts[0]


if __name__ == "__main__":
    print(part1())
    print(part2())
