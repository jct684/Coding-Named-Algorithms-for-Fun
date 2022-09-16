from collections import deque

class Graph():

    def __init__(self):
        self.adjacency_list = {}

    def insert_node(self, data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            return

    def insert_directed_edge(self, vertex1, vertex2):
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            return
        return "Directed edge already exists"
    
    def show_graph(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')


def Kahns_algorithm(graph):
    q = deque()
    num_edges = {key:0 for key in graph}
    output = []
    for v in graph.values():
        for num in v:
            num_edges[num] += 1
    for k, v in num_edges.items():
        if v == 0:
            q.append(k)
    while len(q) > 0:
        current = q.popleft()
        del num_edges[current]
        output.append(current)
        for nums in graph[current]:
            num_edges[nums] -= 1
            if num_edges[nums] == 0:
                q.append(nums)
    return output
    

graph = Graph()
graph.insert_node(5)
graph.insert_node(7)
graph.insert_node(3)
graph.insert_node(11)
graph.insert_node(8)
graph.insert_node(2)
graph.insert_node(9)
graph.insert_node(10)
graph.insert_directed_edge(5,11)
graph.insert_directed_edge(7,11)
graph.insert_directed_edge(7,8)
graph.insert_directed_edge(3,10)
graph.insert_directed_edge(3,8)
graph.insert_directed_edge(11,2)
graph.insert_directed_edge(11,9)
graph.insert_directed_edge(11,10)
graph.insert_directed_edge(8,9)
graph.show_graph()

print("Expected: [5, 7, 3, 11, 8, 2, 10, 9]")
print(Kahns_algorithm(graph.adjacency_list))
