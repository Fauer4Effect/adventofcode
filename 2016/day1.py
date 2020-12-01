file = open("1_1_in.txt","r")
inpt = file.readline()
inpt = inpt.strip().split(", ")

def part1(data):
	v = (0, 1); x = 0; y = 0
	for item in data:
	    l = int("".join(item[1:]))
	    v = (v[1], -v[0]) if item[0] == "R" else (-v[1], v[0])
	    x += v[0] * l
	    y += v[1] * l
	return (x,y)

def part2(data):
    v = (0, 1); x = 0; y = 0
    seen = []
    for item in data:
        l = int("".join(item[1:]))
        v = (v[1], -v[0]) if item[0] == "R" else (-v[1], v[0])
        for ad in range(l):
            x += v[0]
            y += v[1]
            if (x,y) in seen: return (x,y)
            seen.append((x,y))

print part1(inpt)
print part2(inpt)