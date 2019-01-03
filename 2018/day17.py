"""
Author: Kyle Fauerbach
Python solution to advent of code day 17
"""

from collections import defaultdict, deque
import re

def supported(cur_pos, points):
    x, y = cur_pos
    while points[(x, y)] != '#':
        if points[(x, y+1)] != '#' and points[(x, y+1)] != '~':
            return False
        x -= 1
    x, y = cur_pos
    while points[(x, y)] != '#':
        if points[(x, y+1)] != '#' and points[(x, y+1)] != '~':
            return False
        x += 1
    return True

def flowing(cur_pos, points):
    x, y = cur_pos
    while points[(x, y)] != '#':
        if points[(x, y)] == '|':
            return True
        x -= 1
    x, y = cur_pos
    while points[(x, y)] != '#':
        if points[(x, y)] == '|':
            return True
        x += 1
    return False

def run_simulation():
    points = defaultdict(lambda: ".")

    with open("17_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()
    min_y = 100000000
    max_y = 0
    for line in my_input:
        x = re.findall(r"x=[0-9.]*", line)[0][2:]
        y = re.findall(r"y=[0-9.]*", line)[0][2:]
        if '..' in x:
            y = int(y)
            lo, hi = list(map(int, x.split('..')))
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            for x2 in range(lo, hi+1):
                points[(x2, y)] = '#'
        elif '..' in y:
            x = int(x)
            lo, hi = list(map(int, y.split('..')))
            min_y = min(min_y, lo)
            max_y = max(max_y, hi)
            for y2 in range(lo, hi+1):
                points[(x, y2)] = '#'
        else:
            x = int(x)
            y = int(y)
            points[(x, y)] = '#'
            min_y = min(min_y, y)
            max_y = max(max_y, y)
    check = deque()

    points[(500, min_y)] = '|'
    check.append((500, min_y+1))

    while check:
        modified = False
        x, y = check.pop()
        if (x, y) == (500, 2):
            print(supported((x, y), points))
        if points[(x, y)] == '#':
            continue

        if points[(x, y-1)] == '|' and points[(x, y)] == '.':
            points[(x, y)] = '|'
            modified = True
        if points[(x-1, y)] == '~' and points[(x, y)] != '~':
            points[(x, y)] = '~'
            modified = True
        if points[(x+1, y)] == '~' and points[(x, y)] != '~':
            points[(x, y)] = '~'
            modified = True
        if points[(x, y-1)] == '~' and points[(x, y)] != '~':
            points[(x, y)] = '~'
            modified = True
        if points[(x, y)] == '|' and supported((x, y), points):
            points[(x, y)] = '~'
            modified = True
        if points[(x, y)] == '.' and supported((x, y), points) and flowing((x, y), points):
            points[(x, y)] = '~'
            modified = True
        if points[(x, y)] == '|' and (points[(x, y+1)] == '#' or points[(x, y+1)] == '~'):
            if points[(x-1, y)] != '#' and points[(x-1, y)] != '|':
                points[(x-1, y)] = '|'
                modified = True
                check.append((x-2, y))
                check.append((x, y))
                if y+1 <= max_y:
                    check.append((x-1, y+1))
                check.append((x-1, y-1))
                check.append((x-1, y))
            if points[(x+1, y)] != '#' and points[(x+1, y)] != '|':
                points[(x+1, y)] = '|'
                modified = True
                check.append((x, y))
                check.append((x+2, y))
                if y+1 <= max_y:
                    check.append((x+1, y+1))
                check.append((x+1, y-1))
                check.append((x+1, y))

        if modified:
            check.append((x-1, y))
            check.append((x+1, y))
            if y+1 <= max_y:
                check.append((x, y+1))
            check.append((x, y-1))
            check.append((x, y))

    return points

def part1(points):
    water = 0
    for point, value in points.items():
        if value == '|' or value == '~':
            water += 1
    return water

def part2(points):
    water = 0
    for point, value in points.items():
        if value == '~':
            water += 1
    return water

if __name__ == "__main__":
    points = run_simulation()
    print(part1(points))
    print(part2(points))
