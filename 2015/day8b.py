inputfile = open('input8.txt','r')

countlit = 0
countmem = 0

for line in inputfile:
    line = line.strip()
    lit = len(line)
    countlit += lit
    
    mem = lit
    i = 0
    while i < lit:
        if line[i] =="\"":
            mem += 1
        elif line[i] =="\\":
            mem += 1
        i += 1
    mem += 2    #add two for the start/end quotes
    countmem += mem

print(countmem,countlit)
print(countmem - countlit)