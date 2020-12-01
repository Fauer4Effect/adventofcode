def part1(steps):
	x = 0; y = 0
	for i in steps:
		if i == "U" and y < 1: y += 1; 
		elif i == "L" and x > -1: x -= 1
		elif i == "R" and x < 1: x += 1
		elif i == "D" and y > -1: y -= 1
		else: pass
	print x,y

def part2(steps):
	x = 0; y = 0
	valid_moves = {"-2,0":"R", "2,0":"L","-1,1":["D","R"], "-1,-1":["U","R"], "-1,0":["L","U","R","D"], "0,2":"D", "0,-2":"U",
		"0,1":["L","U","R","D"], "0,0":["L","U","R","D"], "0,-1":["L","U","R","D"], "1,1":["L","D"], "1,-1":["L","U"], "1,0":["L","U","R","D"]}

	for i in steps:
		if i not in valid_moves[str(x)+","+str(y)]: pass
		else:
			if i == "U": y += 1; 
			elif i == "L": x -= 1
			elif i == "R": x += 1
			elif i == "D": y -= 1
	print x,y


with open("2_1_in.txt","r") as file:
	for line in file:
		#part1(line)
		part2(line)