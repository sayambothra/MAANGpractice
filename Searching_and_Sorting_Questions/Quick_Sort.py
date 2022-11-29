def Partition(li,l,r):
    i=l-1
    pivot=li[r]
    for j in range(l,r):
        if li[j]<=pivot:
            i+=1
            li[i],li[j]=li[j],li[i]
    li[i+1],li[r]=li[r],li[i+1]
    return (i+1)
def QuickSort(li,start,end):
    if start <=end:
        divide=Partition(li,start,end)
        QuickSort(li,start,divide-1)
        QuickSort(li,divide+1,end)
    return li

list1=[10,80,30,90,40,50,70]
print(QuickSort(list1,0,len(list1)-1))

