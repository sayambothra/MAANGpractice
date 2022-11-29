# Q4. How to find maximum product of two integers in the array where all elements are positive

# TC:O(n)
import numpy as np

myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])
sortedArray = sorted(myArray)
print(sortedArray)
print(sortedArray[-1] * sortedArray[-2])


# Udemy Solution: TC:O(n^2)
def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i]) + "," + str(array[j])
    print(pairs)
    print(maxProduct)


findMaxProduct(myArray)

# Q5. Is Unique: Implement an algorithm to determine if a list has all unique characters,using python list
Ulist = [1.20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 19, 27, 58]
NUlist = []


def UniqueEle(array):
    for i in range(len(Ulist)):
        for j in range(i + 1, len(Ulist)):
            if Ulist[i] == Ulist[j]:
                return False
    return True


print(UniqueEle(Ulist))


# udemy Solution:
def isUnique(list):
    a = []
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True


print(isUnique(Ulist))

# Q6 - Permutation: Having same elements in different order
# TC:O(n)
list1 = ['s', 'a', 'y']
list2 = ['y', 'a', 'd']


def Permutation(list1, list2):
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] not in list2:
                return False
        return True
    return 'Number of elements in both the lists are not Equal'


print(Permutation(list1, list2))

# Q7. Rotate Matrix:
import numpy as np

Rarray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(Rarray[1][1])
print(len(Rarray[0]))
print(Rarray)
Tarray=[]
for i in range(0,3):
    Varray=[]
    for j in range(3,0,-1):
        value=Rarray[j-1][i]
        Varray.append(value)
    Tarray.append(Varray)
print(Tarray)


