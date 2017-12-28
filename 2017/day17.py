"""
Author: Kyle Fauerbach
Python solution to advent of code day 17
"""
def part1():
    """
    answer should be 1173
    """
    steps = 304
    spinlock = [0]
    cur_pos = 0
    for i in xrange(1, 2018):
        cur_pos = (cur_pos + steps) % len(spinlock)
        cur_pos += 1
        spinlock = spinlock[:cur_pos] + [i] + spinlock[cur_pos:]
    wanted = spinlock.index(2017)
    return spinlock[wanted+1]

def part2():
    """
    this time we need to go through 50 million iterations
    obviously this will be too big for our memory, so we should figure out some sort of generator
    
    answer should be 1930815
    """
    def spinlock():
        steps = 304
        cur_pos = 0
        length = 1
        while True:
            cur_pos = (cur_pos + steps) % length
            cur_pos += 1
            if cur_pos == 1:
                after_zero = length
            yield after_zero
            length += 1

    spin = spinlock()
    for _ in range(49999999):
        spin.next()
    return spin.next()

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
