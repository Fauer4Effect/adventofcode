def initialize(wide, tall):
	matrix = [['.' for y in range(wide)] for x in range(tall)]
	return matrix

def print_matrix(matrix):
	for i in range(len(matrix)):
		print matrix[i]

def turn_on(x,y,matrix):
	for i in range(y):
		for j in range(x):
			matrix[i][j] = "#"
	return matrix

def shift_col(col, shift, matrix):
	column = [matrix[i][col] for i in range(len(matrix))]
	column = column[-shift:]+column[:-shift]

	for i in range(len(matrix)):
		matrix[i][col] = column[i]
	return matrix

def shift_row(row, shift, matrix):
	rows = matrix[row]
	rows = rows[-shift:]+rows[:-shift]
	
	matrix[row] = rows
	return matrix

def count(matrix):
	count = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == "#": count += 1
	return count

def part1(line,matrix):
	line = line.split(' ')
	if line[0] == "rect":
		line = map(int, list(line[1].split('x')))
		matrix = turn_on(line[0],line[1],matrix)
	elif line[0] == "rotate" and line[1] == "column":
		col = int(line[2].split('=')[1])
		shift_val = int(line[-1])
		matrix = shift_col(col, shift_val, matrix)
	else:
		row = int(line[2].split('=')[1])
		shift_val = int(line[-1])
		matrix = shift_row(row, shift_val, matrix)

wide =  50
tall = 6
matrix = initialize(wide, tall)

with open("8_1_in.txt","r") as file:
	for line in file:
		part1(line,matrix)
print_matrix(matrix)
print "\n"
print "NUMBER TURNED ON: " + str(count(matrix))

# PART 1 TEST CASES
# wide = 7
# tall = 3
# matrix = initialize(wide, tall)
# part1("rect 3x2",matrix)
# part1("rotate column x=1 by 1", matrix)
# part1("rotate row y=0 by 4", matrix)
# part1("rotate column x=1 by 1", matrix)
