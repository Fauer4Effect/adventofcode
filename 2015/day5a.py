inputfile = open('input5.txt','r')

numnice = 0
for line in inputfile:
    nice = True
    line = line.strip()
    if 'ab' in line:
        nice = False
    if 'cd' in line:
        nice = False
    if 'pq' in line:
        nice = False
    if 'xy' in line:
        nice = False

    counta = line.count('a')
    counte = line.count('e')
    counti = line.count('i')
    counto = line.count('o')
    countu = line.count('u')
    vowelcount = counta+counte+counti+counto+countu
    if vowelcount < 3:
        nice = False

    countdouble = 0
    linelist = list(line)
    for i in range(len(linelist)-1):
        if linelist[i] == linelist[i+1]:
            countdouble += 1
    if countdouble == 0:
        nice = False

    if nice:
        numnice += 1
print(numnice)