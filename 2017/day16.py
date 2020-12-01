"""
Author: Kyle Fauerbach
Python solution to advent of code day 16
"""
def part1(programs):
    """
    answer should be giadhmkpcnbfjelo
    """
    with open("16_1_in.txt", "r") as my_input:
        commands = map(str.strip, my_input.read().split(','))
    for command in commands:
        if 's' in command:
            index = int(command[1:])
            programs = programs[-index:] + programs[:-index]
        elif 'x' in command:
            command = command.split('/')
            first = int(command[0][1:])
            second = int(command[1])
            if second < first:
                first, second = second, first
            programs = programs[:first] + programs[second] + programs[first+1:second] + programs[first] + programs[second+1:]
        elif 'p' in command:
            command = command.split('/')
            first = command[0][1]
            second = command[1]
            first_ind = programs.index(first)
            second_ind = programs.index(second)
            if second_ind < first_ind:
                first_ind, second_ind = second_ind, first_ind
            programs = programs[:first_ind] + programs[second_ind] + programs[first_ind+1:second_ind] + programs[first_ind] + programs[second_ind+1:]
    return programs

def part2():
    """
    we will do a little bit of memoization for dances
    we've already seen
    answer should be njfgilbkcoemhpad
    """
    start = "abcdefghijklmnop"
    dances = {}
    for _ in xrange(1000000):
        if start in dances.keys():
            start = dances[start]
        else:
            fin = part1(start)
            dances[start] = fin
            start = fin
    return start

if __name__ == "__main__":
    print "part1", part1("abcdefghijklmnop")
    print "part2", part2()
