"""
Quick Sort:
 -It is a divide and conquer algorithm
 -Find pivot number and make sure smaller numbers are located on the left of pivot
  and bigger numbers are located on the right of the pivot
 -Unlike merge sort extra space is not required

TC:O(NlogN),SC:O(1)
"""

def Partition(li,l,r):
    i=l-1
    pivot=li[r]
    for j in range(l,r):
        if li[j] <=pivot:
            i+=1
            li[i],li[j]=li[j],li[i]
    li[i+1],li[r] =li[r],li[i+1]
    return (i+1)

def QuickSort(li,start,end):
    if start < end:
        pi=Partition(li,start,end)  #--->O(n)
        QuickSort(li,start,pi-1) #--->O(n/2)
        QuickSort(li,pi+1,end)  #--->O(n/2)
    return li

li=[2,1,7,6,5,3,4,9,8]
print(QuickSort(li,0,8))


