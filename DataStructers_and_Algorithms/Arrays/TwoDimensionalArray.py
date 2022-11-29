import numpy as np
#Creating a 2-D Array
TwoDArray=np.array([[11,15,10,6], [10,14,9,5], [9,13,8,4], [8,12,7,3]])
print(TwoDArray)

# Insertion in 2D Array
# Adding a Column -  TC:O(MN)
newTwoDarray=np.insert(TwoDArray,2,[[1,2,3,4]],axis=1) #axis =1 means adding a column
print(newTwoDarray)
# Adding a Row -  TC: O(MN)
newTwoDarray1=np.insert(TwoDArray,0,[[1,2,3,4]],axis=0) #axis =0 means adding row
print(newTwoDarray1)

# Accessing elements of a Two Dimensional Array - TC: O(1) and SC: O(1)
def accessElements(array,rowIndex,colIndex):
    if rowIndex >=len(array) and colIndex >=len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])
accessElements(TwoDArray,2,1)

# Traversal in 2D array - TC: O(MN) SC: O(1)
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=",")
        print()

traverseTDArray(TwoDArray)

#Searching in 2D Array:  TC:O(MN)
def Search2Darray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return str(i)+" "+str(j)
    return'Element not Found'
print(Search2Darray(TwoDArray,144))

# Deletion in 2D Array:
#Deleting a Column - TC: O(MN) SC: O(1)
newTwoDarray2=np.delete(TwoDArray,0,axis=1)# it has three arguments arrayName, Column index, axis
print(newTwoDarray2)

#Deleting a Row - Tc: O(MN) SC: O(1)
newTwoDarray3=np.delete(TwoDArray,0,axis=0)# it has three arguments arrayName, row index, axis
print(newTwoDarray3)


