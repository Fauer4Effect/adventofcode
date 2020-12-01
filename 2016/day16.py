import string

#using maketrans and translate to swap 0s and 1s
norm = "01"
mapped = "10"
swap = string.maketrans(norm,mapped)

def dragon_curve(a,desired_length):
	b = a[::-1]
	b = string.translate(b,swap)
	a = a+"0"+b
	cur_lenth = len(a)
	if cur_lenth<desired_length:
		a = dragon_curve(a,desired_length)
	return a[:desired_length]

def checksum(line):
	check = ''
	for i in range(0,len(line), 2):
		chunk = line[i:i+2]
		if chunk=="00" or chunk=="11":
			check += "1"
		else:
			check += "0"
	if len(check)%2==0: 
		check = checksum(check)
	return check



inpt = "10010000000110000"

#PART 1
d = dragon_curve(inpt,272)

#PART 2
#d = dragon_curve(inpt,35651584)

print "RAND DATA FOUND"
c = checksum(d)
print "CHECKSUM IS: ",c