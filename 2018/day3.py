"""
Author: Kyle Fauerbach
Python solution to advent of code day 3
"""

def fill_in_matrix(my_input, max_height, max_width):
    cloth = [['0' for i in range(max_height)] for j in range(max_width)]

    for cut in my_input:
        cut = cut.split(" ")
        x, y = cut[2].split(',')
        y = y[:-1]
        x = int(x)
        y = int(y)
        width, height = map(int, cut[3].split('x'))

        for i in range(width):
            for j in range(height):
                cur = cloth[y + j][x + i]
                if cur == '0':
                    cloth[y+j][x+i] = 'X'
                if cur == 'X':
                    cloth[y+j][x+i] = 'Y'
    return cloth

def part1():
    with open("3_1_in.txt", "r") as my_input:
        my_input = my_input.read().split('\n')[:-1]

    max_height = 1500
    max_width = 1500

    cloth = fill_in_matrix(my_input, max_height, max_width)
    overlap = 0
    for i in range(max_height):
        for j in range(max_width):
            if cloth[i][j] == 'Y':
                overlap += 1
    return overlap

def part2():

    with open("3_1_in.txt", "r") as my_input:
        my_input = my_input.read().split('\n')[:-1]

    max_height = 1500
    max_width = 1500

    cloth = fill_in_matrix(my_input, max_height, max_width)
    for cut in my_input:
        cut = cut.split(" ")
        x, y = cut[2].split(',')
        y = y[:-1]
        x = int(x)
        y = int(y)
        width, height = map(int, cut[3].split('x'))

        good = True
        for i in range(width):
            for j in range(height):
                cur = cloth[y + j][x + i]
                if cur == 'Y':
                    good = False
                    break
        if good:
            return cut[0]

    return None


if __name__ == "__main__":
    print(part1())
    print(part2())
