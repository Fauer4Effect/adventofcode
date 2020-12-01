a = 0
b = 0
c = 0	#define c=0 for part1 and c=1 for part2
d = 0


instructions = []
with open("12_1_in.txt","r") as file:
	for line in file:
		instructions.append(line.strip().split(' '))
# for i in range(len(instructions)):
i = 0
while i < len(instructions):
	cur_inst = instructions[i]
	if cur_inst[0] == 'cpy':
		if cur_inst[1] in ['a','b','c','d']:
			exec(cur_inst[2]+"="+cur_inst[1])
		else:
			exec(cur_inst[2] + "=int("+cur_inst[1]+")")
		i += 1
	elif cur_inst[0] == 'dec':
		exec(cur_inst[1]+"-=1")
		i+= 1
	elif cur_inst[0] == 'inc':
		exec(cur_inst[1]+"+=1")
		i+= 1
	elif cur_inst[0] == 'jnz':
		if cur_inst[1] in ['a','b','c','d']:
			cur_val = eval(cur_inst[1])
			if cur_val != 0:
				exec("i+=int("+cur_inst[2]+")")
			else: i += 1
		else:
			if int(cur_inst[1]) != 0:
				exec("i+=int("+cur_inst[2]+")")
			else: i += 1
	else: i += 1

print a,b,c,d

		