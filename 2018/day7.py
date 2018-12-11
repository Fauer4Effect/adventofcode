"""
Author: Kyle Fauerbach
Python solution to advent of code day 7
"""

from collections import defaultdict

def part1():
    with open("7_1_in.txt", "r") as my_input:
        insts = my_input.readlines()

    available = set()
    pre_reqs = defaultdict(set)
    for inst in insts:
        inst = inst.strip().split()
        pre = inst[1]
        cur = inst[7]
        pre_reqs[cur].add(pre)
        available.add(pre)
        available.add(cur)

    cmd_list = [x for x in available]
    cmd_list.sort()

    output = ''
    while cmd_list:
        for cmd in cmd_list:
            if not pre_reqs[cmd]:
                cmd_list.remove(cmd)
                output += cmd
                for key in pre_reqs.keys():
                    try:
                        pre_reqs[key].remove(cmd)
                    except KeyError:
                        pass
                break
    return output

def time_for_cmd(cmd):
    return 61 + (ord(cmd) - ord('A'))

def part2():
    with open("7_1_in.txt", "r") as my_input:
        insts = my_input.readlines()

    available = set()
    pre_reqs = defaultdict(set)
    for inst in insts:
        inst = inst.strip().split()
        pre = inst[1]
        cur = inst[7]
        pre_reqs[cur].add(pre)
        available.add(pre)
        available.add(cur)
    cmd_list = [x for x in available]
    cmd_list.sort()

    num_workers = 5

    output = ''
    working = [0 for _ in range(num_workers)]
    clock = 0
    busy = False
    while cmd_list or busy:
        # for every worker check if they are done
        for i in range(num_workers):
            # working on something
            if working[i] != 0:
                cmd, start = working[i]
                # have finshed working on it
                if (clock-start) >= time_for_cmd(cmd):
                    output += cmd
                    for key in pre_reqs.keys():
                        try:
                            pre_reqs[key].remove(cmd)
                        except KeyError:
                            pass
                    working[i] = 0
                    busy = False
        # for every worker assign new work if possible
        for i in range(num_workers):
            #  little guard because we don't want to be working and pick another
            if working[i] == 0:
                for cmd in cmd_list:
                    if not pre_reqs[cmd]:
                        cmd_list.remove(cmd)
                        working[i] = (cmd, clock)
                        break

        for worker in working:
            if worker != 0:
                busy = True
        # handle the off by one at the end
        if busy:
            clock += 1

    return clock

if __name__ == "__main__":
    print(part1())
    print(part2())
