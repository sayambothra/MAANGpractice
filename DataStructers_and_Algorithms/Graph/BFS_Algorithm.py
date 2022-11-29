class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex): #TC:O(V+E),SC:O(V+E)
        visited=[vertex]
        queue=[vertex]
        while queue:
            deVertex=queue.pop(0)
            print(deVertex)
            for adjacent in self.gdict[deVertex]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    queue.append(adjacent)



customDict={"a":["b","c"],
            "b":["a","d","e"],
            "c":["a","e"],
            "d":["b","e","f"],
            "e":["d","f"],
            "f":["d","e"]
}

graph=Graph(customDict)
graph.bfs("a")
