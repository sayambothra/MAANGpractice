from array import *
#1.Create an array and traverse

myArray=array('i',[1,2,3,4,5])
for i in myArray:
    print(i,end=",")
print()
#2. Access individual elements through indexes
print(myArray[0])

#3.Append any value to the array using append() method
myArray.append(6) #append()- adds value to the end of an array
print(myArray)
#4.Insert value in an array using insert() method
myArray.insert(6,7) # insert() -takes two arguments 1st position 2nd Value
print(myArray)
#5.Extend python array using extend() method
myArray2=array('i',[8,9,10])
myArray.extend(myArray2)
print(myArray)
#6. Add items from list into array using fromlist() method
tempList=[11,12,13]
myArray.fromlist(tempList)
print(myArray)
#7.Remove any array element using remove() method
myArray.remove(11)
print(myArray)
#8. Remove las array element using pop() method
myArray.pop()
print(myArray)
#9. Fetch any element through its index using index() method
print(myArray.index(6)) # returns index position of 6
#10. reverse a python array using reverse() method
myArray.reverse()
print(myArray)
#11. Get array buffer information through buffer_info() method
binfo=myArray.buffer_info()
print(binfo) # returns the starting memory location and number of elements in the array
#12. Check for number of occurences of an element using count() method
myArray.append(7)
print(myArray.count(7))
#13. Convert array to string using tostring()/tobytes() method
strTemp=myArray.tobytes()
print(strTemp)
# ints=array('i')
# int.from_bytes(strTemp)
# print(ints)
#14. Convert array to a python list with same elements uing tolist() method
print(myArray.tolist())
#15.Slice elements from an array:
print(myArray[:4])




