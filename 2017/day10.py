"""
Author: Kyle Fauerbach
Python solution to advent of code day 10
"""
def part1():
    """
    answer should be 13760
    """
    with open("10_1_in.txt", "r") as my_input:
        lengths = map(int, my_input.read().strip().split(','))
    rope = [i for i in range(256)]
    skip = 0
    cur = 0
    for length in lengths:
        sublist = [rope[i%256] for i in range(cur, cur+length)]
        for i in range(cur, cur+length):
            rope[i%256] = sublist.pop()
        cur += length + skip
        skip += 1
    return rope[0] * rope[1]

def part2():
    """
    answer should be 2da93395f1a6bb3472203252e3b17fe5
    """
    with open("10_1_in.txt", "r") as my_input:
        lengths = map(ord, my_input.read().strip())
    default_lengths = [17, 31, 73, 47, 23]
    lengths += default_lengths

    sparse_hash = [i for i in range(256)]
    skip = 0
    cur = 0
    for _ in range(64):
        for length in lengths:
            sublist = [sparse_hash[i%256] for i in range(cur, cur+length)]
            for i in range(cur, cur+length):
                sparse_hash[i%256] = sublist.pop()
            cur += length + skip
            skip += 1

# dense_hash = [reduce(lambda a, b: a ^ b, sparse_hash[16*i:16*(i+1)]) for i in range(16)]
    dense_hash = []
    for i in range(16):
        block = reduce(lambda a, b: a ^ b, sparse_hash[16*i:16*(i+1)])
        dense_hash.append(block)

# final = [format(chunk, "02x") for chunk in dense_hash]
    final = []
    for chunk in dense_hash:
        final.append(format(chunk, "02x"))
    return ''.join(final)

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
