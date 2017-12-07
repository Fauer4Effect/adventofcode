from hashlib import md5

start = "uqwqemis"

def part1():
	count = 0
	ans = ''
	for i in range(100000000):
		if count == 8: break
		h = md5(start + str(i)).hexdigest()
		if h[:5] == '00000':
			ans += h[5]
			count += 1
	print ans

def part2():
	count = 0
	indexes = []
	ans = [0,0,0,0,0,0,0,0]
	for i in range(100000000):
		if count == 8: break
		h = md5(start + str(i)).hexdigest()
		if h[:5] == '00000':
			try:
				if int(h[5]) in range(8) and h[5] not in indexes:
					ans[int(h[5])] = h[6]
					count += 1
					indexes.append(h[5])
			except ValueError as e:
				pass
	print ''.join(ans)

print "PART 1:"
part1()
print "\nPART 2:"
part2()


