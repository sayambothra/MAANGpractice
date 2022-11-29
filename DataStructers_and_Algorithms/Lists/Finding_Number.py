import numpy as np
myArray=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
def findNumber(array,value):
    for i in array:
        if array[i] == value:
            return True
        else:
            return 'Element does not Exist'
print(findNumber(myArray,69))