INF=999
def printSolution(nV,distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF",end=" ")
            else:
                print(distance[i][j],end=" ")
        print(" ")

def FloydWarshall(nV, G): #TC:0(v^3),SC:O(v^2)
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
    printSolution(nV,distance)

G=[[0,8,INF,1],
   [INF,0,1,INF],
   [4,INF,0,1],
   [INF,2,9,1]

   ]

FloydWarshall(4,G)