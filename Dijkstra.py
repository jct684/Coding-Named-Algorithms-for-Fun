import heapq
from collections import defaultdict

class Graph():

    def __init__(self):
        self.adjacency_list = {}

    def insert_node(self, data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            return

    def insert_directed_edge(self, vertex1, vertex2, weight):
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append((weight, vertex2))
            return
        return "Directed edge already exists"
    
    def show_graph(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')


def dijkstras_algorithm(adjacency_list):
    #time complexity O(m log n) where n is nodes and m is the number of edges
    #space complexity O(n)
    node_dist = defaultdict(lambda:float('inf')) #set the distance to infinity
    heap = [] #add shortest distance and node to heap
    parent = {} #stores the node that provided the shortest distance
    visited = set() #tracks nodes that have been visited before
    node_dist['s'] = 0 #pick any node from the set v_s and set distance to 0
    heapq.heappush(heap, (node_dist['s'], 's')) #use node_dist as key for heap
    while heap:
        heap_key, current_node = heapq.heappop(heap) #heap_key will not be used
        visited.add(current_node) #the shortest path to the current node has already been determined at this point
        for i in range(len(adjacency_list[current_node])):
            neighbor = adjacency_list[current_node][i][1] #retrieve neighbor
            neighbor_dist = adjacency_list[current_node][i][0] #retrieve distance to neighbor
            if neighbor not in visited: #no need to check nodes whose shortest pathis known
                current_dist = node_dist[current_node] + neighbor_dist #add distance from first node to current node + neighbor's node
                if current_dist < node_dist[neighbor]: #update if shorter path is found
                    parent[neighbor] = current_node #update parents to confirm path taken
                    node_dist[neighbor] = current_dist #update shorter distance
                    heapq.heappush(heap, (node_dist[neighbor], neighbor)) #add the neighbor to the heap
    return parent, node_dist
    

graph = Graph()
graph.insert_node('s')
graph.insert_node('t')
graph.insert_node('y')
graph.insert_node('x')
graph.insert_node('z')
graph.insert_directed_edge('s','t', 10)
graph.insert_directed_edge('s','y', 5)
graph.insert_directed_edge('t','y', 2)
graph.insert_directed_edge('y','t', 3)
graph.insert_directed_edge('t','x', 1)
graph.insert_directed_edge('y','x', 9)
graph.insert_directed_edge('y','z', 2)
graph.insert_directed_edge('x','z', 4)
graph.insert_directed_edge('z','x', 6)
graph.insert_directed_edge('z','s', 7)
graph.show_graph()

parent, node_dist = dijkstras_algorithm(graph.adjacency_list)
print("EXPECTED: ('t', 'y'), ('y', 's'), ('x', 't'), ('z', 'y')")
print(parent.items())
print("EXPECTED: ('s', 0), ('t', 8), ('y', 5), ('x', 9), ('z', 7)")
print(node_dist.items())
