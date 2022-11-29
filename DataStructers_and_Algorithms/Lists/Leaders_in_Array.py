'''Write a program to print all the Leaders in the array. An element is a leader
if it is greater than all the elements to its right side. And the rightmost
element is always the leader.'''


myList=[1,2,3,4,5,2]

def LeaderArray(list1):
    newList = []
    for i in range(0,len(list1)-1):
        count=0
        for j in range(i+1,len(list1)):
            if list1[i] < list1[j]:
                count=count+1
        if(count ==0):
            newList.append(list1[i])
    newList.append(list1[-1])
    return newList



print(LeaderArray(myList))
