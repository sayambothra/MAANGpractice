list1=[2,3,6,7,9]
list2=[1,4,8,10]
def KthElement(list1,list2,k):
    newList=list1+list2
    newList.sort()
    print(newList)
    return newList[k-1]


print(KthElement(list1,list2,5))