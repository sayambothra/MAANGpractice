myList=[1,2,3,4,5,6,7,8]
def ReverseInGroup(list1,k):
    list2=[]
    for i in range(0,len(list1),k):
        nl=[]
        for j in range(i,i+k):
            if(j>=len(list1)):
                break
            nl.append(list1[j])
        nl.reverse()
        #print(nl)
        list2=list2+nl
    return list2
print(myList)
print(ReverseInGroup(myList,5))
