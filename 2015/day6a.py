inputfile = open('input6.txt','r')

matrix = [[0]*1000 for row in range(1000)]

for line in inputfile:
    #parse input into variables
    i = 0
    while not line[i].isdigit():
        i += 1
    j = i    
    command = line[:i]

    while line[i].isdigit():
        i += 1 
    startx = int(line[j:i])
    i += 1
    j = i
    while line[i].isdigit():
        i += 1
    starty = int(line[j:i])

    i += 9
    j = i
    while line[i].isdigit():
        i += 1
    endx = int(line[j:i])
    i += 1
    j = i
    while line[i].isdigit():
        i += 1
    endy = int(line[j:i])

    if 'on' in command:
        for r in range(startx,endx+1):
            for c in range(starty,endy+1):
                if matrix[r][c] == 0:
                    matrix[r][c] = 1
    elif 'off' in command:
        for r  in range(startx,endx+1):
            for c in range(starty,endy+1):
                if matrix[r][c] == 1:
                    matrix[r][c] = 0
    elif 'toggle' in command:
        for r in range(startx,endx+1):
            for c in range(starty,endy+1):
                if matrix[r][c] == 0:
                    matrix[r][c] = 1
                else:
                    matrix[r][c] = 0

counton = 0
for r in range(1000):
    for c in range(1000):
        if matrix[r][c] == 1:
            counton += 1
print(counton)