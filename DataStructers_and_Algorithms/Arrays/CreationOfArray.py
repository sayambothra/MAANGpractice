
from array import *
#Array Creation
arr1=array('i',[1,2,3,4,5,6])
#Array Insertion
arr1.insert(2,9)
for i in arr1:
    print(i,end="")
#Accesing an Element of an Array: TC: O(1) SC: O(1)
def accessElement(array,index):
    if index >=len(array):
        print('There is no element at this index')
    else:
        print(array[index])
accessElement(arr1,6)
# Deleting an Element from an array:
arr1.remove(4)
for i in arr1:
    print(i,end="")