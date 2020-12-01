"""
Author: Kyle Fauerbach
Python solution to advent of code day 4
"""

import operator
from collections import defaultdict

def part1():
    with open("4_1_in.txt", "r") as my_input:
        my_input = my_input.read().split('\n')[:-1]

    # sorting it solves a lot of our problems
    # we now know that we will have in order
    # Guard start duty, falls asleep, wake ups, fall asleep, wake up...
    # so we don't have to keep track of the dates ourselves
    my_input.sort()

    # guard_id + 60 minutes
    # worst case would be no one falls asleep so all you have are times when they get on
    schedule = [[0 for i in range(61)] for j in range(len(my_input))]
    # dictionary of how much they slept
    total_sleep = defaultdict(int)

    row = -1
    time_asleep = 0
    for entry in my_input:
        entry = entry.split(' ')
        time = entry[1]
        minutes = int(time.split(':')[1][:-1])
        # new guard on duty
        # put new row for new day add to total sleep if not yet seen
        if entry[2] == 'Guard':
            row += 1
            schedule[row][0] = entry[3]
        # mark when they fall asleep
        elif entry[2] == 'falls':
            schedule[row][minutes + 1] = 'X'
            time_asleep = 0
        # when you have reached the matching wake up, go back and mark when asleep
        elif entry[2] == 'wakes':
            for j in range(minutes, 0, -1):
                if schedule[row][j] == 'X':
                    cur_guard = schedule[row][0]
                    total_sleep[cur_guard] += time_asleep
                    break
                schedule[row][j] = 'X'
                time_asleep += 1

    most_sleep = max(total_sleep.items(), key=operator.itemgetter(1))[0]

    # map of minute to when they are asleep for that guard
    sleepy_minutes = defaultdict(int)
    for i in range(row+1):
        if schedule[i][0] != most_sleep:
            continue
        for j in range(1, 61):
            if schedule[i][j] == 'X':
                sleepy_minutes[j-1] += 1
    most_minute = max(sleepy_minutes.items(), key=operator.itemgetter(1))[0]

    return int(most_sleep[1:]) * most_minute

def part2():
    with open("4_1_in.txt", "r") as my_input:
        my_input = my_input.read().split('\n')[:-1]

    my_input.sort()

    guard_asleep = defaultdict(lambda: defaultdict(int))
    schedule = [0 for i in range(61)]

    for entry in my_input:
        entry = entry.split(' ')
        time = entry[1]
        minutes = int(time.split(':')[1][:-1])
        # new guard on duty
        if entry[2] == 'Guard':
            schedule = [0 for i in range(61)]
            schedule[0] = entry[3]
        # mark when they fall asleep
        elif entry[2] == 'falls':
            schedule[minutes + 1] = 'X'
            guard_asleep[schedule[0]][minutes] += 1
        # when you have reached the matching wake up, go back and mark when asleep
        elif entry[2] == 'wakes':
            for j in range(minutes, 0, -1):
                if schedule[j] == 'X':
                    break
                guard_asleep[schedule[0]][j-1] += 1


    # for each guard when where they most often asleep
    most_asleep = defaultdict(int)
    for guard in guard_asleep.keys():
        most_asleep[guard] = max(guard_asleep[guard].items(), key=operator.itemgetter(1))[0]

    max_times = 0
    most_guard = ''
    most_min = 0
    for guard in most_asleep.keys():
        most_common = most_asleep[guard]
        if (guard_asleep[guard][most_common] > max_times):
            max_times = guard_asleep[guard][most_common]
            most_min = most_common
            most_guard = guard

    return int(most_guard[1:]) * most_min

if __name__ == "__main__":
    print(part1())
    print(part2())
