"""
Author: Kyle Fauerbach
Python solution to advent of code day 12
"""

def part1():

    commands = {}
    with open("12_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()
    for cmd in my_input:
        cmd = cmd.strip().split(' => ')
        commands[cmd[0]] = cmd[1]

    state = list("##.####..####...#.####..##.#..##..#####.##.#..#...#.###.###....####.###...##..#...##.#.#...##.##..")
    zero_index = 0

    for _ in range(20):
        state = list('.'*4) + state + list('.'*4)
        zero_index += 4
        new_state = ['.' for _ in range(len(state))]
        for i in range(2, len(state)-2):
            chunk = ''.join(state[i-2:i+3])
            new_state[i] = commands.get(chunk, '.')
        state = new_state

    positives = state[zero_index:]
    negatives = state[:zero_index][::-1]
    total = 0
    for i in range(len(positives)):
        if positives[i] == '#':
            total += i
    for i in range(len(negatives)):
        if negatives[i] == '#':
            total -= (i+1)

    return total

def part2():
    """
    We copied the code from part 1 and instead of going for 20 generations we went for 200
    From that we can see that after 142 generations we are only adding 32 to total
    knowing the total at generation 200 was 18321 we can calculate the future value.
    """
    commands = {}
    with open("12_1_in.txt", "r") as my_input:
        my_input = my_input.readlines()
    for cmd in my_input:
        cmd = cmd.strip().split(' => ')
        commands[cmd[0]] = cmd[1]

    state = list("##.####..####...#.####..##.#..##..#####.##.#..#...#.###.###....####.###...##..#...##.#.#...##.##..")
    zero_index = 0

    for _ in range(200):
        state = list('.'*4) + state + list('.'*4)
        zero_index += 4
        new_state = ['.' for _ in range(len(state))]
        for i in range(2, len(state)-2):
            chunk = ''.join(state[i-2:i+3])
            new_state[i] = commands.get(chunk, '.')
        state = new_state

    positives = state[zero_index:]
    negatives = state[:zero_index][::-1]
    total = 0
    for i in range(len(positives)):
        if positives[i] == '#':
            total += i
    for i in range(len(negatives)):
        if negatives[i] == '#':
            total -= (i+1)

    return ((50000000000 - 200) * 32) + total


if __name__ == "__main__":
    print(part1())
    print(part2())
