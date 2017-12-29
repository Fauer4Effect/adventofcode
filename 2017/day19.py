"""
Author: Kyle Fauerbach
Python solution to advent of code day 19
"""
def solve():
    """
    part 1 answer should be BPDKCZWHGT
    part 2 answer should be 17728
    """
    with open("19_1_in.txt", "r") as my_input:
        inside = map(lambda s: ['*']+s+['*'], map(list, my_input.read().split('\n')))
    padding = ['*' for _ in xrange(129)]
    graph = []
    graph.append(padding)
    graph += inside
    graph.append(padding)
    row = 1
    col = graph[row].index('|')
    direction = 'd'
    seen = set()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    steps = 0
    while True:
        steps += 1
        cur_pos = graph[row][col]
        if cur_pos in letters:
            seen.add(cur_pos)
        if cur_pos not in '+|-' + letters:
            break
        if cur_pos == '+':
            if direction == 'd':
                if graph[row+1][col] == '+' or graph[row+1][col] == '|' or graph[row+1][col] in letters:
                    row += 1
                elif graph[row][col+1] == '+' or graph[row][col+1] == '-' or graph[row][col+1] in letters:
                    col += 1
                    direction = 'r'
                elif graph[row][col-1] == '+' or graph[row][col-1] == '-' or graph[row][col-1] in letters:
                    col -= 1
                    direction = 'l'
            elif direction == 'u':
                if graph[row-1][col] == '+' or graph[row-1][col] == '|' or graph[row-1][col] in letters:
                    row -= 1
                elif graph[row][col+1] == '+' or graph[row][col+1] == '-' or graph[row][col+1] in letters:
                    col += 1
                    direction = 'r'
                elif graph[row][col-1] == '+' or graph[row][col-1] == '-' or graph[row][col-1] in letters:
                    col -= 1
                    direction = 'l'
            elif direction == 'r':
                if graph[row][col+1] == '+' or graph[row][col+1] == '-' or graph[row][col+1] in letters:
                    col += 1
                elif graph[row+1][col] == '+' or graph[row+1][col] == '|' or graph[row+1][col] in letters:
                    row += 1
                    direction = 'd'
                elif graph[row-1][col] == '+' or graph[row-1][col] == '|' or graph[row-1][col] in letters:
                    row -= 1
                    direction = 'u'
            elif direction == 'l':
                if graph[row][col-1] == '+' or graph[row][col-1] == '-' or graph[row][col-1] in letters:
                    col -= 1
                elif graph[row+1][col] == '+' or graph[row+1][col] == '|' or graph[row+1][col] in letters:
                    row += 1
                    direction = 'd'
                elif graph[row-1][col] == '+' or graph[row-1][col] == '|' or graph[row-1][col] in letters:
                    row -= 1
                    direction = 'u'                
        else:
            if direction == 'd':
                row += 1
            if direction == 'u':
                row -= 1
            if direction == 'r':
                col += 1
            if direction == 'l':
                col -= 1
    ans = ''.join([char for char in seen])
    return ans, steps-1

if __name__ == "__main__":
    part1, part2 = solve()
    print "part1", part1
    print "part2", part2
