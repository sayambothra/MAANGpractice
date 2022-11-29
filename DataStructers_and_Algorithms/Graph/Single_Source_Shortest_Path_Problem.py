import heapq


class Graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict={}
        self.gdict=gdict



#BFS is applicavle only for unweighted graph
    def bfs(self,start,end):  #TC:O(E) , SC:O(E)
        queue=[]
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node  == end:
                return path
            for adjacent in self.gdict.get(node,[]):
                new_path=list(path)
                new_path.append(adjacent)
                queue.append(new_path)


customDict={"a":["b","c"],
            "b":["d","g"],
            "c":["d","e"],
            "d":["f"],
            "e":["f"],
            "g":["f"]}

g=Graph(customDict)
print(g.bfs("a","f"))

#Single Source Shortest Path Problem - Using Dijsktra's Algorithm

#class for Edge:
class Edge:
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight=weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertex
#class For Node
class Node:
    def __init__(self,name):
        self.name=name
        self.visited=False
        #Previous node that we come to this the node
        self.predecessor=name
        self.neighbors=[]
        self.min_distance=float("inf")

    #To Compare minimun distance of nodes
    def __lt__(self,other_node):
        return self.min_distance <other_node.min_distance

    def add_Edge(self,weight,destination_vertex):
        edge=Edge(weight,self,destination_vertex)
        self.neighbors.append(edge)

#Dijsktra Algorithm
class Dijsktra:
    def __init__(self):
        self.heap=[]
    def calculate(self,start_vertex):
        start_vertex.min_distance=0
        heapq.heappush(self.heap,start_vertex)
        while self.heap:
            actual_vertex=heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbors:
                start=edge.start_vertex
                target=edge.target_vertex
                new_distance=start.min_distance+edge.weight
                if new_distance < target.min_distance:
                    target.min_distance=new_distance
                    target.predecessor=start
                    #update the heap
                    heapq.heappush(self.heap,target)
            actual_vertex.visited = True
    def get_shortest_path(self,vertex):
        print(f"The shortest path to the vertex is :  {vertex.min_distance}")
        actual_vertex=vertex
        while actual_vertex is not None:
            print(actual_vertex.name,end=" ")
            actual_vertex=actual_vertex.predecessor

#Step 1 - Create Nodes:
NodeA=Node("A")
NodeB=Node("B")
NodeC=Node("C")
NodeD=Node("D")
NodeE=Node("E")
NodeF=Node("F")
NodeG=Node("G")
NodeH=Node("H")
#Step - 2 : Create Edges:
NodeA.add_Edge(6,NodeB)
NodeA.add_Edge(9,NodeD)
NodeA.add_Edge(10,NodeC)

NodeB.add_Edge(5,NodeD)
NodeB.add_Edge(13,NodeF)
NodeB.add_Edge(16,NodeE)

NodeC.add_Edge(6,NodeD)
NodeC.add_Edge(5,NodeH)
NodeC.add_Edge(21,NodeG)

NodeD.add_Edge(8,NodeF)
NodeD.add_Edge(7,NodeH)

NodeF.add_Edge(4,NodeE)
NodeF.add_Edge(12,NodeG)

NodeE.add_Edge(10,NodeG)

NodeH.add_Edge(21,NodeG)
NodeH.add_Edge(2,NodeF)
DijsktraAlgorithm=Dijsktra()
DijsktraAlgorithm.calculate(NodeA)
DijsktraAlgorithm.get_shortest_path(NodeB)



