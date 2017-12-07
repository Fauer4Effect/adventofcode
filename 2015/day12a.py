inputfile = open("input.txt",'r')

numlist = ['0','1','2','3','4','5','6','7','8','9']
total = 0
for char in inputfile:
    charlist = list(char)
    valuelist = []
    for i in range(len(charlist)):
        if charlist[i] not in numlist:
            value = ''.join(valuelist)
            valuelist = []
            try:
                total += int(value)
            except ValueError:
                pass

        else:
            valuelist.append(charlist[i])
            try:
                if charlist[i-1]=='-':
                    valuelist.insert(0,'-')
            except IndexError:
                pass


print(total)
