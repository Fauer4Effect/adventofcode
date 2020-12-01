import re

#searches if abba is in the str
def abba(str):
	rg1 = re.compile(r'(.)(?!\1)(.)\2\1')
	return rg1.search(str) != None

def part1(line):
	#searches for []
	rg2 = re.compile(r'\[.*?\]')
	#gets stuff inside []
	for mid in rg2.findall(line):
		#if abba in inside
		if abba(mid): return False
	#is there abba in outside
	return abba(line)



def part2(line):
	#searches for []
	rg1 = re.compile(r'\[.*?\]')
	#strings of aba
	rg2 = re.compile(r'(?=((.)(?!\2).\2))')


	#outside of []
	outside = re.split(rg1, line)
	#inside of []
	ins = rg1.findall(line)
	inside1 = [i[1:-1] for i in ins]

	#inside of [] matches aba
	inner_aba = []
	for i in inside1:
		inner = rg2.findall(i)
		for j in inner:
			inner_aba.append(j[0])

	# outside of [] matches aba
	outeraba = []
	for out in outside:
		o = rg2.findall(out)
		for i in o:
			outeraba.append(i[0])

	for i in inner_aba:
		for j in outeraba:
			if j[1]+j[0]+j[1] == i:	return 1

	return 0				

tsl = 0
ssl = 0
with open("7_1_in.txt","r") as file:
	for line in file:
		if part1(line.strip()): tsl += 1
		ssl += part2(line)
print "PART 1: " + str(tsl)
print "PART 2: " + str(ssl)

# PART 2 TEST CASES
# print part2("aba[babcdc]xyz")
# print part2("xyx[xyx]xyx")
# print part2("aaa[kek]eke")
# print part2("zazbz[bzb]cdb")
# print part2("aba[cdc]xyz[bab]aaa")
# print part2("aaaaa[aaaaaaa]ababa[aaa]zyz")
