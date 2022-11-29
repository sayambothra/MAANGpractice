def KthSmallest(li,k):
    for i in range(0,len(li)):
        min_index=i
        for j in range(i+1,len(li)):
            if li[min_index] > li[j]:
                min_index=j
        li[i],li[min_index]=li[min_index],li[i]
    print(li)
    return li[k-1]

list1=[7,10,4,3,20,15]
print(KthSmallest(list1,3))


