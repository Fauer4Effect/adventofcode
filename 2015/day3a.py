inputfile = open('input3.txt','r')
for line in inputfile:
    commands = list(line.strip())
    
    matrix = [[0]*2000 for r in range(2001)]

    row = 999
    col = 999
    for command in commands:
        presents = matrix[row][col]
        matrix[row][col] = presents + 1
        if command =='^':
            row -= 1
        elif command =='<':
            col -= 1
        elif command =='>':
            col += 1
        else:
            row += 1
    presents = matrix[row][col]
    matrix[row][col] = presents + 1 

    count = 0    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] >= 1:
                count += 1
print(count)
