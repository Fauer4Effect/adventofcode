"""
Author: Kyle Fauerbach
Python solution to advent of code day 14
"""

def part1():
    recipes = [3,7]
    num_recipes = 2
    elf1_index = 0
    elf2_index = 1
    elf1_step = 0
    elf2_step = 0
    goal = 990941
    additional = 10
    ans = []
    while num_recipes < goal+additional:
        elf1_index = (elf1_index + elf1_step) % len(recipes)
        elf2_index = (elf2_index + elf2_step) % len(recipes)
        elf1_recipe = recipes[elf1_index]
        elf2_recipe = recipes[elf2_index]
        new_recipe = elf1_recipe + elf2_recipe
        new_str = str(new_recipe)
        for c in new_str:
            if num_recipes >= goal:
                ans.append(c)
            recipes.append(int(c))
            num_recipes += 1
        elf1_step = 1 + elf1_recipe
        elf2_step = 1 + elf2_recipe

    return ''.join(ans)

def part2():
    recipes = [3,7]
    num_recipes = 2
    elf1_index = 0
    elf2_index = 1
    elf1_step = 0
    elf2_step = 0
    goal = "990941"
    while 1:
        elf1_index = (elf1_index + elf1_step) % len(recipes)
        elf2_index = (elf2_index + elf2_step) % len(recipes)
        elf1_recipe = recipes[elf1_index]
        elf2_recipe = recipes[elf2_index]
        new_recipe = elf1_recipe + elf2_recipe
        new_str = str(new_recipe)
        for c in new_str:
            if goal == ''.join(map(str, recipes[-len(goal):])):
                return num_recipes - len(goal)
            recipes.append(int(c))
            num_recipes += 1
        elf1_step = 1 + elf1_recipe
        elf2_step = 1 + elf2_recipe

    return None

if __name__ == "__main__":
    print(part1())
    print(part2())
