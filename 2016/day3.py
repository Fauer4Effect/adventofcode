def validator(tri):
	tri = list(map(lambda x: int(x),tri.strip().split()))

	if tri[0] + tri[1] <= tri[2]: return 0
	elif tri[0] + tri[2] <= tri[1]: return 0
	elif tri[1] + tri[2] <= tri[0]: return 0
	else: return 1
			
valid = 0
with open("3_1_in.txt","r") as file:
	#PART 1 SOLUTION
	#for tri in file:
	#	valid += validator(tri)
	

	#DAY 2 SOLUTION
	al = file.read().strip().split()
	print al
	#READ BY COLUMNS, THREE COLUMNS PER LINE SO REPEAT IT THREE TIMES
	for i in range(3):
		for j in range(i,len(al)-6,9):
			tri = al[j] + ' '+ al[j+3] +' '+ al[j+6]
			valid += validator(tri)


print valid