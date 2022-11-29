class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def dfs(self,vertex): #TC:O(V+E) , SC:O(V+E)
        visited=[vertex]
        stack=[vertex]
        while stack:
            popVertex=stack.pop()
            print(popVertex)
            for adjacent in self.gdict[popVertex]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    stack.append(adjacent)


customDict={"a":["b","c"],
            "b":["a","d","e"],
            "c":["a","e"],
            "d":["b","e","f"],
            "e":["d","f"],
            "f":["d","e"]
}

graph=Graph(customDict)
graph.dfs("a")

