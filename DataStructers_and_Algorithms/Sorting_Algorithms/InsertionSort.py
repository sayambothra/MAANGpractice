"""
Insertion Sort:
- Divide the given array into two part
- Take first element from unsorted array and find its correct position in sorted array
- Repeat until sorted array
TC:O(n^2),SC:O(1)
When to use Insertion Sort?
When we have contionous inflow of numbers and want to keep them sorted
"""

def InsertionSort(li):
    for i in range(1,len(li)):
        key=li[i]
        j=i-1
        while j>=0 and key < li[j]:
            li[j+1]=li[j]
            j-=1
        li[j+1] = key
    return li

print(InsertionSort([2,7,1,6,5]))


