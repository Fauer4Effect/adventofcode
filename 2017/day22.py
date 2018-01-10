"""
Author: Kyle Fauerbach
Python solution to advent of code day 22
"""

from collections import defaultdict

def gen_graph():
    """
    returns a dictionary keys are tuple of x,y coord and value is 0 in clean
        1 if infected
    """
    with open("22_1_in.txt", "r") as my_input:
        graph = map(list, map(str.strip, my_input.readlines()))
    range_y = 0 - int((len(graph)-1)/2)
    range_x = 0 - int((len(graph[0])-1)/2)
    # the defaultdict from collections is much faster than the normal python dict
    grid = defaultdict()
    for i in xrange(abs(range_y), range_y-1, -1):
        new_i = abs(range_y) - i
        for j in xrange(range_x, abs(range_x)+1):
            new_j = j + abs(range_x)
            if graph[new_i][new_j] == '#':
                grid[(j, i)] = 'i'
            else:
                grid[(j, i)] = 'c'
    return grid

def part1():
    """
    answer should be 5570
    """
    grid = gen_graph()
    cur_x = 0
    cur_y = 0
    facing = 'n'
    caused_infection = 0
    for _ in xrange(10000):
        # python is witchcraft
        # we can do (cur_x, cur_y) in grid and will get a fast response
        # because it's a hashed object in a lookup table
        # compare this to our original approach
        # if (cur_x, cur_y) in grid.keys()
        # according to python documentation, grid.keys() specifies to create a list
        # this means that it's doing a O(n) lookup on that instead of O(1)
        if (cur_x, cur_y) in grid:
            infected = grid[(cur_x, cur_y)]
        else:
            grid[(cur_x, cur_y)] = 'c'
            infected = 'c'
        if infected == 'i':
            grid[(cur_x, cur_y)] = 'c'
            if facing == 'n':
                facing = 'e'
            elif facing == 'e':
                facing = 's'
            elif facing == 's':
                facing = 'w'
            else:
                facing = 'n'
        else:
            grid[(cur_x, cur_y)] = 'i'
            caused_infection += 1
            if facing == 'n':
                facing = 'w'
            elif facing == 'w':
                facing = 's'
            elif facing == 's':
                facing = 'e'
            else:
                facing = 'n'
        if facing == 'n':
            cur_y += 1
        elif facing == 'e':
            cur_x += 1
        elif facing == 's':
            cur_y -= 1
        else:
            cur_x -= 1
    return caused_infection

def part2():
    """
    answer should be 2512022
    """
    grid = gen_graph()
    cur_x = 0
    cur_y = 0
    facing = 'n'
    caused_infection = 0
    for _ in xrange(10000000):
        if (cur_x, cur_y) in grid:
            infected = grid[(cur_x, cur_y)]
        else:
            grid[(cur_x, cur_y)] = 'c'
            infected = 'c'
        if infected == 'i':
            grid[(cur_x, cur_y)] = 'f'
            if facing == 'n':
                facing = 'e'
            elif facing == 'e':
                facing = 's'
            elif facing == 's':
                facing = 'w'
            else:
                facing = 'n'
        elif infected == 'w':
            grid[(cur_x, cur_y)] = 'i'
            caused_infection += 1
        elif infected == 'f':
            grid[(cur_x, cur_y)] = 'c'
            if facing == 'n':
                facing = 's'
            elif facing == 's':
                facing = 'n'
            elif facing == 'e':
                facing = 'w'
            else:
                facing = 'e'
        else:
            grid[(cur_x, cur_y)] = 'w'
            if facing == 'n':
                facing = 'w'
            elif facing == 'w':
                facing = 's'
            elif facing == 's':
                facing = 'e'
            else:
                facing = 'n'
        if facing == 'n':
            cur_y += 1
        elif facing == 'e':
            cur_x += 1
        elif facing == 's':
            cur_y -= 1
        else:
            cur_x -= 1
    return caused_infection

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
