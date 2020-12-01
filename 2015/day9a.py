#python classes to represent graphs
from representingGraphsInPython import *

inputfile = open('input9.txt','r')

#generate weighted graph from input
g = Graph()
citylist = []
for line in inputfile:
    linelist = line.strip().split()
    linelist.pop(1)
    linelist.pop(2)

    city1 = linelist[0]
    city2 = linelist[1]
    dist = int(linelist[2])
    
    if city1 not in citylist:
        g.add_vertex(city1)
        citylist.append(city1)
    if city2 not in citylist:
        g.add_vertex(city2)
        citylist.append(city2)

    g.add_edge(city1,city2,dist)

#implement nearest neighbor algorithm using each vertex as a starting point
for start in g:
    notVisited = citylist[:]
    adjacentlist = {}
    finalPathLength = 0

    notVisited.remove(start.get_id())
    while len(notVisited) != 0:
        adjacentlist = {}

        for next in start.get_connections():
                wid = next
                dist = start.get_weight(next)
                adjacentlist[wid] = dist

        minCity = ''
        minDist = 99999999
        for key in adjacentlist:
            if key.get_id() in notVisited:
                if adjacentlist[key] < minDist:
                    minCity = key.get_id()
                    cityName = key
                    minDist = adjacentlist[key]

        finalPathLength += minDist
        try:
            notVisited.remove(minCity)
        except ValueError:
            break
        start = cityName
    
    #print length of each path, and make sure all cities visited
    print(finalPathLength,notVisited)
    


