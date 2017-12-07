def decompress(line):
	i = 0
	new_line = ''

	while i < len(line):
		ind = line.find("(")
		if ind != -1 and i == ind: 
			end = line.find(")")

			mult = line[ind+1:end]

			i += len(mult)+2

			mult = mult.split('x')
			num = int(mult[0])
			repeat = int(mult[1])

			chunk = line[i:i+num]
			chunk = chunk*repeat
			new_line += chunk

			line = line[end+num+1:]
			i = 0

		else: 
			new_line += line[i]
			i += 1

	return new_line

def decomp_count(line):
    if '(' not in line:
        return len(line)
    num_chars = 0
    while '(' in line:
        num_chars += line.find('(')
        line = line[line.find('('):]
        marker = line[1:line.find(')')].split('x')
        line = line[line.find(')') + 1:]
        num_chars += decomp_count(line[:int(marker[0])]) * int(marker[1])

        line = line[int(marker[0]):]
    num_chars += len(line)
    return num_chars


ans1 = ''
with open("9_1_in.txt","r") as file:
	for line in file:
		ans1 += decompress(line.strip())
		#ans2 += decomp_count(line.strip())
		
print len(ans1)

with open("9_1_in.txt","r") as file:
	inpt = file.read().strip()
print decomp_count(inpt)

#PART 2 TEST CASES
# ans1 = decompress("(27x12)(20x12)(13x14)(7x10)(1x12)A")
# ans1 = decompress("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")
# has_paren = ans1.find("(")
# while has_paren != -1:
# 	ans1 = decompress(ans1)
# 	print (len(ans1))
# 	has_paren = ans1.find("(")


# PART 1 TEST CASES
# decompress("ADVENT")
# decompress("A(1x5)BC")
# decompress("(3x3)XYZ")
# decompress("A(2x2)BCD(2x2)EFG")
# decompress("(6x1)(1x3)A")
# decompress("X(8x2)(3x3)ABCY")
