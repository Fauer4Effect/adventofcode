"""
Author: Kyle Fauerbach
Python solution to advent of code day 9
"""

from collections import deque

def play_game(num_players, last_marble):
    scores = [0 for _ in range(num_players)]
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % num_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores)

def part1():
    num_players = 431
    last_marble = 70950
    return play_game(num_players, last_marble)



def part2():
    num_players = 431
    last_marble = 7095000
    return play_game(num_players, last_marble)

if __name__ == "__main__":
    print(part1())
    print(part2())
