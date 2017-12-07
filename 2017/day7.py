"""
Author: Kyle Fauerbach
Python solution to advent of code day 7
"""
def part1():
    """
    answer should be hlhomy
    """
    with open("7_1_in.txt", "r") as my_input:
        matrix = map(str.strip, my_input.readlines())
    tree = {}
    alone = set()
    for entry in matrix:
        entry = entry.split('->')
        if len(entry) > 1:
            parent = entry[0].split(' ')[0].strip()
            children = map(str.strip, entry[1].split(','))
            for child in children:
                tree[child] = parent
    for child, parent in tree.iteritems():
        if parent not in tree.keys():
            alone.add(parent)
    return alone
        

def part2():
    """
    we want the highest bad program so we want the first one that prints as bad
    when we run it we can see that the first bad output is
        rugzyaj [1579, 1571, 1571, 1571] ['apjxafk', 'jngcap', 'wrtyhxg', 'hblcbb']
    from that we can see that the weight of the a apjxafk stack is wrong
    we go and pull the weight for apjxafk and see that it weights 1513
    from that bad output we can see that the stack of apjxafk weighs 8 more than it should
    so we subtract that 8 from the weight of the apjxafk node

    answer should be 1505
    """
    with open("7_1_in.txt", "r") as my_input:
        matrix = map(str.strip, my_input.readlines())
    tree = {}
    ind_weights = {}
    for entry in matrix:
        entry = entry.split('->')
        program = entry[0].split(' ')[0].strip()
        weight = int(entry[0].split(' ')[1].strip()[1:-1])
        ind_weights[program] = weight
        if len(entry) > 1:
            parent = entry[0].split(' ')[0].strip()
            children = map(str.strip, entry[1].split(','))
            tree[parent] = children
    
    def get_weight(root):
        children = tree.get(root) or None
        if children is None:
            return ind_weights[root]
        else:
            children_weights = [get_weight(child) for child in children]
            if len(set(children_weights)) > 1:
                print root, children_weights, tree[root]
            return ind_weights[root] + sum(children_weights)
    get_weight('hlhomy')
        
        


if __name__ == "__main__":
    print "part1", part1()
    part2()
