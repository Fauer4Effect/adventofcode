"""
Author: Kyle Fauerbach
Python solution to advent of code day 8
"""

from collections import deque

"""
Recursively handle getting the total metadata of a node.
If there's children then get their total first then get your own total.
Returns the total and the new serial since we don't have it defined as a global or anything.
"""
def do_child_simple(serial):
    children = serial.popleft()
    meta = serial.popleft()
    total = 0
    for _ in range(children):
        new_total, serial = do_child_simple(serial)
        total += new_total
    for _ in range(meta):
        total += serial.popleft()
    return total, serial

def part1():
    with open("8_1_in.txt", "r") as my_input:
        serial = deque(map(int, my_input.read().strip().split()))
    total = None
    while serial:
        total, serial = do_child_simple(serial)

    return total

def do_child_complex(serial):
    children = serial.popleft()
    meta = serial.popleft()
    value = 0

    # if the node has no children then its value is just the sum of the metadata
    if not children:
        for _ in range(meta):
            value += serial.popleft()
        return value, serial

    # python list is really an array and since we will be indexing during the metadata portion
    # we will use a normal list instead of a deque. Deque is optimized for append/remove from
    # either end but effiency of indexing near the middle of the deque is O(n).
    children_values = []
    for _ in range(children):
        new_value, serial = do_child_complex(serial)
        children_values.append(new_value)

    for _ in range(meta):
        metadata = serial.popleft()
        new_value = 0
        if metadata <= len(children_values):
            new_value = children_values[metadata-1]
        value += new_value
    return value, serial

def part2():
    with open("8_1_in.txt", "r") as my_input:
        serial = deque(map(int, my_input.read().strip().split()))

    value = 0
    while serial:
        value, serial = do_child_complex(serial)

    return value

if __name__ == "__main__":
    print(part1())
    print(part2())
