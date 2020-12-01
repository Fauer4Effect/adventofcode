
def sculpture(time):
	goal = False
	
	time += 1
	d1 = (15+time) % 17
	if d1 == 0:
		first = True
	else:
		first = False
	
	time += 1
	d2 = (2+time) % 3
	if first and d2==0:
		second = True
	else:
		second = False
	
	time += 1
	d3 = (4+time) % 19
	if second and d3==0:
		third = True
	else:
		third = False

	time += 1
	d4 = (2+time)%13
	if third and d4==0:
		fourth = True
	else:
		fourth = False

	time += 1
	d5 = (2+time) % 7
	if fourth and d5==0:
		fifth = True
	else:
		fifth = False

	time += 1
	d6 = (0+time) % 5
	if fifth and d6 == 0:
		sixth = True
	else:
		sixth = False

	# PART 1
	# if sixth:
	# 	goal = True

	# PART 2 ADDS ADDITIONAL DISK
	time += 1
	d7 = (0+time) % 11
	if sixth and d7==0:
		seventh = True
	else:
		seventh = False

	if seventh:
		goal = True


	if goal:
		print "CORRECT TIME IS:",i


for i in range(10000000):
	sculpture(i)