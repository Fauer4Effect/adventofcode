"""
Author: Kyle Fauerbach
Python solution to advent of code day 13
run with pypy
"""
def part1():
    """
    answer should be 3184
    """
    with open("13_1_in.txt", "r") as my_input:
        firewalls = map(str.strip, my_input.readlines())
    severity = 0
    for firewall in firewalls:
        firewall = firewall.split(': ')
        depth = int(firewall[0])
        rng = int(firewall[1])
        num_positions = rng*2 - 2
        time = depth
        if time % num_positions == 0:
            severity += depth * rng
    return severity

def part2():
    """
    answer should be 3878062
    """
    with open("13_1_in.txt", "r") as my_input:
        firewalls = map(str.strip, my_input.readlines())
    delay = 0
    while True:
        caught = False
        for firewall in firewalls:
            firewall = firewall.split(': ')
            depth = int(firewall[0])
            rng = int(firewall[1])
            num_positions = rng*2 - 2
            time = depth + delay
            if time % num_positions == 0:
                caught = True
                break
        if caught:
            delay += 1
        else:
            break
    return delay

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
