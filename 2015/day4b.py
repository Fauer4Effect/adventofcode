import md5

myinput =  "yzbqklnj"

hash1 = md5.new(myinput).hexdigest()
#print(hash1)
x = hash1[:6]
#print(x)

i = 0
while x != '000000':
    hash1 = md5.new(myinput+str(i)).hexdigest()
    x = hash1[:6]
    print(x,i)
    i += 1

print(str(i-1)) #subtract 1 to account for the extra addition

