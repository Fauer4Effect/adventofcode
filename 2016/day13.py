from collections import deque

def is_open(x,y):
	if x <0 or y<0: return False
	num = x*x + 3*x + 2*x*y + y + y*y
	num += 1364
	num = bin(num)[2:]
	num_ones = num.count('1')
	return num_ones % 2 == 0

def bfs(start, goal):

	q = deque()
	explored = set()
	parent = {}
	distance = {}

	q.append(start)
	explored.add(start)
	distance[start] = 0

	while q:
		v1,v2 = q.popleft()
		cur_distance = distance[(v1,v2)]

		if (v1,v2)==goal:
			path = []
			try:
				par = parent[goal]
				while True:
					path.append(par)
					par = parent[par]
			except KeyError:
				return path, distance

		else:
			for i in range(-1,2):
				side = (v1+i,v2)
				up = (v1,v2+i)
				if side not in explored and is_open(side[0],side[1]):
					explored.add(side)
					q.append(side)
					parent[side] = (v1,v2)
					distance[side] = cur_distance+1

				if up not in explored and is_open(up[0],up[1]):
					explored.add(up)
					q.append(up)
					parent[up] = (v1,v2)
					distance[up] = cur_distance+1

start = (1,1)
goal = (31,39)
path, distance = bfs(start, goal)

#PART ONE ASKS US TO FIND THE SHORTEST PATH TO THE LOCATION SO WE USE BFS
print "LENGTH OF PATH:",len(path)

#PART 2 ASKS FOR ALL POINTS YOU CAN REACH IN 50 STEPS SO WE ADD A DICTIONARY THAT KEEPS TRACK OF HOW MANY STEPS WE'VE GONE
radius = []
for key,item in distance.iteritems():
	if item <= 50:
		radius.append(key)
print "PRINT IN RADIUS:",len(radius)