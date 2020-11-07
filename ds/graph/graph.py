# vertex
# edge

class Graph:
    def __init__(self):
        self.graph = {}

    def add(self, vertex, edges):
        if vertex in self.graph:
            self.graph[vertex] = self.graph[vertex] + edges
        else:
            self.graph[vertex] = edges

        return self.graph

    def bfs(self, source):
        queue = []
        visited = set()
        queue.append(source)
        visited.add(source)

        while queue:
            current = queue.pop(0)
            print(current)
            for edges in self.graph[current]:
                if edges not in visited:
                    queue.append(edges)
                    visited.add(edges)

    def dfs(self, source, visited=None):
        if visited == None:
            visited = set()

        visited.add(source)
        print(source)

        for edges in self.graph[source]:
            if edges not in visited:
                self.dfs(edges, visited)
        
graph = Graph()
graph.add('A', ["B"])
graph.add('B', ["C", "E"])
graph.add('C', ["D"])
graph.add('D', [])
graph.add('E', ["F"])
graph.add('F', ["D"])

print("BFS")
graph.bfs('A')

print("DFS")
graph.dfs('A')