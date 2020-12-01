inputfile = open('input5.txt','r')

numnice = 0
for line in inputfile:
    nice = True

    countdub = 0
    for i in range(len(line)-1):
        chars = line[i:i+2]
        if line.count(chars)>1:
            countdub += 1
    if countdub == 0:
        nice = False


    countgap = 0
    linelist = list(line)
    for i in range(len(linelist)-2):
        if linelist[i]==linelist[i+2]:
            countgap += 1
    if countgap == 0:
        nice = False

    if nice:
        numnice += 1
print(numnice)