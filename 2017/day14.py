"""
Author: Kyle Fauerbach
Python solution to advent of code day 14
"""

def knot_hash(my_input):
    """
    helper function that calculates a knot hash
    """
    lengths = map(ord, my_input)
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

def part1():
    """
    my_input = "hxtvlmkl"
    answer should be 8214
    """
    used = 0
    for i in range(128):
        hsh = knot_hash("hxtvlmkl-" + str(i))
        row = str(bin(int(hsh, 16))[2:].zfill(128))
        row = list("0"*(128-len(row)) + row)
        for space in row:
            if space == '1':
                used += 1
    return used

def part2():
    """
    answer should be 1093
    """
    unseen = []
    for i in range(128):
        hsh = knot_hash("hxtvlmkl-" + str(i))
        row = bin(int(hsh, 16))[2:].zfill(128)
        unseen += [(i, j) for j, d in enumerate(row) if d == '1']
    groups = 0
    while unseen:
        queued = [unseen[0]]
        while queued:
            (x, y) = queued.pop()
            if (x, y) in unseen:
                unseen.remove((x, y))
                queued += [(x - 1, y), (x+ 1, y), (x, y+1), (x, y-1)]
        groups += 1
    return groups

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
