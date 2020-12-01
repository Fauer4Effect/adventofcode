"""
Author: Kyle Fauerbach
Python solution to advent of code day 3
"""
def part1():
    """
    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

    consider for the above sample, we can see that 10 is in ring 2
    corners of ring 2 are 25, 21, 17, 13
    we will number corners in the following manner
    1---0
    |   |
    2---3
    then we find the larger corner of the side that the number lies on
    from that we can calculate the offset of the number along that side
    then we calculate the displacement of that number from the center of the side
    the distance of the number from the center is the ring + that displacement

    distance for 10 should be 3
    distance for 15 should be 2
    distance for 21 should be 4

    final answer should be 371
    """
    my_input = 368078
    ring = 0
    while (2*ring+1)**2 < my_input:
        ring += 1
    width = 2*ring+1
    corners = [width**2 - ((width-1)*a) for a in range(4)][::-1]
    anchor = 0
    for corner in corners:
        if my_input <= corner:
            anchor = corner
            break
    diff = ring - (anchor - my_input)
    return ring + abs(diff)

def part2():
    """
    we can see that it looks like an integer sequence so we try searching
    1,1,2,4,5,10,11,23 on the online encyclopedia of integer sequences
    https://oeis.org/A141481

    Alternatively we can just build an algorithm that fills in the matrix

    answer should be 369601
    """
    my_input = 368078
    coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    x = y = dx = 0
    dy = -1
    grid = {}

    while True:
        total = 0
        for offset in coords:
            ox, oy = offset
            if (x+ox, y+oy) in grid:
                total += grid[(x+ox, y+oy)]
        if total > int(my_input):
            return total
        if (x, y) == (0, 0):
            grid[(0, 0)] = 1
        else:
            grid[(x, y)] = total
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
