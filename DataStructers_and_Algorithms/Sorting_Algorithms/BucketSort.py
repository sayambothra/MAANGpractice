"""
Bucket Sort
- Create buckets and distribute elements of array into buckets
- Sort Buckets individually
- Merge buckets after sorting

Number of Buckets - round(Sqrt(number of elements))
Appropriate bucket =ceil(Value * number of buckets/maxValue)

TC:O(n^2)/O(NlogN),SC:O(n)
When to use Bucket Sort?
- When input uniformly distributed
"""
import math
print("Hello")
def InsertionSort(li):
    for i in range(1,len(li)):
        key=li[i]
        j=i-1
        while j>=0 and key <li[j]:
            li[j+1]=li[j]
            j-=1
        li[j+1] =key
    return li


def BucketSort(li):
    numberOfBuckets=round(math.sqrt(len(li)))
    arr=[]
    maxValue=max(li)
    for i in range(numberOfBuckets):
        arr.append([])
    for j in li:
        appValue=math.ceil(j*numberOfBuckets/maxValue)
        arr[appValue-1].append(j)

    for i in range(numberOfBuckets):
       arr[i] = InsertionSort(arr[i])

    k=0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            li[k]=arr[i][j]
            k += 1

    return li




print(BucketSort([2,7,6,1,3]))
