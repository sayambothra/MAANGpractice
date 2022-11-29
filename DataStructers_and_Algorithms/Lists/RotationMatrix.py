matrix=[[1,2,3],[4,5,6],[7,8,9]]
RotataryMatrix=[[0,0,0],[0,0,0],[0,0,0]]

print(len(matrix[0]))
print(len(matrix))
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        RotataryMatrix[j][len(matrix)-1-i]=matrix[i][j]

print(RotataryMatrix)