myinput ='1113122113'

inputlist = list(myinput)
inputlist.append(' ')   #add empty space to end so loop stays in bound

for i in range(40):
    output = []
    count = 1
    for i in range(len(inputlist)):
        if i + 1 < len(inputlist):
            if inputlist[i]==inputlist[i+1]:
                count += 1

            else:
                output.append(str(count))
                output.append(inputlist[i])
                count = 1
    inputlist = output[:]
    inputlist.append(' ')

inputlist.pop()   #remove extra space added at end of loop
print(len(inputlist))



