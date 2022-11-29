def SortElements(li):
    nl=[]
    countList=[]
    for i in range(0,len(li)):
        min_index=i
        for j in range(i+1,len(li)):
            if li[min_index]>li[j]:
                min_index=j
        li[i],li[min_index]=li[min_index],li[i]
    nl=set(li)
    nl=list(nl)
    nl.sort()
    print(nl)
    for i in range(len(nl)):
        countList.append([nl[i],li.count(nl[i])])
    print(countList)
    sortedCL=sorted(countList,key=lambda countList:countList[1],reverse=True)
    print(sortedCL)
    Sl=[]
    for i in range(len(sortedCL)):
        for j in range(sortedCL[i][1]):
            Sl.append(sortedCL[i][0])

    return Sl





li=[2,5,2,6,-1,99999,5,8,8,8]
print(SortElements(li))
