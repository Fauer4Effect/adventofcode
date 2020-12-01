'''
The Vertex class uses a dictionary (adjacent) to keep track of the vertices 
to which it is connected, and the weight of each edge. The Vertex constructor 
initializes the id, which is usually a string, and the adjacent dictionary. 
The add_neighbor() method is used add a connection from this vertex to another. 
The get_connections() method returns all of the vertices in the adjacency list. 
The get_weight() method returns the weight of the edge from this vertex to the 
vertex passed as a parameter.

The Graph class contains a dictionary(vert-dict) that maps vertex names to vertex 
objects, and we can see the output by the __str__() method of Vertex class:

Graph also provides methods for adding vertices to a graph and connecting one vertex 
to another. The get_vertices() method returns the names of all of the vertices in 
the graph. Also, we have the __iter__() method to make it easy to iterate over 
all the vertex objects in a particular graph. Together, the two methods allow 
us to iterate over the vertices in a graph by name, or by the objects themselves.

In main(), we created six vertices laebled 'a' through 'f'. Then we displayed 
the vertex dictionary. Notice that for each key 'a' through 'f' we have created
an instance of a Vertex. Next, we add the edges that connect the vertices together. 
Finally, a nested loop verifies that each edge in the graph is properly stored. 
'''

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

    for v in g:
        print 'g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()])