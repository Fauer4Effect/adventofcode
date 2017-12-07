import re
from hashlib import md5

def quint_gen(part2):
	salt = "yjdafjpo"

	rg = re.compile(r'(.)\1{4}')
	quints = {}
	
	for i in range(0,40000):
		hash1 = md5(salt+str(i)).hexdigest()

		if part2:
			for j in range(2016):
				hash1 = md5(hash1).hexdigest()
		if rg.search(hash1) != None:
			quints[i] = (hash1, rg.findall(hash1)[0])	
	return quints

def find_keys(part2):
	index = -1
	count = 0
	salt = "yjdafjpo"
	rg1 = re.compile(r'(.)\1{2}')
	quints = quint_gen(part2)

	while count < 64:
		index += 1
		hash1 = md5(salt + str(index)).hexdigest()

		if part2:
			for i in range(2016):
				hash1 = md5(hash1).hexdigest()
		if rg1.search(hash1) != None:
			char1 = rg1.findall(hash1)[0]

			found = False
			for ind,(hash2,char2) in quints.iteritems():
				if char1 == char2 and 0 < ind-index <=1000:
					print "HASH 1: ", hash1, char1, index, count
					print "HASH 2: ", hash2, char2, ind, "\n"
					count += 1
					found = True

	return index


#PART1 WITH SALT ABC = 22728
#print find_keys(False)

#PART2 WITH SALT ABC = 22859
#part2 implements key stretching both for hash1 and hash2
print find_keys(True)