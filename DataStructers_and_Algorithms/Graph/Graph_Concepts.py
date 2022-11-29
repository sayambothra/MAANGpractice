class Graph:
    # def __init__(self,graphDict=None):
    #     if graphDict == None:
    #         graphDict={}
    #     self.graphDict=graphDict
    #
    # def addEdge(self,vertex,edge):
    #     self.graphDict[vertex].append(edge)
    def __init__(self):
        self.adjacency_list={}
    def addVertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex]=[]
            return True
        return False
    def printGraph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                print("Edge or Vertex does not exist")
                return True
        return False
    def removeVertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            for othervertex in self.adjacency_list[vertex]:
                self.adjacency_list[othervertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False





customDict={"a":["b","c"],
            "b":["a","d","e"],
            "c":["a","e"],
            "d":["b","e","f"],
            "e":["d","f","c"],
            "f":["d","e"]
            }
graph=Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addEdge("A","B")
graph.addEdge("B","C")
graph.addEdge("A","C")
graph.addEdge("D","C")
graph.addEdge("D","A")
graph.printGraph()
# print(graph.addEdge("C","d"))
# graph.removeEdge("A","b")
print("After Remove")
graph.removeVertex("D")
graph.printGraph()