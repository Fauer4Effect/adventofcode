import collections
import string


norm = "abcdefghijklmnopqrstuvwxyz"

def part1(line):
	sector_id = line[-10:-7]
	checksum = line[-6:-1]
	num = line[:-11].replace('-','')

	count = collections.Counter(num)
	keys = count.keys()
	keys = sorted(keys)
	keys = sorted(keys, key=lambda x: -count[x])
	check = ''.join(keys[:5])

	if check == checksum: return int(sector_id)
	else: return 0


def part2(line):
	sector_id = line[-10:-7]
	num = line[:-11].replace('-',' ')

	shift = int(sector_id)%26
	mapped = norm[shift:] + norm[:shift]

	unencrypt = string.maketrans(norm,mapped)
	return string.translate(line,unencrypt)

total = 0
with open("4_1_in.txt","r") as file:
	# for i in file:
	# 	total += part1(i.strip())

	for i in file:
		print part2(i.strip())
print total

