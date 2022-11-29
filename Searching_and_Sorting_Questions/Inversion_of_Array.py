def InverseArray(li):
    newList=[]
    print(len(li))
    for i in range(0,len(li)):
        for j in range(i+1,len(li)):
            if li[i] > li[j]:
                newList.append(tuple((li[i],li[j])))
    return newList;


list1=[1,20,6,4,5];
list2=[8,4,2,1]
print(InverseArray(list2))