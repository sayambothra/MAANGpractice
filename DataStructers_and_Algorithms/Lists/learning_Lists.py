#Creating a List
import random

integers=[1,2,3,4]
print(integers)
# Accessing/Traversing the list
shoppingList=['Milk','Cheese','Butter']
print(shoppingList[0])
print(shoppingList[::-1])
print('Milk' in shoppingList) #returns True or false based on whether the value exists in the list or not
print(shoppingList[-1]) # return last element of the list

# traversing the list:
for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i]=shoppingList[i]+"+"
    print(shoppingList[i])

#Update/Insert - List
myList=[1,2,3,4,5,6,7]
print(myList)
myList[2]=33 #update an element in the list TC:0(1),SC:0(1
print(myList)
#inserting an element to the beginning of the list - TC:O(1),SC:O(1)
#Inserting an element to any given place in the list using insert() method - TC:O(n),SC:O(1)
myList.insert(1,11) #insert(index,value)
print(myList)
#Inserting an element to the end of the list - TC:O(1),SC:O(1)
myList.append(55)
#Inserting another list to the list - TC:O(n),SC:O(n)
newList=[10,20,30]
myList.extend(newList)
print(myList)

#Slice/Delete from List:
myList1=['a','b','c','d','e','f']
myList1[0:2]=[1,2] #updating multiple elements in a list
print(myList1)
print(myList1[0:2])
myList1.pop(1) #pop() - takes index as an argument - TC:O(1)/0(n),SC:O(1)
print(myList1)
del myList1[4] #deleting an element using index -TC:O(n),SC:O(1)
del myList1[0:2] #deleting multiple elements using index range
myList1.remove('e') #remove-delete an element by knowing element directly and not index- TC:O(n),SC:O(1)
print(myList1)

#Searching for an element in the List
myList2=[10,20,30,40,50,60,70,80,90]
#Using IN operator
if 20 in myList2:   # TC:0(n)
    print(myList2.index(20))
else:
    print('The value does not exist in the list')

#Using Linear Serach:  TC:O(n),SC:O(1)
def searchinList(list,value):
    for i in list:
        if i==value:
            return list.index(value)
    return 'The value does not exist'
print(searchinList(myList2,50))

#List-Operations
a=[1,2,3]
b=[4,5,6]
c=[]
for i in range(len(a)):
    c.append((a[i]+b[i]))
print(c)

a=[0,1]
a=a*4 # * operator - makes our elements in the list to be repititve
print(a)

#List- Functions
  #len()- returns count of elements in the list
  #max() -returns highest element in the list
  #min() -returns lowest element in the list
  #sum() -returns sum of all elements in the list
# listChallenge=[]
# while True:
#     inp=input('Enter a number')
#     if inp=='done':
#         break
#     else:
#         listChallenge.append(float(inp))
# Average=sum(listChallenge)/len(listChallenge)
# print(Average)

#Strings and Lists

name='Sayam-Bothra'
b=list(name) # convert a String to a list usin list() method
delimiter='-'
c=name.split(delimiter)
print(b)
print(c)
print(delimiter.join(c))  # Convert a list to String using join() method

test=[2,4,1,3]
sorttest=sorted(test)
print(test)
print(sorttest)

# lists Vs Arrays
#-Arithmetic Operations
import numpy as np
myArray=np.array([1,2,3,4,5,'a'])
Alist=[1,2,3,4,5,'a']
print(myArray)
print(Alist)
# print(myArray/2)
# print(Alist/2)
a1=[1,2,3,4,5,6,7,8,9]
print(a1[3:0:-1])
#print(random.shuffle(a1))
#print(a1[::-1])
arr=[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
for i in range(0,4):
    print(arr[i])
    print(arr[i].pop())

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6):
    print(arr[i], end = " ")

def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])
# will ask Anish today at 4PM
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = 'Guava'
fruit_list1[1] = 'Banana'
fruit_list3[1] = 'Kiwi'

sum = 0
print(fruit_list1)
print(fruit_list2)
print(fruit_list3)
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        #print(ls[0])
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)





