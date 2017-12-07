import collections


def part1(words):
	ans = ''
	for i in range(len(words[0])):
		letters = []
		for j in range(len(words)):
			letters += [words[j][i]]
		count = collections.Counter(letters)
		ans += count.most_common(1)[0][0]
	print ans

def part2(words):
	for i in range(len(words[0])):
		letters = []
		for j in range(len(words)):
			letters += [words[j][i]]
		count = collections.Counter(letters)
		print count



l = []
with open("6_1_in.txt","r") as file:
	for i in file:
		l += [i.strip()]
part1(l)
part2(l)