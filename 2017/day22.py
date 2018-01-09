"""
Author: Kyle Fauerbach
Python solution to advent of code day 22
"""
def part1():
    """
    answer should be
    """
    with open("22_1_in.txt", "r") as my_input:
        graph = map(list, map(str.strip, my_input.readlines()))
    graph = [['.','.','#'], ['#','.','.'], ['.','.','.']]
    num_rows = 0 - int((len(graph)-1)/2)
    num_cols = 0 - int((len(graph[0])-1)/2)
    grid = {}
    for i in xrange(num_rows, abs(num_rows)+1):
        for j in xrange(num_cols, abs(num_cols)+1):
            if graph[i+num_rows-1][j+num_cols-1] == '#':
                grid[(i, j)] = 1
            elif graph[i+num_rows-1][j+num_cols-1] == '.':
                grid[(i, j)] = 0
    cur_x = 0
    cur_y = 0
    facing = 'n'
    caused_infection = 0
    for _ in xrange(7):
        if (cur_x, cur_y) in grid.keys():
            infected = grid[(cur_x, cur_y)]
        else:
            grid[(cur_x, cur_y)] = 0
            infected = 0
        if infected:
            grid[(cur_x, cur_y)] = 0
            if facing == 'n':
                facing = 'e'
            elif facing == 'e':
                facing = 's'
            elif facing == 's':
                facing = 'w'
            else:
                facing = 'n'
        else:
            grid[(cur_x, cur_y)] = 1
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

if __name__ == "__main__":
    print "part1", part1()
