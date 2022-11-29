import numpy as np

myArray = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])

for i in range(len(myArray)):
    for j in range(i+1,len(myArray)):
        if myArray[i] < myArray[j]:
            temp=myArray[i]
            myArray[i]=myArray[j]
            myArray[j]=temp
print()
print(myArray[0],myArray[1],end= " = ")
print(myArray[0]*myArray[1])

#Udemy Solution
def findMaxProduct(array):
    maxProduct=0
    for i in range(len(myArray)):
        for j in range(i+1,len(myArray)):
            if myArray[i]*myArray[j]>maxProduct:
                maxProduct=myArray[i]*myArray[j]
                pairs=str(myArray[i]+","+myArray[j])
    print(pairs)
    print(maxProduct)
findMaxProduct(myArray)