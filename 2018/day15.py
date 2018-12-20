"""
Author: Kyle Fauerbach
Python solution to advent of code day 15
"""

from operator import attrgetter
from collections import deque

class Fighter(object):
    def __init__(self, location, type, pp=3, hp=200):
        self.x = location[0]
        self.y = location[1]
        self.type = type
        self.pp = pp
        self.hp = hp
        self.is_alive = True

    def __repr__(self):
        return self.type

    def find_enemies(self, grid):
        enemies = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != '.' and grid[y][x] != '#':
                    person = grid[y][x]
                    if person.type != self.type and person.is_alive:
                        enemies.append(person)
        return enemies

    def check_range(self, enemies):
        range = []
        for enemy in enemies:
            # if (abs(self.x - enemy.x) <= 1) and (abs(self.y - enemy.y) <= 1):
            if (abs(self.x - enemy.x) == 1) and (abs(self.y - enemy.y) == 0):
                range.append(enemy)
            if (abs(self.x - enemy.x) == 0) and (abs(self.y - enemy.y) == 1):
                range.append(enemy)
        return range

    def find_open_squares(self, location, grid):
        """
        Find open squares that are adjacent to an enemy location
        """
        height = len(grid)
        width = len(grid[0])
        x, y = location
        search = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        search = [(x2, y2) for x2, y2 in search if 0<=x2<width and 0<=y2<height and grid[y2][x2] == '.']
        return search

    def got_attacked(self, attacker_pp):
        self.hp -= attacker_pp
        if self.hp < 1:
            self.is_alive = False

    def attack(self, in_range):
        # Sort by hit points then sort in reading order to break ties
        in_range = sorted(in_range, key=attrgetter('hp', 'y', 'x'))
        chosen = in_range[0]
        chosen.got_attacked(self.pp)

    def bfs(self, current, goal, grid):
        height = len(grid)
        width = len(grid[0])
        queue = deque([[current]])
        seen = set([current])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if (x, y) == goal:
                return len(path)
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0<=x2<width and 0<=y2<height and grid[y2][x2] == '.' and (x2, y2) not in seen:
                    queue.append(path+[(x2,y2)])
                    seen.add((x2,y2))
        return 1000000


    def move(self, open, grid):
        height = len(grid)
        width = len(grid[0])
        # Find which squares are reachable
        distances = {}
        for point in open:
            distances[point] = self.bfs((self.x, self.y), point, grid)
        # sort those reachable ones by distance and then reading order
        chosen = sorted(distances.items(), key=lambda kv: (kv[1], kv[0][1], kv[0][0]))[0][0]
        if distances[chosen] == 1000000:
            return

        # for the chosen square pick which adjacent square to go to by distance
        # from that new square to the chosen and reading order
        x, y = self.x, self.y
        search = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        search = [(x2, y2) for x2, y2 in search if 0<=x2<width and 0<=y2<height and grid[y2][x2] == '.']
        if not search:
            return
        distances = {}
        for point in search:
            distances[point] = self.bfs(point, chosen, grid)
        goto = sorted(distances.items(), key=lambda kv: (kv[1], kv[0][1], kv[0][0]))[0][0]

        # move to that square
        grid[self.y][self.x] = '.'
        self.x, self.y = goto
        grid[self.y][self.x] = self
        return

    def do_turn(self, grid):
        """
        Return true if combat is over, i.e. all enemies killed. False otherwise.
        """
        enemies = self.find_enemies(grid)
        if not enemies:
            return True

        open = []
        for enemy in enemies:
            open += self.find_open_squares((enemy.x, enemy.y), grid)
        in_range = self.check_range(enemies)
        if not in_range and not open:
            return False

        if not in_range:
            self.move(open, grid)
            # update what enemies are in range
            in_range = self.check_range(enemies)

        if in_range:
            self.attack(in_range)

        # remove dead people from grid
        for enemy in enemies:
            if not enemy.is_alive:
                grid[enemy.y][enemy.x] = '.'
        return False


def play_game(part2, elf_attack_power=3):
    with open("15_1_in.txt", "r") as my_input:
        grid = [list(x.replace('\n', '')) for x in my_input.readlines()]
    fighters = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'E':
                new_fighter = Fighter((x, y), 'E', elf_attack_power)
                grid[y][x] = new_fighter
                fighters.append(new_fighter)
            elif grid[y][x] == 'G':
                new_fighter = Fighter((x, y), 'G')
                grid[y][x] = new_fighter
                fighters.append(new_fighter)
    rounds = 0
    elf_died = False
    while 1:
        done = False
        # fighters take turns in reading order
        fighters = sorted(fighters, key=attrgetter('y', 'x'))
        for fighter in fighters:
            if fighter.is_alive:
                done = fighter.do_turn(grid)
            if done:
                break
        for fighter in fighters:
            if fighter.type == 'E' and not fighter.is_alive:
                elf_died = True
                break

        fighters = [fighter for fighter in fighters if fighter.is_alive]
        if done:
            break
        if part2 and elf_died:
            break
        rounds += 1

    score = 0
    for fighter in fighters:
        score += fighter.hp

    return elf_died, fighters[0].type, rounds * score

def part1():
    elf_died, winner_type, score = play_game(False)

    return score

def part2():

    elf_attack_power = 4
    while 1:
        elf_died, winner_type, score = play_game(True, elf_attack_power)
        if not elf_died:
            break
        elf_attack_power += 1

    return elf_attack_power, score

if __name__ == "__main__":
    print(part1())
    print(part2())
