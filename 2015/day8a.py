inputfile = open('input8.txt','r')

countlit = 0
countmem = 0

for line in inputfile:
    line = line.strip()
    lit = len(line)
    countlit += lit
    
    mem = lit - 2 #start and end quotes
    i = 0
    while i < lit:
        #print(line[i])
        if line[i] == '\\':
            if line[i+1] =='x':
                mem -= 3
                i += 3
            elif line[i+1] =='"':
                mem -= 1
                i += 1
            elif line[i+1] =='\\':
                mem -= 1
                i += 1
        i += 1
    countmem += mem
    
print(countlit,countmem)
print(countlit - countmem)