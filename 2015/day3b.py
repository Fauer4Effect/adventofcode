inputfile = open('input3.txt','r')
for line in inputfile:
    commands = list(line.strip())
    
    matrix = [[0]*2000 for r in range(2001)]

    rowS = 999
    colS = 999
    rowR = 999
    colR = 999
    step = 0
    for command in commands:
        if step%2 != 0:
            presents = matrix[rowR][colR]
            matrix[rowR][colR] = presents + 1
            if command =='^':
                rowR -= 1
            elif command =='<':
                colR -= 1
            elif command =='>':
                colR += 1
            else:
                rowR += 1
            presents = matrix[rowR][colR]
            matrix[rowR][colR] = presents + 1     

        else:
            presents = matrix[rowS][colS]
            matrix[rowS][colS] = presents + 1
            if command =='^':
                rowS -= 1
            elif command =='<':
                colS -= 1
            elif command =='>':
                colS += 1
            else:
                rowS += 1
            presents = matrix[rowS][colS]
            matrix[rowS][colS] = presents + 1

        step += 1 

    count = 0    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] >= 1:
                count += 1
print(count)
