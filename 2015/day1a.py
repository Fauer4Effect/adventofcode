inputfile = open("input1.txt",'r')

for string in inputfile:
    list1= list(string)


floor = 0
for i in range(len(list1)):
    val = list1[i]
    if val=='(':
        floor += 1
    else:
        floor -= 1
print(floor)