"""
Author: Kyle Fauerbach
Python solution to advent of code day 18
"""

def check_open(acres, neighbors):
    open = 0
    for neighbor in neighbors:
        if acres[neighbor] == '|':
            open += 1
    return True if open >= 3 else False

def check_tree(acres, neighbors):
    lumber = 0
    for neighbor in neighbors:
        if acres[neighbor] == '#':
            lumber += 1
    return True if lumber >= 3 else False

def check_lumber(acres, neighbors):
    lumber = 0
    tree = 0
    for neighbor in neighbors:
        if acres[neighbor] == '#':
            lumber += 1
        if acres[neighbor] == '|':
            tree += 1
    return False if lumber > 0 and tree > 0 else True

def transform(neighbors, acres, type):
    if type == '.':
        return check_open(acres, neighbors)
    if type == '|':
        return check_tree(acres, neighbors)
    if type == '#':
        return check_lumber(acres, neighbors)

def neighbors_full(cur_pos, acres, type):
    x, y = cur_pos
    neighbors = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    return transform(neighbors, acres, type)

def neighbors_left(cur_pos, acres, type):
    x, y = cur_pos
    neighbors = [(x,y-1),(x+1,y-1),(x+1,y),(x,y+1),(x+1,y+1)]
    return transform(neighbors, acres, type)

def neighbors_right(cur_pos, acres, type):
    x, y = cur_pos
    neighbors = [(x-1,y-1),(x,y-1),(x-1,y),(x-1,y+1),(x,y+1),]
    return transform(neighbors, acres, type)

def neighbors_top(cur_pos, acres, type):
    x, y = cur_pos
    neighbors = [(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    return transform(neighbors, acres, type)

def neighbors_bottom(cur_pos, acres, type):
    x, y = cur_pos
    neighbors = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y)]
    return transform(neighbors, acres, type)

def neighbors_top_left(cur_pos, acres, type):
    x, y = cur_pos
    neighbors = [(x+1,y),(x,y+1),(x+1,y+1)]
    return transform(neighbors, acres, type)

def neighbors_top_right(cur_pos, acres, type):
    x, y = cur_pos
    neighbors = [(x-1,y-1),(x,y-1),(x-1,y)]
    return transform(neighbors, acres, type)

def neighbors_bottom_left(cur_pos, acres, type):
    x, y = cur_pos
    neighbors = [(x,y-1),(x+1,y-1),(x+1,y)]
    return transform(neighbors, acres, type)

def neighbors_bottom_right(cur_pos, acres, type):
    x, y = cur_pos
    neighbors = [(x-1,y),(x,y-1),(x-1,y-1)]
    return transform(neighbors, acres, type)

def run_simulation(map, time, max_x, max_y):
    acres = map
    for _ in range(time):
        new_acres = {}
        # inside parts so we don't have to do the edges
        for y in range(1, max_y-1):
            for x in range(1, max_x-1):
                if acres[(x, y)] == '|':
                    if neighbors_full((x, y), acres, '|'):
                        new_acres[(x, y)] = '#'
                if acres[(x, y)] == '#':
                    if neighbors_full((x, y), acres, '#'):
                        new_acres[(x, y)] = '.'
                if acres[(x, y)] == '.':
                    if neighbors_full((x, y), acres, '.'):
                        new_acres[(x, y)] = '|'
        # left edge
        for y in range(1, max_y-1):
            if acres[(0, y)] == '|':
                if neighbors_left((0, y), acres, '|'):
                    new_acres[(0, y)] = '#'
            if acres[(0, y)] == '#':
                if neighbors_left((0, y), acres, '#'):
                    new_acres[(0, y)] = '.'
            if acres[(0, y)] == '.':
                if neighbors_left((0, y), acres, '.'):
                    new_acres[(0, y)] = '|'
        # right edge
        for y in range(1, max_y-1):
            if acres[(max_x-1, y)] == '|':
                if neighbors_right((max_x-1, y), acres, '|'):
                    new_acres[(max_x-1, y)] = '#'
            if acres[(max_x-1, y)] == '#':
                if neighbors_right((max_x-1, y), acres, '#'):
                    new_acres[(max_x-1, y)] = '.'
            if acres[(max_x-1, y)] == '.':
                if neighbors_right((max_x-1, y), acres, '.'):
                    new_acres[(max_x-1, y)] = '|'
        # top edge
        for x in range(1, max_x-1):
            if acres[(x, 0)] == '|':
                if neighbors_top((x, 0), acres, '|'):
                    new_acres[(x, 0)] = '#'
            if acres[(x, 0)] == '#':
                if neighbors_top((x, 0), acres, '#'):
                    new_acres[(x, 0)] = '.'
            if acres[(x, 0)] == '.':
                if neighbors_top((x, 0), acres, '.'):
                    new_acres[(x, 0)] = '|'
        # bottom edge
        for x in range(1, max_x-1):
            if acres[(x, max_y-1)] == '|':
                if neighbors_bottom((x, max_y-1), acres, '|'):
                    new_acres[(x, max_y-1)] = '#'
            if acres[(x, max_y-1)] == '#':
                if neighbors_bottom((x, max_y-1), acres, '#'):
                    new_acres[(x, max_y-1)] = '.'
            if acres[(x, max_y-1)] == '.':
                if neighbors_bottom((x, max_y-1), acres, '.'):
                    new_acres[(x, max_y-1)] = '|'
        # corners
        if acres[(0, 0)] == '|':
            if neighbors_top_left((0, 0), acres, '|'):
                new_acres[(0, 0)] = '#'
        if acres[(0, 0)] == '#':
            if neighbors_top_left((0, 0), acres, '#'):
                new_acres[(0, 0)] = '.'
        if acres[(0, 0)] == '.':
            if neighbors_top_left((0, 0), acres, '.'):
                new_acres[(0, 0)] = '|'

        if acres[(0, max_y-1)] == '|':
            if neighbors_bottom_left((0, max_y-1), acres, '|'):
                new_acres[(0, max_y-1)] = '#'
        if acres[(0, max_y-1)] == '#':
            if neighbors_bottom_left((0, max_y-1), acres, '#'):
                new_acres[(0, max_y-1)] = '.'
        if acres[(0, max_y-1)] == '.':
            if neighbors_bottom_left((0, max_y-1), acres, '.'):
                new_acres[(0, max_y-1)] = '|'

        if acres[(max_x-1, 0)] == '|':
            if neighbors_top_right((max_x-1, 0), acres, '|'):
                new_acres[(max_x-1, 0)] = '#'
        if acres[(max_x-1, 0)] == '#':
            if neighbors_top_right((max_x-1, 0), acres, '#'):
                new_acres[(max_x-1, 0)] = '.'
        if acres[(max_x-1, 0)] == '.':
            if neighbors_top_right((max_x-1, 0), acres, '.'):
                new_acres[(max_x-1, 0)] = '|'

        if acres[(max_x-1, max_y-1)] == '|':
            if neighbors_bottom_right((max_x-1, max_y-1), acres, '|'):
                new_acres[(max_x-1, max_y-1)] = '#'
        if acres[(max_x-1, max_y-1)] == '#':
            if neighbors_bottom_right((max_x-1, max_y-1), acres, '#'):
                new_acres[(max_x-1, max_y-1)] = '.'
        if acres[(max_x-1, max_y-1)] == '.':
            if neighbors_bottom_right((max_x-1, max_y-1), acres, '.'):
                new_acres[(max_x-1, max_y-1)] = '|'

        for point, type in new_acres.items():
            acres[point] = type

    wooded = 0
    lumber = 0
    for _, value in acres.items():
        if value == '|':
            wooded += 1
        if value == '#':
            lumber += 1

    return wooded * lumber


def part1():
    with open("18_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()
    acres = {}
    for y in range(len(my_input)):
        for x in range(len(my_input[y])):
            acres[(x, y)] = my_input[y][x]
    max_x = len(my_input[0])
    max_y = len(my_input)

    return run_simulation(acres, 10, max_x, max_y)


def part2():
    with open("18_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()
    acres = {}
    for y in range(len(my_input)):
        for x in range(len(my_input[y])):
            acres[(x, y)] = my_input[y][x]
    max_x = len(my_input[0])
    max_y = len(my_input)

    # we can find a cycle in the scores, in our case, the cycle is 28.
    # 1000000000 % 28 = 20
    # so what if we try 2820 times?

    print(run_simulation(acres, 2820, max_x, max_y))

if __name__ == "__main__":
    print(part1())
    print(part2())
